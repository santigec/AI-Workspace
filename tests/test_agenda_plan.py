"""Test agenda format and exact calendars; no visual generation implied."""
import importlib.util
import json
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("build_agenda_plan", ROOT / "scripts/build_agenda_plan.py")
agenda = importlib.util.module_from_spec(spec)
spec.loader.exec_module(agenda)

class AgendaPlanTests(unittest.TestCase):
    def setUp(self):
        self.order = json.loads((ROOT / "tribe/templates/orders/agenda-a4.example.json").read_text(encoding="utf-8"))

    def test_nine_a4_models_and_two_distinct_labels(self):
        plan = agenda.build_plan(self.order)
        pieces = plan["artifacts"]
        self.assertEqual(11, len(pieces))
        self.assertEqual(9, sum(p["dimensions_mm"] == {"width_mm": 210, "height_mm": 297} for p in pieces))
        dimensions = {p["id"]: p["dimensions_mm"] for p in pieces}
        self.assertEqual({"width_mm": 205, "height_mm": 165}, dimensions["agenda_label"])
        self.assertEqual({"width_mm": 205, "height_mm": 95}, dimensions["packaging_label"])
        self.assertTrue(all(p["render_status"] == "NOT_GENERATED" for p in pieces))
        self.assertFalse(plan["production_ready"])

    def test_actual_calendar_dates_align_with_weekday_columns(self):
        for year in (2026, 2027, 2028, 2100):
            for first in ("monday", "sunday"):
                data = agenda.calendar_data(year, first)
                seen = []
                for month in data["months"]:
                    for week in month["weeks"]:
                        self.assertEqual(7, len(week))
                        for column, value in enumerate(week):
                            if value is not None:
                                d = date.fromisoformat(value)
                                self.assertEqual(month["month"], d.month)
                                self.assertEqual((column + (0 if first == "monday" else 6)) % 7, d.weekday())
                                seen.append(value)
                expected_days = (date(year + 1, 1, 1) - date(year, 1, 1)).days
                self.assertEqual(expected_days, len(seen))
                self.assertEqual(expected_days, len(set(seen)))

    def test_leap_century_rule(self):
        self.assertEqual(29, agenda.calendar_data(2028)["months"][1]["days_in_month"])
        self.assertEqual(28, agenda.calendar_data(2100)["months"][1]["days_in_month"])

    def test_chosen_years_are_not_hardcoded(self):
        self.order["calendar_years"] = [2028, 2029]
        self.assertEqual([2028, 2029], [c["year"] for c in agenda.build_plan(self.order)["calendars"]])

    def test_interiors_are_white_with_thematic_watermark(self):
        pieces = agenda.build_plan(self.order)["artifacts"]
        for piece in pieces:
            if piece["low_ink"]:
                self.assertEqual("white", piece["background"])
                self.assertFalse(piece["full_color_background"])
        grid = next(p for p in pieces if p["id"] == "grid_page")
        self.assertTrue(grid["central_thematic_watermark"])
        self.assertTrue(grid["themed_header_footer"])

    def test_color_backgrounds_are_not_accepted_for_interiors(self):
        self.order["interiors"]["background"] = "pink"
        with self.assertRaises(ValueError):
            agenda.build_plan(self.order)

    def test_inside_cover_reverses_use_white_base(self):
        pieces = agenda.build_plan(self.order)["artifacts"]
        for name in ("inside_front_cover", "inside_back_cover"):
            piece = next(p for p in pieces if p["id"] == name)
            self.assertEqual("white", piece["background"])
            self.assertTrue(piece["low_ink"])

    def test_nonconsecutive_years_are_rejected(self):
        self.order["calendar_years"] = [2026, 2028]
        with self.assertRaises(ValueError):
            agenda.build_plan(self.order)

    def test_absent_personalization_does_not_invent_name(self):
        self.assertIsNone(agenda.build_plan(self.order)["personalization"]["name"])

if __name__ == "__main__":
    unittest.main()
