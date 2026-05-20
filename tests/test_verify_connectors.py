import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import verify_connectors as connectors  # noqa: E402


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_connector(root: Path, name: str, server_text: str | None = None) -> None:
    write(root / "connectors" / name / "README.md", f"# {name}\n")
    write(root / "connectors" / name / "example.md", "example\n")
    write(
        root / "connectors" / name / "server.py",
        server_text
        or (
            "import argparse\n"
            "import json\n"
            "parser = argparse.ArgumentParser()\n"
            "sub = parser.add_subparsers(dest='command', required=True)\n"
            "sub.add_parser('search')\n"
            "sub.add_parser('fetch')\n"
            "headers={'User-Agent': 'fixture'}\n"
            "print(json.dumps([]))\n"
        ),
    )


def write_lean_connector(root: Path) -> None:
    write(root / "connectors" / "lean" / "README.md", "# lean\n")
    write(root / "connectors" / "lean" / "example.md", "example\n")
    write(
        root / "connectors" / "lean" / "server.py",
        "import argparse\n"
        "import json\n"
        "parser = argparse.ArgumentParser()\n"
        "sub = parser.add_subparsers(dest='command', required=True)\n"
        "sub.add_parser('check')\n"
        "sub.add_parser('env')\n"
        "print(json.dumps({'ok': True}))\n",
    )


class ConnectorVerifierTest(unittest.TestCase):
    def test_valid_connector_contracts_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_connector(root, "arxiv")
            write_connector(root, "oeis")
            write(
                root / "prompts" / "subagents" / "researcher.md",
                "invoke connectors/arxiv/server.py\ninvoke connectors/oeis/server.py\n",
            )

            result = connectors.check_connectors(root)

        self.assertEqual([], result.fail)

    def test_missing_example_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_connector(root, "arxiv")
            write_connector(root, "oeis")
            (root / "connectors" / "arxiv" / "example.md").unlink()
            write(
                root / "prompts" / "subagents" / "researcher.md",
                "invoke connectors/arxiv/server.py\ninvoke connectors/oeis/server.py\n",
            )

            result = connectors.check_connectors(root)

        self.assertTrue(any("missing connectors/arxiv/example.md" in item for item in result.fail), result.fail)

    def test_missing_researcher_invocation_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_connector(root, "arxiv")
            write_connector(root, "oeis")
            write(root / "prompts" / "subagents" / "researcher.md", "invoke connectors/arxiv/server.py\n")

            result = connectors.check_connectors(root)

        self.assertTrue(any("researcher.md missing connectors/oeis/server.py" in item for item in result.fail), result.fail)

    def test_lean_connector_uses_check_env_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_connector(root, "arxiv")
            write_connector(root, "oeis")
            write_lean_connector(root)
            write(
                root / "prompts" / "subagents" / "researcher.md",
                "invoke connectors/arxiv/server.py\n"
                "invoke connectors/oeis/server.py\n"
                "invoke connectors/lean/server.py\n",
            )

            result = connectors.check_connectors(root)

        self.assertEqual([], result.fail)
        self.assertTrue(
            any("connectors/lean/server.py exposes check/env JSON CLI contract" in item for item in result.ok),
            result.ok,
        )


if __name__ == "__main__":
    unittest.main()
