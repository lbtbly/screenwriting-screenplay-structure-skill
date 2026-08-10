#!/usr/bin/env python3
"""Validate this marketplace and its plugins.

Runs the checks the official `claude plugin validate` makes, plus the ones it
does not: version drift between plugin.json and the marketplace entry, broken
relative paths cited inside skill reference files, and missing SKILL.md.

    python3 scripts/validate.py [--strict]

--strict treats warnings as errors. Exit code 1 on any error.
"""
from __future__ import annotations
import json, re, sys, os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STRICT = "--strict" in sys.argv
errors: list[str] = []
warnings: list[str] = []

def err(m): errors.append(m)
def warn(m): warnings.append(m)

KEBAB = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*$")

# ---------------------------------------------------------------- marketplace
mpath = ROOT / ".claude-plugin" / "marketplace.json"
if not mpath.exists():
    err(f"missing {mpath.relative_to(ROOT)}")
    print("FAIL"); sys.exit(1)
try:
    mkt = json.loads(mpath.read_text())
except json.JSONDecodeError as e:
    err(f"marketplace.json is not valid JSON: {e}")
    print("FAIL"); sys.exit(1)

for field in ("name", "owner", "plugins"):
    if field not in mkt:
        err(f"marketplace.json missing required field {field!r}")

name = mkt.get("name", "")
if name and not KEBAB.fullmatch(name):
    err(f"marketplace name {name!r} is not kebab-case")
if name in {"org", "org-provisioned", "unknown"}:
    err(f"marketplace name {name!r} is reserved")

owner = mkt.get("owner")
if isinstance(owner, dict):
    if not owner.get("name"):
        err("marketplace owner.name is required")
elif owner is not None:
    err("marketplace owner must be an object with a name")

if not mkt.get("description"):
    warn("marketplace has no description")

plugins = mkt.get("plugins") or []
if not plugins:
    warn("marketplace defines no plugins")

seen: set[str] = set()

# -------------------------------------------------------------------- plugins
for i, entry in enumerate(plugins):
    tag = f"plugins[{i}]"
    pname = entry.get("name")
    if not pname:
        err(f"{tag} missing required field 'name'"); continue
    tag = f"plugins[{i}] ({pname})"
    if pname in seen:
        err(f"{tag} duplicate plugin name")
    seen.add(pname)
    if not KEBAB.fullmatch(pname):
        err(f"{tag} name is not kebab-case")

    if "version" in entry:
        warn(f"{tag} declares a version in the marketplace entry; plugin.json always "
             f"wins, so this can mask a real update. Remove it.")

    src = entry.get("source")
    if src is None:
        err(f"{tag} missing required field 'source'"); continue

    if isinstance(src, str):
        if ".." in Path(src).parts:
            err(f"{tag} source path contains '..'"); continue
        if not src.startswith("./"):
            warn(f"{tag} relative source should start with './' (got {src!r})")
        pdir = (ROOT / src).resolve()
        try:
            pdir.relative_to(ROOT)
        except ValueError:
            err(f"{tag} source resolves outside the repository"); continue
        if not pdir.is_dir():
            err(f"{tag} source directory does not exist: {src}"); continue
    elif isinstance(src, dict):
        kind = src.get("source")
        need = {"github": ["repo"], "url": ["url"], "git-subdir": ["url", "path"],
                "npm": ["package"], "archive": ["url"]}
        if kind not in need:
            err(f"{tag} unknown source type {kind!r}")
        else:
            for k in need[kind]:
                if not src.get(k):
                    err(f"{tag} source type {kind!r} requires {k!r}")
        continue  # remote sources cannot be checked locally
    else:
        err(f"{tag} source must be a string or object"); continue

    # ---- plugin.json (required when strict, which is the default)
    strict_entry = entry.get("strict", True)
    manifest = pdir / ".claude-plugin" / "plugin.json"
    if strict_entry and not manifest.exists():
        err(f"{tag} strict plugin has no .claude-plugin/plugin.json")
    elif not strict_entry and manifest.exists():
        err(f"{tag} strict:false but plugin.json exists — this is a load conflict")

    if manifest.exists():
        try:
            pj = json.loads(manifest.read_text())
        except json.JSONDecodeError as e:
            err(f"{tag} plugin.json is not valid JSON: {e}"); pj = {}
        if pj:
            if not pj.get("name"):
                err(f"{tag} plugin.json missing 'name'")
            elif not KEBAB.fullmatch(pj["name"]):
                err(f"{tag} plugin.json name {pj['name']!r} is not kebab-case")
            v = pj.get("version")
            if not v:
                warn(f"{tag} plugin.json has no version; version falls back to the git "
                     f"commit SHA, so every push ships an update")
            elif not re.fullmatch(r"\d+\.\d+\.\d+", v):
                warn(f"{tag} version {v!r} is not semver")

    # ---- skills
    skills_dir = pdir / "skills"
    if skills_dir.is_dir():
        for sd in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
            sm = sd / "SKILL.md"
            rel = sm.relative_to(ROOT)
            if not sm.exists():
                err(f"{tag} skill {sd.name}/ has no SKILL.md"); continue
            text = sm.read_text()
            if not text.startswith("---"):
                err(f"{rel} has no YAML frontmatter"); continue
            fm_end = text.find("\n---", 3)
            if fm_end == -1:
                err(f"{rel} frontmatter is not terminated"); continue
            fm = text[3:fm_end]
            if not re.search(r"^name:\s*\S", fm, re.M):
                err(f"{rel} frontmatter missing 'name'")
            if not re.search(r"^description:\s*\S", fm, re.M):
                err(f"{rel} frontmatter missing 'description'")
            fname = re.search(r"^name:\s*(\S+)", fm, re.M)
            if fname and fname.group(1) != sd.name:
                warn(f"{rel} frontmatter name {fname.group(1)!r} != directory {sd.name!r}")

    # ---- relative paths cited inside markdown (the check nothing else does)
    for md in sorted(pdir.rglob("*.md")):
        # library corpora cite each other loosely; only check skill-facing docs
        if "structure-library" in md.parts and md.name != "INDEX.md":
            continue
        if "voice-library" in md.parts:
            continue
        for m in re.finditer(r"`((?:\.{1,2}/)[^`\s]+\.(?:md|py|html))`", md.read_text()):
            path_cited = m.group(1)
            if "<" in path_cited or ">" in path_cited:
                continue  # `./<file>.md` is a documentation placeholder, not a citation
            target = (md.parent / path_cited).resolve()
            if not target.exists():
                err(f"{md.relative_to(ROOT)} cites a path that does not resolve: {path_cited}")

# --------------------------------------------------------------------- report
for w in warnings: print(f"warning: {w}")
for e in errors:   print(f"error:   {e}")
print()
n_ok = len(seen)
if errors or (STRICT and warnings):
    print(f"FAIL — {len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1)
print(f"OK — marketplace {name!r}, {n_ok} plugin(s), {len(warnings)} warning(s)")
