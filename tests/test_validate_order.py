"""Verify draft/production boundaries using synthetic catalog fixtures."""
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate_order", ROOT / "scripts/validate_order.py")
orders = importlib.util.module_from_spec(spec)
spec.loader.exec_module(orders)

class OrderValidationTests(unittest.TestCase):
    def setUp(self):
        self.order = json.loads((ROOT / "tribe/templates/orders/mug-draft.example.json").read_text(encoding="utf-8"))

    def test_example_allows_draft_without_approving_print(self):
        result = orders.validate_order(self.order)
        self.assertEqual("DRAFT_ALLOWED", result["status"])
        self.assertFalse(result["production_ready"])
        self.assertTrue(result["warnings"])

    def test_unverified_product_blocks_production(self):
        self.order.update(mode="production", workspace_ref="a" * 40)
        result = orders.validate_order(self.order, workspace_head="a" * 40, tracked_changes=False)
        self.assertEqual("BLOCKED_PRODUCTION", result["status"])

    def test_unknown_product_is_invalid(self):
        self.order["product"]["id"] = "imaginary_product"
        self.assertEqual("INVALID", orders.validate_order(self.order)["status"])

    def test_product_workflow_mismatch_is_invalid(self):
        self.order["workflow"] = "tumbler-sublimation"
        self.assertEqual("INVALID", orders.validate_order(self.order)["status"])

    def test_hard_background_cannot_be_adaptable(self):
        self.order["resilience"]["adaptable_elements"].append("background")
        self.assertEqual("INVALID", orders.validate_order(self.order)["status"])

    def test_false_hard_format_is_rejected(self):
        self.order["constraints"].append({"key": "format", "value": "svg", "priority": "hard"})
        self.assertEqual("INVALID", orders.validate_order(self.order)["status"])

    def test_edit_without_original_is_invalid(self):
        self.order["artwork"]["operation"] = "edit"
        self.assertEqual("INVALID", orders.validate_order(self.order)["status"])

    def test_invalid_resolution_is_rejected(self):
        self.order["output"]["resolution_ppi"] = -300
        self.assertEqual("INVALID", orders.validate_order(self.order)["status"])

    def test_tumbler_capacities_have_distinct_heights(self):
        for capacity, height in (("500ml", 125), ("600ml", 142), ("750ml", 182)):
            with self.subTest(capacity=capacity):
                self.order["workflow"] = "tumbler-sublimation"
                self.order["product"]["id"] = "tumbler_" + capacity
                self.order["requested_dimensions"] = None
                result = orders.validate_order(self.order)
                self.assertEqual("DRAFT_ALLOWED", result["status"])
                self.assertEqual({"width_mm": 232, "height_mm": height}, result["effective_dimensions"])

    def test_tumbler_600ml_background_does_not_change_size(self):
        example = json.loads((ROOT / "tribe/templates/orders/tumbler-600ml.example.json").read_text(encoding="utf-8"))
        for background in ("transparent", "solid", "themed"):
            with self.subTest(background=background):
                example["output"]["background"] = background
                for constraint in example["constraints"]:
                    if constraint["key"] == "background":
                        constraint["value"] = background
                result = orders.validate_order(example)
                self.assertEqual("DRAFT_ALLOWED", result["status"])
                self.assertEqual({"width_mm": 232, "height_mm": 142}, result["effective_dimensions"])

    def test_tumbler_750ml_background_does_not_change_size(self):
        example = json.loads((ROOT / "tribe/templates/orders/tumbler-750ml.example.json").read_text(encoding="utf-8"))
        for background in ("transparent", "solid", "themed"):
            with self.subTest(background=background):
                example["output"]["background"] = background
                for constraint in example["constraints"]:
                    if constraint["key"] == "background":
                        constraint["value"] = background
                result = orders.validate_order(example)
                self.assertEqual("DRAFT_ALLOWED", result["status"])
                self.assertEqual({"width_mm": 232, "height_mm": 182}, result["effective_dimensions"])

    def test_tumbler_500ml_uses_its_dimensions_not_mug_dimensions(self):
        self.order["workflow"] = "tumbler-sublimation"
        self.order["product"]["id"] = "tumbler_500ml"
        self.order["requested_dimensions"] = None
        result = orders.validate_order(self.order)
        self.assertEqual("DRAFT_ALLOWED", result["status"])
        self.assertEqual({"width_mm": 232, "height_mm": 125}, result["effective_dimensions"])
        self.assertFalse(result["production_ready"])

    def test_tumbler_500ml_background_changes_preserve_dimensions(self):
        example = json.loads((ROOT / "tribe/templates/orders/tumbler-500ml.example.json").read_text(encoding="utf-8"))
        for background in ("transparent", "solid", "themed"):
            with self.subTest(background=background):
                example["output"]["background"] = background
                for constraint in example["constraints"]:
                    if constraint["key"] == "background":
                        constraint["value"] = background
                result = orders.validate_order(example)
                self.assertEqual("DRAFT_ALLOWED", result["status"])
                self.assertEqual({"width_mm": 232, "height_mm": 125}, result["effective_dimensions"])

    def test_themed_background_with_description_is_allowed(self):
        self.order["output"].update(background="themed", background_description="Selva infantil con cielo azul")
        self.order["artwork"]["reference_images"] = [{"source": "chat:reference-1", "role": "background"}]
        result = orders.validate_order(self.order)
        self.assertEqual("DRAFT_ALLOWED", result["status"])
        self.assertEqual({"width_mm": 205, "height_mm": 95}, result["effective_dimensions"])

    def test_themed_background_without_description_is_invalid(self):
        self.order["output"]["background"] = "themed"
        self.assertEqual("INVALID", orders.validate_order(self.order)["status"])

    def test_themed_background_does_not_override_transparency_constraint(self):
        self.order["output"].update(background="themed", background_description="Selva")
        self.order["constraints"].append({"key": "background", "value": "transparent", "priority": "hard"})
        self.assertEqual("INVALID", orders.validate_order(self.order)["status"])

    def test_unknown_reference_role_is_invalid(self):
        self.order["artwork"]["reference_images"] = [{"source": "chat:reference-1", "role": "unknown"}]
        self.assertEqual("INVALID", orders.validate_order(self.order)["status"])

    def test_marking_catalog_verified_without_spec_is_rejected(self):
        with tempfile.TemporaryDirectory(prefix="tribe-validation-", dir=ROOT.parent) as temp:
            self.assertEqual(Path(temp).resolve().parent, ROOT.parent.resolve())
            root = Path(temp) / "repo"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "__pycache__", "design-runs", ".venv", "outputs"))
            catalog = root / "tribe/knowledge/product-catalog/mugs.yaml"
            data = json.loads(catalog.read_text(encoding="utf-8"))
            data["products"][0]["verification"]["status"] = "verified"
            catalog.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaises(ValueError):
                orders.load_catalog(root)

    def test_verified_input_is_not_print_approval(self):
        with tempfile.TemporaryDirectory(prefix="tribe-validation-", dir=ROOT.parent) as temp:
            self.assertEqual(Path(temp).resolve().parent, ROOT.parent.resolve())
            root = Path(temp) / "repo"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "__pycache__", "design-runs", ".venv", "outputs"))
            catalog = root / "tribe/knowledge/product-catalog/mugs.yaml"
            data = json.loads(catalog.read_text(encoding="utf-8"))
            product = data["products"][0]
            product.update(supplier="Synthetic supplier", model="Synthetic model")
            product["verification"] = {"status": "verified", "source": "Synthetic fixture only", "verified_by": "test", "verified_at": "2026-10-14"}
            product["production"].update(print_area={"width_mm": 205, "height_mm": 95},
                safe_margin_mm=2, bleed_mm=0, resolution_ppi=300, color_profile="Synthetic profile",
                format="png", background="transparent", mirror="delegated_to_rip")
            catalog.write_text(json.dumps(data), encoding="utf-8")
            self.order.update(mode="production", workspace_ref="a" * 40)
            result = orders.validate_order(self.order, root, workspace_head="a" * 40, tracked_changes=False)
            self.assertEqual("INPUT_READY", result["status"])
            self.assertFalse(result["production_ready"])
            self.order["requested_dimensions"]["width_mm"] = 300
            self.assertEqual("BLOCKED_PRODUCTION",
                orders.validate_order(self.order, root, workspace_head="a" * 40, tracked_changes=False)["status"])

if __name__ == "__main__":
    unittest.main()
