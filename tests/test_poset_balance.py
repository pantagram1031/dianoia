import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import poset_balance as pb  # noqa: E402


class PosetBalanceTest(unittest.TestCase):
    def test_antichain_pair_is_balanced(self) -> None:
        report = pb.balance_report(pb.make_poset(2, []))

        self.assertEqual(2, report["linear_extensions"])
        self.assertTrue(report["has_balanced_pair"])
        self.assertEqual([1, 2], report["best_pair"]["x_before_y"])

    def test_chain_has_no_incomparable_pair(self) -> None:
        report = pb.balance_report(pb.make_poset(3, [(0, 1), (1, 2)]))

        self.assertEqual(1, report["linear_extensions"])
        self.assertFalse(report["has_balanced_pair"])
        self.assertEqual(0, report["incomparable_pair_count"])

    def test_transitive_closure_rejects_cycle(self) -> None:
        with self.assertRaises(ValueError):
            pb.make_poset(2, [(0, 1), (1, 0)])

    def test_labeled_poset_enumeration_matches_small_counts(self) -> None:
        self.assertEqual(3, len(pb.all_labeled_posets(2)))
        self.assertEqual(19, len(pb.all_labeled_posets(3)))

    def test_unlabeled_poset_enumeration_matches_small_counts(self) -> None:
        self.assertEqual(2, len(pb.all_unlabeled_posets(2)))
        self.assertEqual(5, len(pb.all_unlabeled_posets(3)))
        self.assertEqual(16, len(pb.all_unlabeled_posets(4)))
        self.assertEqual(63, len(pb.all_unlabeled_posets(5)))
        self.assertEqual(318, len(pb.all_unlabeled_posets(6)))

    def test_width_and_height_for_v_poset(self) -> None:
        poset = pb.make_poset(3, [(0, 2), (1, 2)])

        self.assertEqual(2, pb.width(poset))
        self.assertEqual(2, pb.height(poset))

    def test_exhaustive_small_finds_no_counterexample_through_four(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "summary.json"
            with redirect_stdout(StringIO()):
                code = pb.main(["exhaustive-small", "--max-n", "4", "--output", str(output)])

            self.assertEqual(0, code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(0, payload["counterexample_count"])
            self.assertEqual(219, payload["summary"][-1]["labeled_posets"])

    def test_exhaustive_unlabeled_records_structural_summaries(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "summary.json"
            with redirect_stdout(StringIO()):
                code = pb.main(
                    ["exhaustive-unlabeled", "--max-n", "4", "--output", str(output)]
                )

            self.assertEqual(0, code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            last = payload["summary"][-1]
            self.assertEqual(16, last["total_posets"])
            self.assertEqual(0, last["counterexample_count"])
            self.assertIn("width_distribution", last)
            self.assertIn("worst_by_width", last)

    def test_one_point_extension_keeps_unlabeled_representatives(self) -> None:
        levels = pb.all_unlabeled_posets_by_extension(4)

        self.assertEqual([1, 2, 3, 4], list(levels))
        self.assertEqual(16, len(levels[4]))


if __name__ == "__main__":
    unittest.main()
