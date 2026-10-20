"""Structural contract tests for the adhesivo-tarrito skill."""
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate_order", ROOT / "scripts/validate_order.py")
orders = importlib.util.module_from_spec(spec)
spec.loader.exec_module(orders)


class AdhesivoTarritoTests(unittest.TestCase):
    def test_skill_and_wrapper_are_discoverable(self):
        domain = (ROOT / "tribe/skills/adhesivo-tarrito/SKILL.md").read_text(encoding="utf-8")
        wrapper = (ROOT / ".agents/skills/adhesivo-tarrito/SKILL.md").read_text(encoding="utf-8")
        registry = json.loads((ROOT / "registry/skills.yaml").read_text(encoding="utf-8"))
        frontmatter = domain.split("---", 2)[1].strip().splitlines()
        self.assertEqual(2, len(frontmatter))
        self.assertEqual("name: adhesivo-tarrito", frontmatter[0])
        self.assertIn("adhesivo tarrito", frontmatter[1])
        self.assertNotIn("license:", domain)
        self.assertNotIn("metadata:", domain)
        self.assertIn("tribe/skills/adhesivo-tarrito/SKILL.md", wrapper)
        self.assertEqual("0.1.0", registry["skills"]["adhesivo-tarrito"]["version"])

    def test_geometry_contract_is_explicit(self):
        rules = (ROOT / "tribe/standards/adhesivo-tarrito-rules.md").read_text(encoding="utf-8")
        for center in ("22.5", "67.5", "112.5", "157.5"):
            self.assertIn(center, rules)
        for seam in ("45", "90", "135"):
            self.assertIn(seam, rules)
        self.assertIn("180 x 80 mm", rules)

    def test_catalog_order_resolves_to_180_by_80_draft(self):
        example = json.loads((ROOT / "tribe/templates/orders/adhesivo-tarrito.example.json").read_text(encoding="utf-8"))
        result = orders.validate_order(example)
        self.assertEqual("DRAFT_ALLOWED", result["status"])
        self.assertFalse(result["production_ready"])
        self.assertEqual({"width_mm": 180, "height_mm": 80}, result["effective_dimensions"])

    def test_unconfirmed_production_parameters_remain_null(self):
        catalog = json.loads((ROOT / "tribe/knowledge/product-catalog/jars.yaml").read_text(encoding="utf-8"))
        product = catalog["products"][0]
        self.assertEqual("unverified", product["verification"]["status"])
        for field in ("print_area", "safe_margin_mm", "bleed_mm", "resolution_ppi", "mirror"):
            self.assertIsNone(product["production"][field])


if __name__ == "__main__":
    unittest.main()
