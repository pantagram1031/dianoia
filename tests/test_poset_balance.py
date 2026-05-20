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
        self.assertEqual((2, 1), pb.rank_shape(poset))
        self.assertEqual([[0, 1], [2]], pb.rank_layers(poset))
        self.assertEqual([0, 1], pb.minimal_elements(poset))
        self.assertEqual([2], pb.maximal_elements(poset))
        self.assertEqual([[0, 2], [0, 0]], pb.cover_rank_matrix(poset))

    def test_structural_profile_records_layer_vertex_signatures(self) -> None:
        profile = pb.structural_profile(pb.make_poset(3, [(0, 2), (1, 2)]))

        self.assertIn("cover_rank_matrix", profile)
        self.assertIn("rank_layer_vertex_signatures", profile)
        self.assertEqual([[0, 2], [0, 0]], profile["cover_rank_matrix"])
        self.assertEqual(
            [
                [[0, 1, 1, [0, 0], [0, 1]], [0, 1, 1, [0, 0], [0, 1]]],
                [[2, 0, 0, [2, 0], [0, 0]]],
            ],
            profile["rank_layer_vertex_signatures"],
        )

    def test_rank_normal_form_uses_layer_labels(self) -> None:
        normal = pb.rank_normal_form(pb.make_poset(3, [(0, 2), (1, 2)]))

        self.assertEqual([["a", "b"], ["c"]], normal["rank_layers"])
        self.assertEqual(["a<c", "b<c"], normal["cover_relations"])
        self.assertEqual(["a", "b"], normal["minimal_elements"])
        self.assertEqual(["c"], normal["maximal_elements"])

    def test_named_case_reports_named_pair_counts(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            case = Path(temp_dir) / "case.json"
            output = Path(temp_dir) / "report.json"
            case.write_text(
                json.dumps(
                    {
                        "labels": ["a", "b", "c"],
                        "cover_relations": ["a<c", "b<c"],
                        "check_pairs": [["a", "b"]],
                    }
                ),
                encoding="utf-8",
            )
            with redirect_stdout(StringIO()):
                code = pb.main(["named-case", str(case), "--output", str(output)])

            self.assertEqual(0, code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(2, payload["linear_extensions"])
            self.assertEqual(["a<c", "b<c"], payload["cover_relations"])
            self.assertEqual([1, 2], payload["check_pairs"][0]["first_before_second"])
            self.assertEqual([1, 2], payload["check_pairs"][0]["second_before_first"])

    def test_named_case_recurrence_reports_root_split(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            case = Path(temp_dir) / "case.json"
            output = Path(temp_dir) / "trace.json"
            case.write_text(
                json.dumps(
                    {
                        "labels": ["a", "b", "c"],
                        "cover_relations": ["a<c", "b<c"],
                        "check_pairs": [["a", "b"]],
                    }
                ),
                encoding="utf-8",
            )
            with redirect_stdout(StringIO()):
                code = pb.main(
                    ["named-case-recurrence", str(case), "--output", str(output)]
                )

            self.assertEqual(0, code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(2, payload["linear_extensions"])
            self.assertEqual(1, payload["trace"]["first_before_second"])
            self.assertEqual(1, payload["trace"]["second_before_first"])
            self.assertEqual(["a", "b"], [item["choose"] for item in payload["trace"]["available"]])

    def test_named_case_recurrence_can_emit_nested_split(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            case = Path(temp_dir) / "case.json"
            output = Path(temp_dir) / "trace.json"
            case.write_text(
                json.dumps(
                    {
                        "labels": ["a", "b", "c", "d"],
                        "cover_relations": ["a<c", "b<d"],
                        "check_pairs": [["c", "d"]],
                    }
                ),
                encoding="utf-8",
            )
            with redirect_stdout(StringIO()):
                code = pb.main(
                    [
                        "named-case-recurrence",
                        str(case),
                        "--depth",
                        "2",
                        "--output",
                        str(output),
                    ]
                )

            self.assertEqual(0, code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(2, payload["depth"])
            root_choices = payload["trace"]["available"]
            self.assertEqual(["a", "b"], [item["choose"] for item in root_choices])
            self.assertIn("subtrace", root_choices[0])
            self.assertEqual(["a"], root_choices[0]["subtrace"]["placed"])
            self.assertEqual(
                ["b", "c"],
                [item["choose"] for item in root_choices[0]["subtrace"]["available"]],
            )

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

    def test_exhaustive_unlabeled_can_filter_width(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "summary.json"
            with redirect_stdout(StringIO()):
                code = pb.main(
                    [
                        "exhaustive-unlabeled",
                        "--max-n",
                        "5",
                        "--width",
                        "3",
                        "--output",
                        str(output),
                    ]
                )

            self.assertEqual(0, code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(3, payload["filters"]["width"])
            self.assertEqual(29, payload["summary"][-1]["total_posets"])

    def test_exhaustive_unlabeled_can_filter_rank_shape(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "summary.json"
            with redirect_stdout(StringIO()):
                code = pb.main(
                    [
                        "exhaustive-unlabeled",
                        "--max-n",
                        "5",
                        "--width",
                        "3",
                        "--rank-shape",
                        "2,2,1",
                        "--output",
                        str(output),
                    ]
                )

            self.assertEqual(0, code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual([2, 2, 1], payload["filters"]["rank_shape"])
            self.assertGreater(payload["summary"][-1]["total_posets"], 0)

    def test_extremal_width_records_profiles(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "extremal.json"
            with redirect_stdout(StringIO()):
                code = pb.main(
                    [
                        "extremal-width",
                        "--max-n",
                        "5",
                        "--width",
                        "3",
                        "--limit",
                        "1",
                        "--output",
                        str(output),
                    ]
                )

            self.assertEqual(0, code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(1, len(payload["records"]))
            record = payload["records"][0]
            self.assertEqual([4, 11], record["lower_orientation_probability"])
            self.assertEqual([1, 33], record["gap_above_one_third"])
            self.assertIn("rank_layer_sizes", record["profile"])

    def test_shape_classes_groups_profiles(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "classes.json"
            with redirect_stdout(StringIO()):
                code = pb.main(
                    [
                        "shape-classes",
                        "--max-n",
                        "5",
                        "--width",
                        "3",
                        "--rank-shape",
                        "2,2,1",
                        "--output",
                        str(output),
                    ]
                )

            self.assertEqual(0, code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertGreater(payload["bucket_count"], 0)
            self.assertGreater(payload["total_posets"], 0)
            self.assertIn("examples", payload["buckets"][0])

    def test_shape_classes_fine_signature_mode(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "classes.json"
            with redirect_stdout(StringIO()):
                code = pb.main(
                    [
                        "shape-classes",
                        "--max-n",
                        "5",
                        "--width",
                        "3",
                        "--rank-shape",
                        "2,2,1",
                        "--signature",
                        "fine",
                        "--output",
                        str(output),
                    ]
                )

            self.assertEqual(0, code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual("fine", payload["signature_mode"])
            self.assertGreater(payload["bucket_count"], 0)
            self.assertIn("cover_matrix=", payload["buckets"][0]["signature"])

    def test_shape_classes_matrix_signature_mode(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "classes.json"
            with redirect_stdout(StringIO()):
                code = pb.main(
                    [
                        "shape-classes",
                        "--max-n",
                        "5",
                        "--width",
                        "3",
                        "--rank-shape",
                        "2,2,1",
                        "--signature",
                        "matrix",
                        "--output",
                        str(output),
                    ]
                )

            self.assertEqual(0, code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual("matrix", payload["signature_mode"])
            self.assertGreater(payload["bucket_count"], 0)
            self.assertIn("cover_matrix=", payload["buckets"][0]["signature"])
            self.assertNotIn("layer_vertex_signatures=", payload["buckets"][0]["signature"])

    def test_bucket_members_extracts_all_matching_profiles(self) -> None:
        bucket = (
            "layers=2,2,1|covers=4|mins=2|maxs=2|"
            "cover_matrix=[[0,2,1],[0,0,1],[0,0,0]]"
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "members.json"
            with redirect_stdout(StringIO()):
                code = pb.main(
                    [
                        "bucket-members",
                        "--max-n",
                        "5",
                        "--width",
                        "3",
                        "--rank-shape",
                        "2,2,1",
                        "--signature",
                        "matrix",
                        "--bucket",
                        bucket,
                        "--output",
                        str(output),
                    ]
                )

            self.assertEqual(0, code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual("matrix", payload["signature_mode"])
            self.assertEqual(bucket, payload["bucket"])
            self.assertEqual(1, payload["record_count"])
            self.assertEqual([4, 11], payload["records"][0]["lower_orientation_probability"])
            self.assertIn("rank_normal_form", payload["records"][0])
            self.assertIn("cover_relations", payload["records"][0]["rank_normal_form"])

    def test_cover_matrix_forms_derives_rank_normal_forms(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "forms.json"
            with redirect_stdout(StringIO()):
                code = pb.main(
                    [
                        "cover-matrix-forms",
                        "--rank-shape",
                        "2,1",
                        "--cover-matrix",
                        "[[0,2],[0,0]]",
                        "--width",
                        "2",
                        "--height",
                        "2",
                        "--output",
                        str(output),
                    ]
                )

            self.assertEqual(0, code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(1, payload["form_count"])
            self.assertEqual(["a<c", "b<c"], payload["forms"][0]["cover_relations"])


if __name__ == "__main__":
    unittest.main()
