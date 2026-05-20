import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import no_three_in_line_verify as nti  # noqa: E402


class NoThreeInLineVerifierTest(unittest.TestCase):
    def test_accepts_valid_2n_certificate(self) -> None:
        points = [
            (0, 0),
            (0, 1),
            (1, 2),
            (1, 3),
            (2, 0),
            (2, 1),
            (3, 2),
            (3, 3),
        ]

        result = nti.verify_points(
            4,
            points,
            require_2n=True,
            require_two_per_row=True,
            require_two_per_column=True,
        )

        self.assertTrue(result.ok, result.errors)
        self.assertEqual([], result.line_violations)

    def test_rejects_three_collinear_points(self) -> None:
        result = nti.verify_points(4, [(0, 0), (1, 1), (2, 2)])

        self.assertFalse(result.ok)
        self.assertTrue(any("lines containing" in error for error in result.errors), result.errors)
        self.assertEqual([(1, -1, 0)], [line for line, _ in result.line_violations])

    def test_rejects_duplicate_and_out_of_bounds_points(self) -> None:
        result = nti.verify_points(3, [(0, 0), (0, 0), (3, 1)])

        self.assertFalse(result.ok)
        self.assertIn("duplicate point: (0, 0)", result.errors)
        self.assertIn("point outside 3x3 grid: (3, 1)", result.errors)

    def test_parse_json_certificate(self) -> None:
        text = json.dumps({"n": 2, "points": [[0, 0], [0, 1], [1, 0], [1, 1]]})

        n, points = nti.parse_certificate_text(text)

        self.assertEqual(2, n)
        self.assertEqual([(0, 0), (0, 1), (1, 0), (1, 1)], points)

    def test_parse_table_entry_certificate(self) -> None:
        text = "N=2: [(0, 0), (0, 1), (1, 0), (1, 1)]"

        n, points = nti.parse_certificate_text(text)

        self.assertEqual(2, n)
        self.assertEqual([(0, 0), (0, 1), (1, 0), (1, 1)], points)

    def test_cli_returns_nonzero_for_invalid_certificate(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "bad.json"
            path.write_text(
                json.dumps({"n": 3, "points": [[0, 0], [1, 1], [2, 2]]}),
                encoding="utf-8",
            )

            with redirect_stdout(StringIO()):
                code = nti.main([str(path)])

        self.assertEqual(1, code)


if __name__ == "__main__":
    unittest.main()
