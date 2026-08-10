#!/usr/bin/env bash
# Bump a plugin's version — the only thing that actually ships an update to users.
#
#   ./scripts/bump-version.sh screenwriting-structure patch
#   ./scripts/bump-version.sh screenwriting-voices minor
#   ./scripts/bump-version.sh screenwriting-structure 2.0.0
#
# Claude resolves a plugin's version from its plugin.json. If that string does not
# change, users keep the cached copy however many commits you push.

set -euo pipefail
cd "$(dirname "$0")/.."

PLUGIN="${1:-}"
BUMP="${2:-patch}"

if [[ -z "$PLUGIN" ]]; then
  echo "usage: $0 <plugin-name> [major|minor|patch|X.Y.Z]" >&2
  echo "available:" >&2
  find plugins -maxdepth 1 -mindepth 1 -type d -printf '  %f\n' >&2
  exit 1
fi

MANIFEST="plugins/$PLUGIN/.claude-plugin/plugin.json"
[[ -f "$MANIFEST" ]] || { echo "no manifest at $MANIFEST" >&2; exit 1; }

NEW=$(python3 - "$MANIFEST" "$BUMP" <<'PY'
import json, re, sys
path, bump = sys.argv[1], sys.argv[2]
d = json.load(open(path))
cur = d.get("version", "0.0.0")
if re.fullmatch(r"\d+\.\d+\.\d+", bump):
    new = bump
else:
    if not re.fullmatch(r"\d+\.\d+\.\d+", cur):
        sys.exit(f"current version {cur!r} is not semver; pass an explicit X.Y.Z")
    a, b, c = (int(x) for x in cur.split("."))
    if bump == "major":   a, b, c = a + 1, 0, 0
    elif bump == "minor": b, c = b + 1, 0
    elif bump == "patch": c += 1
    else: sys.exit(f"unknown bump {bump!r}: use major, minor, patch, or X.Y.Z")
    new = f"{a}.{b}.{c}"
d["version"] = new
# rewrite preserving key order, trailing newline
json.dump(d, open(path, "w"), indent=2, ensure_ascii=False)
open(path, "a").write("\n")
print(new)
PY
)

echo "$PLUGIN -> $NEW"

# Guard the documented failure mode: a version in the marketplace entry masks plugin.json.
python3 - <<'PY'
import json, sys
m = json.load(open(".claude-plugin/marketplace.json"))
bad = [p["name"] for p in m.get("plugins", []) if "version" in p]
if bad:
    print(f"WARNING: marketplace entries declare a version: {', '.join(bad)}", file=sys.stderr)
    print("plugin.json always wins, so a stale entry here can hide a real update. Remove them.", file=sys.stderr)
PY

if command -v claude >/dev/null 2>&1; then
  claude plugin validate . || { echo "validation failed — not committing" >&2; exit 1; }
else
  python3 scripts/validate.py
fi

echo
echo "next:"
echo "  git commit -am \"${PLUGIN}: <what changed> (v${NEW})\" && git push"
