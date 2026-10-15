"""Validate an agenda order and plan pieces with exact calendar data; no image rendering."""
import argparse
import calendar
import copy
import json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
MONTHS = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
          "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
DAYS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

def calendar_data(year, week_starts_on="monday"):
    if not 1900 <= year <= 9998:
        raise ValueError("Calendar year outside supported range")
    if week_starts_on not in {"monday", "sunday"}:
        raise ValueError("Unknown week start")
    first = 0 if week_starts_on == "monday" else 6
    cal = calendar.Calendar(firstweekday=first)
    months = []
    for month in range(1, 13):
        weeks = [[date.isoformat() if date.month == month else None for date in week]
                 for week in cal.monthdatescalendar(year, month)]
        months.append({"month": month, "name": MONTHS[month - 1],
                       "days_in_month": calendar.monthrange(year, month)[1], "weeks": weeks})
    return {"year": year, "leap_year": calendar.isleap(year),
            "week_starts_on": week_starts_on, "day_labels": DAYS[first:] + DAYS[:first],
            "months": months, "holidays": []}

def build_plan(order, root=ROOT):
    root = Path(root)
    schema = json.loads((root / "tribe/schemas/agenda-order.schema.json").read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    errors = [f"{'/'.join(map(str, e.absolute_path))}: {e.message}"
              for e in Draft202012Validator(schema).iter_errors(order)]
    if errors:
        raise ValueError("\n".join(errors))
    years = order["calendar_years"]
    if years[1] != years[0] + 1:
        raise ValueError("Calendar years must be consecutive and ascending")
    specs = json.loads((root / "tribe/knowledge/agenda-specs.json").read_text(encoding="utf-8"))
    plan = []
    for component in specs["components"]:
        piece = copy.deepcopy(component)
        dimensions = copy.deepcopy(specs["profiles"][piece["profile"]])
        piece["dimensions_mm"] = dimensions
        if piece["id"] in {"calendar_current", "calendar_next"}:
            year = years[0 if piece["id"] == "calendar_current" else 1]
            piece["id"] = f"calendar_{year}"
            piece["label"] = f"Calendario {year}"
            piece["calendar_year"] = year
        piece["render_status"] = "NOT_GENERATED"
        piece["background"] = "white" if piece["low_ink"] else "theme_as_requested"
        if piece["low_ink"]:
            piece["themed_header_footer"] = order["interiors"]["themed_header_footer"]
            piece["full_color_background"] = False
        if piece["id"] == "grid_page":
            piece["watermark_opacity"] = order["interiors"]["watermark_opacity"]
            piece["grid_mm"] = order["interiors"]["grid_mm"]
        if piece["id"] == "important_activities":
            piece["line_spacing_mm"] = order["interiors"]["line_spacing_mm"]
        ppi = order["print"]["resolution_ppi"]
        piece["target_pixels"] = (
            {"width": round(dimensions["width_mm"] / 25.4 * ppi),
             "height": round(dimensions["height_mm"] / 25.4 * ppi)} if ppi else None)
        piece["suggested_files"] = [f"{piece['id']}.{ext}" for ext in order["print"]["requested_formats"]]
        plan.append(piece)
    return {
        "order_id": order["order_id"], "workflow": "agenda-design",
        "status": "PLAN_ONLY", "production_ready": False,
        "theme": copy.deepcopy(order["theme"]),
        "personalization": copy.deepcopy(order["personalization"]),
        "calendar_years": years, "artifacts": plan,
        "calendars": [calendar_data(year, order["week_starts_on"]) for year in years],
        "warnings": ["No images, PDFs or print files generated.",
                     "Binding margins, bleed and final visual/print QA require actual artifacts and job specifications."]
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("order", type=Path)
    parser.add_argument("--out", type=Path, help="Write JSON plan; never artwork")
    args = parser.parse_args()
    try:
        plan = build_plan(json.loads(args.order.read_text(encoding="utf-8")))
    except (OSError, ValueError, KeyError) as exc:
        print(f"INVALID: {exc}")
        return 1
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"PLAN_ONLY: {len(plan['artifacts'])} pieces, calendar years {plan['calendar_years']}; no artwork generated.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
