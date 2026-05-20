import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import no_three_in_line_frontier as frontier  # noqa: E402


SAMPLE_TABLE = """
Header.
N=2: [(0, 0), (0, 1), (1, 0), (1, 1)] N=4: [(0, 0), (0, 1), (1, 2), (1, 3), (2, 0), (2, 1), (3, 2), (3, 3)]
"""

SAMPLE_TABLE_WITH_TRAILING_PROSE = """
N=2: [(0, 0), (0, 1), (1, 0), (1, 1)] Configurations for N<2 are trivial.
"""


class NoThreeInLineFrontierTest(unittest.TestCase):
    def test_extract_table_entries(self) -> None:
        entries = frontier.extract_table_entries(SAMPLE_TABLE)

        self.assertEqual([2, 4], list(entries))
        self.assertEqual(4, len(entries[2]))
        self.assertEqual(8, len(entries[4]))

    def test_extract_final_entry_before_trailing_prose(self) -> None:
        entries = frontier.extract_table_entries(SAMPLE_TABLE_WITH_TRAILING_PROSE)

        self.assertEqual([2], list(entries))
        self.assertEqual(4, len(entries[2]))

    def test_decode_flammenkamp_configuration(self) -> None:
        symmetry, points = frontier.decode_flammenkamp_configuration(".0101", 2)

        self.assertEqual(".", symmetry)
        self.assertEqual([(0, 0), (1, 0), (0, 1), (1, 1)], points)

    def test_extract_command_writes_and_verifies_certificates(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            table = root / "table.txt"
            table.write_text(SAMPLE_TABLE, encoding="utf-8")

            with redirect_stdout(StringIO()):
                code = frontier.main(
                    [
                        "extract",
                        str(table),
                        "--output-dir",
                        str(root / "certificates"),
                        "--source-url",
                        "https://example.test/table.txt",
                        "--retrieved-date",
                        "2026-05-20",
                    ]
                )

            self.assertEqual(0, code)
            summary = json.loads(
                (root / "certificates" / "prellberg-frontier-summary.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertTrue(summary["ok"], summary)
            self.assertEqual(2, len(summary["certificates"]))

    def test_flammenkamp_command_writes_and_verifies_certificate(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            encoded = root / "n2_iden"
            encoded.write_text(".0101\n", encoding="ascii")

            with redirect_stdout(StringIO()) as stdout:
                code = frontier.main(
                    [
                        "flammenkamp",
                        str(encoded),
                        "--n",
                        "2",
                        "--output-dir",
                        str(root / "certificates"),
                        "--source-url",
                        "https://example.test/n2_iden",
                        "--retrieved-date",
                        "2026-05-20",
                    ]
                )

            self.assertEqual(0, code)
            payload = json.loads(stdout.getvalue())
            self.assertTrue(payload["ok"], payload)
            certificate = root / "certificates" / "flammenkamp-n2.json"
            self.assertTrue(certificate.exists())

    def test_verify_dir_rejects_bad_certificate(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            cert_dir = Path(temp_dir)
            (cert_dir / "prellberg-n3.json").write_text(
                json.dumps({"n": 3, "points": [[0, 0], [1, 1], [2, 2]]}),
                encoding="utf-8",
            )

            with redirect_stdout(StringIO()):
                code = frontier.main(["verify-dir", str(cert_dir)])

        self.assertEqual(1, code)


if __name__ == "__main__":
    unittest.main()
