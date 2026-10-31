"""Structural checks for the A3 coloring backpack skill; not print approval."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class BolsitosColorearA3Tests(unittest.TestCase):
    def test_skill_and_workflow_are_registered(self):
        registry = json.loads((ROOT / "registry/skills.yaml").read_text(encoding="utf-8"))
        skill = registry["skills"]["bolsitos-colorear-a3"]
        workflow = registry["workflows"]["bolsitos-colorear-a3"]
        self.assertEqual("0.1.0", skill["version"])
        self.assertIn("bolsitos-colorear-a3", workflow["steps"])

    def test_a3_coloring_contract_is_consistent(self):
        paths = (
            "tribe/skills/bolsitos-colorear-a3/SKILL.md",
            "workflows/tribe/bolsitos-colorear-a3.md",
            ".agents/skills/bolsitos-colorear-a3/SKILL.md",
        )
        for name in paths:
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn("297 × 420 mm", text)
            self.assertIn("0–105 mm", text)
        skill = (ROOT / paths[0]).read_text(encoding="utf-8")
        for value in ("25%", "350–420 mm", "3508 × 4961 px", "line art negro puro", "fondo blanco opaco"):
            self.assertIn(value, skill)

    def test_product_catalog_records_coloring_variant(self):
        products = json.loads((ROOT / "tribe/knowledge/product-catalog/drawstring-backpacks.yaml").read_text(encoding="utf-8"))["products"]
        product = next(item for item in products if item["id"] == "drawstring_backpack_coloring_a3")
        self.assertEqual((297, 420), (product["width_mm"], product["height_mm"]))
        self.assertEqual("unverified", product["verification"]["status"])
        self.assertIn("line_art", product["style_defaults"])


if __name__ == "__main__":
    unittest.main()
