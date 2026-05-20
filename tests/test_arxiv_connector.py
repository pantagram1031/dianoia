import argparse
import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SERVER = ROOT / "connectors" / "arxiv" / "server.py"
SPEC = importlib.util.spec_from_file_location("arxiv_server", SERVER)
assert SPEC is not None and SPEC.loader is not None
arxiv = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(arxiv)


class ArxivConnectorTest(unittest.TestCase):
    def test_build_search_query_with_category_and_dates(self) -> None:
        query = arxiv.build_search_query(
            "finite induced saturated graphs",
            category="math.CO",
            from_date="2025-11-01",
            to_date="2026-05-20",
        )

        self.assertIn("all:finite", query)
        self.assertIn("all:induced", query)
        self.assertIn("all:saturated", query)
        self.assertIn("all:graphs", query)
        self.assertIn("cat:math.CO", query)
        self.assertIn("submittedDate:[202511010000 TO 202605202359]", query)

    def test_build_openness_query_adds_research_lead_terms(self) -> None:
        query = arxiv.build_search_query("chromatic threshold", openness=True)

        self.assertIn("all:chromatic", query)
        self.assertIn("all:threshold", query)
        self.assertIn('all:"open problem"', query)
        self.assertIn("all:conjecture", query)
        self.assertIn(" OR ", query)

    def test_quoted_user_phrases_are_preserved(self) -> None:
        query = arxiv.build_search_query('"locally finite perturbation" tournament')

        self.assertIn('all:"locally finite perturbation"', query)
        self.assertIn("all:tournament", query)

    def test_normalize_arxiv_id_accepts_abs_and_pdf_urls(self) -> None:
        self.assertEqual("2604.06609", arxiv.normalize_arxiv_id("https://arxiv.org/abs/2604.06609"))
        self.assertEqual("2604.06609", arxiv.normalize_arxiv_id("https://arxiv.org/pdf/2604.06609.pdf"))

    def test_openness_output_contains_meta_without_network_in_query_builder(self) -> None:
        captured = {}

        def fake_query(params):
            captured.update(params)
            return [{"arxiv_id": "2601.00001"}]

        original = arxiv.query
        arxiv.query = fake_query
        try:
            result = arxiv.openness(
                argparse.Namespace(
                    query="open induced saturation",
                    category="math.CO",
                    from_date="2026-01-01",
                    to_date="2026-05-20",
                    max_results=2,
                    sort_by="submittedDate",
                )
            )
        finally:
            arxiv.query = original

        self.assertEqual("submittedDate", captured["sortBy"])
        self.assertEqual("2", captured["max_results"])
        self.assertEqual("openness", result["query_meta"]["mode"])
        self.assertEqual([{"arxiv_id": "2601.00001"}], result["records"])
        self.assertIn("submittedDate:[202601010000 TO 202605202359]", result["query_meta"]["search_query"])


if __name__ == "__main__":
    unittest.main()
