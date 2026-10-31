"""Structural checks for the A3 drawstring backpack skill; not print approval."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DrawstringBackpackSublimationTests(unittest.TestCase):
    def test_skill_and_workflow_are_registered(self):
        registry = json.loads((ROOT / "registry/skills.yaml").read_text(encoding="utf-8"))
        skill = registry["skills"]["drawstring-backpack-sublimation"]
        workflow = registry["workflows"]["drawstring-backpack-sublimation"]
        self.assertEqual("0.1.0", skill["version"])
        self.assertIn("drawstring-backpack-sublimation", workflow["steps"])

    def test_a3_and_layout_contract_are_consistent(self):
        paths = (
            "tribe/skills/drawstring-backpack-sublimation/SKILL.md",
            "workflows/tribe/drawstring-backpack-sublimation.md",
            ".agents/skills/drawstring-backpack-sublimation/SKILL.md",
        )
        for name in paths:
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn("A3", text)
            self.assertIn("297 × 420 mm", text)
        skill = (ROOT / paths[0]).read_text(encoding="utf-8")
        for value in ("25%", "0–105 mm", "350–420 mm", "3508 × 4961 px"):
            self.assertIn(value, skill)

    def test_product_catalog_records_unverified_geometry(self):
        product = json.loads((ROOT / "tribe/knowledge/product-catalog/drawstring-backpacks.yaml").read_text(encoding="utf-8"))["products"][0]
        self.assertEqual("drawstring_backpack_a3", product["id"])
        self.assertEqual((297, 420), (product["width_mm"], product["height_mm"]))
        self.assertEqual("unverified", product["verification"]["status"])
        self.assertTrue(product["production"]["excluded_zones"])


if __name__ == "__main__":
    unittest.main()
