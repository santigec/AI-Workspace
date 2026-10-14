"""Validate catalog and order input; never generates artwork or certifies QA."""
import argparse
import json
import subprocess
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]

def read_local(root, relative):
    root = Path(root).resolve()
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise ValueError(f"Path outside workspace: {relative}")
    return json.loads(path.read_text(encoding="utf-8"))

def schema_errors(data, schema, context):
    Draft202012Validator.check_schema(schema)
    errors = Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(data)
    return [f"{context}/{'/'.join(map(str, e.absolute_path))}: {e.message}" for e in errors]

def load_catalog(root=ROOT):
    root = Path(root)
    index = read_local(root, "registry/products.yaml")
    if index.get("schema_version") != 1 or not isinstance(index.get("catalogs"), list):
        raise ValueError("Invalid product registry")
    schema = read_local(root, index["catalog_schema"])
    order_schema = read_local(root, index["order_schema"])
    Draft202012Validator.check_schema(order_schema)
    workflows = read_local(root, "registry/skills.yaml")["workflows"]
    products, errors = {}, []
    for relative in index["catalogs"]:
        catalog = read_local(root, relative)
        catalog_errors = schema_errors(catalog, schema, relative)
        errors.extend(catalog_errors)
        if catalog_errors:
            continue
        for product in catalog["products"]:
            pid = product["id"]
            if pid in products:
                errors.append(f"Duplicate product id: {pid}")
            products[pid] = product
            workflow = product["workflow"]
            if workflow is not None and workflow not in workflows:
                errors.append(f"{pid}: unknown workflow {workflow}")
            area = product["production"]["print_area"]
            if area and product["width_mm"] and product["height_mm"]:
                if area["width_mm"] > product["width_mm"] or area["height_mm"] > product["height_mm"]:
                    errors.append(f"{pid}: print area exceeds canvas")
                margin = product["production"]["safe_margin_mm"]
                if margin is not None and 2 * margin >= min(area.values()):
                    errors.append(f"{pid}: safe margin leaves no printable space")
    if errors:
        raise ValueError("\n".join(errors))
    return products, workflows, order_schema

def validate_order(order, root=ROOT, workspace_head=None, tracked_changes=None):
    """Return validation only; INPUT_READY never means PRINT_READY."""
    products, workflows, schema = load_catalog(root)
    errors = schema_errors(order, schema, "order")
    if errors:
        return {"status": "INVALID", "production_ready": False, "errors": errors, "warnings": []}
    pid = order["product"]["id"]
    if pid not in products:
        errors.append(f"Unknown product: {pid}")
    workflow = order["workflow"]
    if workflow not in workflows:
        errors.append(f"Unknown workflow: {workflow}")
    product = products.get(pid)
    if product and workflow != product["workflow"]:
        errors.append("Workflow does not match selected product")
    keys = [constraint["key"] for constraint in order["constraints"]]
    if len(keys) != len(set(keys)):
        errors.append("Duplicate constraint keys")
    hard = {c["key"]: c["value"] for c in order["constraints"] if c["priority"] == "hard"}
    recognized = {
        "format": order["output"]["format"],
        "background": order["output"]["background"],
        "resolution_ppi": order["output"]["resolution_ppi"],
        "main_name": order["content"]["main_name"],
    }
    for key, observed in recognized.items():
        if key in hard and hard[key] != observed:
            errors.append(f"Hard constraint {key} contradicts order field")
    if hard.get("preserve_original_art") is True and order["artwork"]["operation"] != "edit":
        errors.append("Preserving original art requires edit and source artwork")
    if "background" in order["resilience"]["adaptable_elements"] and (
        "background" in hard or order["output"]["background"] == "transparent"
    ):
        errors.append("Required background cannot also be adaptable")
    if order["output"]["background"] == "transparent" and order["output"]["format"] == "pdf":
        errors.append("Transparent delivery must use PNG or SVG in this workflow")
    if errors:
        return {"status": "INVALID", "production_ready": False, "errors": errors, "warnings": []}

    production = order["mode"] == "production"
    blockers, warnings = [], []
    if product["verification"]["status"] != "verified":
        blockers.append("Product specifications are unverified")
    if order["requested_dimensions"]:
        dims = order["requested_dimensions"]
        same = (dims["width_mm"], dims["height_mm"]) == (product["width_mm"], product["height_mm"])
        if not same:
            blockers.append("Requested dimensions differ from catalog; confirm a matching product specification")
    else:
        dims = {"width_mm": product["width_mm"], "height_mm": product["height_mm"]}
    if not dims["width_mm"] or not dims["height_mm"]:
        blockers.append("No dimensions available for a sized draft")

    if product["verification"]["status"] == "verified":
        spec = product["production"]
        for field in ("format", "background", "resolution_ppi"):
            requested = order["output"][field]
            # Higher resolution is acceptable; format and background must match.
            mismatch = requested != spec[field]
            if field == "resolution_ppi" and requested is not None:
                mismatch = requested < spec[field]
            if mismatch:
                blockers.append(f"Output {field} does not meet verified product specification")

    if production:
        if workspace_head is None:
            try:
                workspace_head = subprocess.check_output(
                    ["git", "-C", str(root), "rev-parse", "HEAD"], text=True
                ).strip()
            except (subprocess.CalledProcessError, OSError):
                blockers.append("Cannot verify workspace commit")
        if order["workspace_ref"] != workspace_head:
            blockers.append("workspace_ref differs from workspace HEAD")
        if tracked_changes is None:
            try:
                tracked_changes = bool(subprocess.check_output(
                    ["git", "-C", str(root), "status", "--porcelain", "--untracked-files=no"], text=True
                ).strip())
            except (subprocess.CalledProcessError, OSError):
                tracked_changes = True
        if tracked_changes:
            blockers.append("Workspace has uncommitted tracked changes")
        status = "BLOCKED_PRODUCTION" if blockers else "INPUT_READY"
        errors = blockers
    elif blockers and not order["resilience"]["allow_draft_on_missing_specs"]:
        status, errors = "INVALID", blockers
    elif not dims["width_mm"] or not dims["height_mm"]:
        status, errors = "INVALID", blockers
    else:
        status, errors, warnings = "DRAFT_ALLOWED", [], blockers
    if status == "INPUT_READY":
        warnings.append("Input validation only: artwork, hard constraints and print QA still require execution.")
    return {
        "status": status, "production_ready": False,
        "product_id": pid, "workflow": workflow,
        "effective_dimensions": dims,
        "dimension_source": "order" if order["requested_dimensions"] else "catalog",
        "errors": errors, "warnings": warnings,
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("order", nargs="?", type=Path)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        if args.order is None:
            products, _, _ = load_catalog(args.root)
            print(f"PASS: {len(products)} product records validated; verification status is unchanged.")
            return 0
        order = json.loads(args.order.read_text(encoding="utf-8"))
        result = validate_order(order, args.root)
    except (ValueError, OSError, KeyError) as exc:
        print(f"INVALID: {exc}")
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] in {"DRAFT_ALLOWED", "INPUT_READY"} else 1

if __name__ == "__main__":
    raise SystemExit(main())
