"""Validate AI-Workspace structure; does not execute model evaluations."""
import argparse
import json
import re
from pathlib import Path

DOMAINS = {"shared", "tribe", "image-studio", "software-office"}
STATES = {"experimental", "alpha", "beta", "stable", "deprecated"}

def validate(root):
    root = Path(root).resolve()
    errors = []

    def fail(message):
        errors.append(message)

    def local_path(value, context):
        if not isinstance(value, str) or not value:
            fail(f"{context}: missing path")
            return None
        target = (root / value).resolve()
        if not target.is_relative_to(root):
            fail(f"{context}: path outside repository")
            return None
        if not target.is_file():
            fail(f"{context}: missing file {value}")
            return None
        return target

    def load_json(relative):
        target = local_path(relative, relative)
        if target is None:
            return None
        try:
            return json.loads(target.read_text(encoding="utf-8"))
        except (ValueError, OSError) as exc:
            fail(f"{relative}: invalid JSON-compatible data: {exc}")
            return None

    registry = load_json("registry/skills.yaml")
    manifest = load_json("evals/cases.json")
    if not isinstance(registry, dict) or not isinstance(manifest, dict):
        if not errors:
            fail("Registry and case manifest must be objects")
        return errors
    if registry.get("schema_version") != 1 or manifest.get("schema_version") != 1:
        fail("Unsupported schema_version")
    skills = registry.get("skills")
    workflows = registry.get("workflows")
    cases = manifest.get("cases")
    if not isinstance(skills, dict) or not isinstance(workflows, dict) or not isinstance(cases, list):
        fail("Invalid skills, workflows or cases collection")
        return errors

    indexed_cases = {}
    for case in cases:
        if not isinstance(case, dict) or not isinstance(case.get("id"), str):
            fail("Case requires a string id")
            continue
        cid = case["id"]
        if cid in indexed_cases:
            fail(f"Duplicate case {cid}")
        indexed_cases[cid] = case
        if case.get("skill") not in skills:
            fail(f"{cid}: unknown skill")
        local_path(case.get("path"), cid)
        if case.get("status") not in {"NOT_RUN", "PASS", "FAIL"}:
            fail(f"{cid}: invalid evaluation status")
        if case.get("status") in {"PASS", "FAIL"}:
            report = local_path(case.get("result_path"), f"{cid} result")
            if report and not report.read_text(encoding="utf-8").strip():
                fail(f"{cid}: empty evidence report")

    paths = set()
    for name, skill in skills.items():
        if not isinstance(skill, dict):
            fail(f"{name}: skill must be an object")
            continue
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            fail(f"{name}: invalid skill name")
        domain = skill.get("domain")
        if domain not in DOMAINS or skill.get("owner") not in DOMAINS:
            fail(f"{name}: invalid domain or owner")
        expected = f"{domain}/skills/{name}/SKILL.md"
        if skill.get("path") != expected:
            fail(f"{name}: path must be {expected}")
        path = local_path(skill.get("path"), name)
        paths.add(skill.get("path"))
        if not re.fullmatch(r"\d+\.\d+\.\d+", str(skill.get("version", ""))):
            fail(f"{name}: invalid version")
        if skill.get("status") not in STATES:
            fail(f"{name}: invalid lifecycle status")
        for field in ("requires_before", "recommends_next", "evaluation_cases"):
            if not isinstance(skill.get(field), list):
                fail(f"{name}: {field} must be a list")
        for dependency in skill.get("requires_before", []) + skill.get("recommends_next", []):
            if dependency not in skills:
                fail(f"{name}: unknown dependency {dependency}")
            if dependency == name:
                fail(f"{name}: self dependency")
        for cid in skill.get("evaluation_cases", []):
            if cid not in indexed_cases or indexed_cases[cid].get("skill") != name:
                fail(f"{name}: invalid case reference {cid}")
        if skill.get("status") in {"beta", "stable"}:
            cids = skill.get("evaluation_cases", [])
            behavioral = [cid for cid in cids if indexed_cases.get(cid, {}).get("scope", "behavioral") == "behavioral"]
            if not behavioral or any(indexed_cases.get(cid, {}).get("status") != "PASS" for cid in cids):
                fail(f"{name}: promotion requires passing evaluation evidence")
        if path:
            text = path.read_text(encoding="utf-8")
            front = re.match(r"^---\n(.*?)\n---(?:\n|$)", text, re.S)
            if not front:
                fail(f"{name}: missing frontmatter")
            else:
                # Current repository convention uses only two plain scalar fields.
                fields = {}
                for line in front.group(1).splitlines():
                    match = re.fullmatch(r"(name|description): (.+)", line)
                    if not match:
                        fail(f"{name}: unsupported frontmatter line {line!r}")
                    else:
                        if match[1] in fields:
                            fail(f"{name}: duplicate frontmatter field")
                        fields[match[1]] = match[2]
                if fields.get("name") != name:
                    fail(f"{name}: frontmatter name differs")
                desc = fields.get("description", "")
                if not desc or len(desc) > 1024 or any(c in desc for c in "<>") or ": " in desc:
                    fail(f"{name}: invalid plain scalar description")
            if "[TODO:" in text:
                fail(f"{name}: unfinished scaffold")
            for target in re.findall(r"\]\(([^)]+)\)", text):
                if "://" in target or target.startswith("#"):
                    continue
                linked = (path.parent / target.split("#")[0]).resolve()
                if not linked.is_relative_to(root) or not linked.is_file():
                    fail(f"{name}: broken reference {target}")

    actual = {p.relative_to(root).as_posix() for domain in DOMAINS
              for p in (root / domain / "skills").glob("*/SKILL.md")}
    for orphan in actual - paths:
        fail(f"Unregistered skill {orphan}")

    visiting, visited = set(), set()
    def visit(name):
        if name in visiting:
            fail(f"Cycle in requires_before at {name}")
            return
        if name in visited or name not in skills:
            return
        visiting.add(name)
        for dependency in skills[name].get("requires_before", []):
            visit(dependency)
        visiting.remove(name)
        visited.add(name)
    for name in skills:
        visit(name)

    for name, workflow in workflows.items():
        if not isinstance(workflow, dict):
            fail(f"{name}: workflow must be an object")
            continue
        path = local_path(workflow.get("path"), f"workflow {name}")
        steps = workflow.get("steps", [])
        conditional = workflow.get("conditional_steps", [])
        if workflow.get("status") not in STATES or not isinstance(steps, list) or not steps:
            fail(f"{name}: invalid workflow")
            continue
        if not isinstance(conditional, list) or any(step not in steps for step in conditional):
            fail(f"{name}: invalid conditional steps")
        if path:
            body = path.read_text(encoding="utf-8")
            for step in steps:
                if step not in skills:
                    fail(f"{name}: unknown workflow skill {step}")
                elif step not in body:
                    fail(f"{name}: undocumented workflow step {step}")
    for cid, case in indexed_cases.items():
        skill = skills.get(case.get("skill"), {})
        if cid not in skill.get("evaluation_cases", []):
            fail(f"{cid}: missing backlink in registry")
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    for error in errors:
        print(f"FAIL: {error}")
    if not errors:
        print("PASS: registry, skill structure, case references and workflows validated.")
        print("Behavioral evaluations are separate; NOT_RUN cases remain unexecuted.")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
