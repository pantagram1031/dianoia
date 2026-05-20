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

    def test_matrix_feature_partition_groups_near_boundary_buckets(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            classes = Path(temp_dir) / "classes.json"
            output = Path(temp_dir) / "features.json"
            classes.write_text(
                json.dumps(
                    {
                        "bucket_count": 2,
                        "buckets": [
                            {
                                "signature": (
                                    "layers=2,2,1|covers=4|mins=2|maxs=2|"
                                    "cover_matrix=[[0,2,1],[0,0,1],[0,0,0]]"
                                ),
                                "count": 1,
                                "min_lower_orientation_probability": [4, 11],
                            },
                            {
                                "signature": (
                                    "layers=2,2,1|covers=5|mins=2|maxs=1|"
                                    "cover_matrix=[[0,2,1],[0,0,2],[0,0,0]]"
                                ),
                                "count": 1,
                                "min_lower_orientation_probability": [1, 2],
                            },
                        ],
                    }
                ),
                encoding="utf-8",
            )
            with redirect_stdout(StringIO()):
                code = pb.main(
                    [
                        "matrix-feature-partition",
                        str(classes),
                        "--threshold",
                        "2/5",
                        "--processed-threshold",
                        "2/5",
                        "--output",
                        str(output),
                    ]
                )

            self.assertEqual(0, code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(1, payload["included_bucket_count"])
            self.assertEqual(1, payload["processed_bucket_count"])
            self.assertEqual(0, payload["unprocessed_bucket_count"])
            self.assertEqual(1, payload["group_count"])
            features = payload["groups"][0]["features"]
            self.assertEqual(1, features["skip_edges"])
            self.assertEqual([2, 1], features["adjacent_vector"])
            self.assertEqual([1], features["skip_vector"])
            self.assertTrue(features["has_bottom_skip"])
            self.assertTrue(payload["groups"][0]["buckets"][0]["processed"])

    def test_matrix_feature_partition_vector_key_splits_same_coarse_key(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            classes = Path(temp_dir) / "classes.json"
            output = Path(temp_dir) / "features.json"
            classes.write_text(
                json.dumps(
                    {
                        "bucket_count": 2,
                        "buckets": [
                            {
                                "signature": (
                                    "layers=2,2,1|covers=4|mins=2|maxs=1|"
                                    "cover_matrix=[[0,1,1],[0,0,2],[0,0,0]]"
                                ),
                                "count": 1,
                                "min_lower_orientation_probability": [2, 5],
                            },
                            {
                                "signature": (
                                    "layers=2,2,1|covers=4|mins=2|maxs=1|"
                                    "cover_matrix=[[0,2,1],[0,0,1],[0,0,0]]"
                                ),
                                "count": 1,
                                "min_lower_orientation_probability": [2, 5],
                            },
                        ],
                    }
                ),
                encoding="utf-8",
            )
            with redirect_stdout(StringIO()):
                code = pb.main(
                    [
                        "matrix-feature-partition",
                        str(classes),
                        "--key-detail",
                        "vector",
                        "--output",
                        str(output),
                    ]
                )

            self.assertEqual(0, code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual("vector", payload["key_detail"])
            self.assertEqual(2, payload["group_count"])
            keys = {group["feature_key"] for group in payload["groups"]}
            self.assertTrue(
                any("adjacent_vector=1,2|skip_vector=1" in key for key in keys)
            )
            self.assertTrue(
                any("adjacent_vector=2,1|skip_vector=1" in key for key in keys)
            )

    def test_matrix_vector_frontier_finds_minimal_unprocessed_classes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            partition = Path(temp_dir) / "partition.json"
            output = Path(temp_dir) / "frontier.json"
            partition.write_text(
                json.dumps(
                    {
                        "key_detail": "vector",
                        "groups": [
                            {
                                "feature_key": "p",
                                "features": {
                                    "adjacent_vector": [1, 1],
                                    "skip_vector": [0],
                                },
                                "bucket_count": 1,
                                "profile_count": 1,
                                "processed_bucket_count": 1,
                                "unprocessed_bucket_count": 0,
                                "min_lower_orientation_probability": [2, 5],
                            },
                            {
                                "feature_key": "u-frontier",
                                "features": {
                                    "adjacent_vector": [2, 1],
                                    "skip_vector": [0],
                                },
                                "bucket_count": 1,
                                "profile_count": 1,
                                "processed_bucket_count": 0,
                                "unprocessed_bucket_count": 1,
                                "min_lower_orientation_probability": [1, 2],
                            },
                            {
                                "feature_key": "u-dominated",
                                "features": {
                                    "adjacent_vector": [3, 1],
                                    "skip_vector": [0],
                                },
                                "bucket_count": 1,
                                "profile_count": 1,
                                "processed_bucket_count": 0,
                                "unprocessed_bucket_count": 1,
                                "min_lower_orientation_probability": [1, 2],
                            },
                        ],
                    }
                ),
                encoding="utf-8",
            )
            with redirect_stdout(StringIO()):
                code = pb.main(
                    [
                        "matrix-vector-frontier",
                        str(partition),
                        "--output",
                        str(output),
                    ]
                )

            self.assertEqual(0, code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(1, payload["processed_class_count"])
            self.assertEqual(2, payload["unprocessed_class_count"])
            self.assertEqual(1, payload["unprocessed_frontier_count"])
            self.assertEqual("U1", payload["unprocessed_frontier"][0]["id"])
            dominated = payload["unprocessed_classes"][1]
            self.assertFalse(dominated["is_unprocessed_frontier"])
            self.assertEqual(["U1"], dominated["dominated_by_unprocessed"])
            self.assertEqual(["P1"], payload["unprocessed_frontier"][0]["dominates_processed"])

    def test_matrix_vector_deltas_groups_classes_from_base(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            frontier = Path(temp_dir) / "frontier.json"
            output = Path(temp_dir) / "deltas.json"
            frontier.write_text(
                json.dumps(
                    {
                        "processed_classes": [
                            {
                                "id": "P1",
                                "feature_key": "p",
                                "vector": [2, 1, 0],
                                "adjacent_vector": [2, 1],
                                "skip_vector": [0],
                                "processed_bucket_count": 1,
                                "min_lower_orientation_probability": [2, 5],
                            }
                        ],
                        "unprocessed_classes": [
                            {
                                "id": "U1",
                                "feature_key": "u-base",
                                "vector": [1, 1, 0],
                                "adjacent_vector": [1, 1],
                                "skip_vector": [0],
                                "unprocessed_bucket_count": 1,
                                "min_lower_orientation_probability": [3, 7],
                            },
                            {
                                "id": "U2",
                                "feature_key": "u-next",
                                "vector": [2, 1, 1],
                                "adjacent_vector": [2, 1],
                                "skip_vector": [1],
                                "unprocessed_bucket_count": 1,
                                "min_lower_orientation_probability": [1, 2],
                            },
                        ],
                    }
                ),
                encoding="utf-8",
            )
            with redirect_stdout(StringIO()):
                code = pb.main(
                    [
                        "matrix-vector-deltas",
                        str(frontier),
                        "--base-id",
                        "U1",
                        "--output",
                        str(output),
                    ]
                )

            self.assertEqual(0, code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual("U1", payload["base_id"])
            self.assertEqual([1, 1, 0], payload["base_vector"])
            self.assertEqual(3, payload["class_count"])
            self.assertEqual(3, payload["nonnegative_from_base_count"])
            deltas = {tuple(group["delta"]): group for group in payload["delta_groups"]}
            self.assertEqual(["P1"], deltas[(1, 0, 0)]["processed_ids"])
            self.assertEqual(["U2"], deltas[(1, 0, 1)]["unprocessed_ids"])

    def test_matrix_vector_form_ledger_reconstructs_cover_matrix(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            frontier = Path(temp_dir) / "frontier.json"
            output = Path(temp_dir) / "forms.json"
            frontier.write_text(
                json.dumps(
                    {
                        "processed_classes": [],
                        "unprocessed_classes": [
                            {
                                "id": "U1",
                                "adjacent_vector": [2, 1],
                                "skip_vector": [0],
                                "unprocessed_bucket_count": 1,
                                "min_lower_orientation_probability": [1, 2],
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            with redirect_stdout(StringIO()):
                code = pb.main(
                    [
                        "matrix-vector-form-ledger",
                        str(frontier),
                        "--ids",
                        "U1",
                        "--rank-shape",
                        "2,1,1",
                        "--width",
                        "2",
                        "--height",
                        "3",
                        "--output",
                        str(output),
                    ]
                )

            self.assertEqual(0, code)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(1, payload["class_count"])
            self.assertEqual([[0, 2, 0], [0, 0, 1], [0, 0, 0]], payload["classes"][0]["cover_matrix"])
            self.assertGreaterEqual(payload["classes"][0]["form_count"], 1)
            self.assertIn("best_pair", payload["classes"][0]["forms"][0])

    def test_matrix_vector_named_cases_extracts_ledger_forms(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            ledger = Path(temp_dir) / "ledger.json"
            output_dir = Path(temp_dir) / "cases"
            summary = Path(temp_dir) / "summary.json"
            ledger.write_text(
                json.dumps(
                    {
                        "classes": [
                            {
                                "id": "P7",
                                "forms": [
                                    {
                                        "rank_normal_form": {
                                            "label_by_item": {
                                                "0": "a",
                                                "1": "b",
                                            },
                                            "cover_relations": ["a<b"],
                                            "best_pair": {
                                                "pair": ["a", "b"],
                                                "lower_orientation_probability": [1, 2],
                                            },
                                        }
                                    }
                                ],
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            with redirect_stdout(StringIO()):
                code = pb.main(
                    [
                        "matrix-vector-named-cases",
                        str(ledger),
                        "--ids",
                        "P7",
                        "--output-dir",
                        str(output_dir),
                        "--summary",
                        str(summary),
                    ]
                )

            self.assertEqual(0, code)
            payload = json.loads(summary.read_text(encoding="utf-8"))
            self.assertEqual(1, payload["case_count"])
            case_payload = json.loads((output_dir / "p7-form-1.json").read_text(encoding="utf-8"))
            self.assertEqual("P7", case_payload["source_class"])
            self.assertEqual([["a", "b"]], case_payload["check_pairs"])


if __name__ == "__main__":
    unittest.main()
