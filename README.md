# Screenwriting plugins for Claude

A Claude plugin marketplace with two craft plugins for screenwriters. Both work in Claude Code and in Cowork.

| Plugin | What it does |
|---|---|
| **screenwriting-structure** | Designs `structure.md` plot specs from 23 frameworks with page targets measured from produced screenplays, then audits drafts against them. Ships a 42-script structural library and a measurement script. |
| **screenwriting-voices** | Designs `voice.md` character specs (16-axis taxonomy, dialect and L1 kits, an interactive Voice Designer page), then writes, judges, and audits dialogue from them. Ships a 10-voice library. |

## Install

```
/plugin marketplace add lambertbouley/screenwriting-plugins
/plugin install screenwriting-structure@screenwriting
/plugin install screenwriting-voices@screenwriting
```

Replace `lambertbouley` with your GitHub username if the repo lives elsewhere. A local path works too, for testing before you push:

```
/plugin marketplace add ./screenwriting-plugins
```

## Updates

Claude refreshes registered marketplaces in the background after startup, and `/plugin marketplace update screenwriting` forces it.

**A plugin only updates when its version string changes.** Claude resolves a plugin's version from `plugins/<name>/.claude-plugin/plugin.json` first; if that string is unchanged, users keep the cached copy no matter how many commits you push. Version is deliberately *not* duplicated in `marketplace.json`, because a stale entry there can mask a real update.

So: edit, bump, push.

```bash
./scripts/bump-version.sh screenwriting-structure minor
git commit -am "structure: <what changed>" && git push
```

The script bumps the version, validates the marketplace, and prints the resulting version. `major`, `minor`, `patch`, or an explicit version string all work.

## Layout

```
.
├── .claude-plugin/
│   └── marketplace.json          # the catalog — one entry per plugin
├── plugins/
│   ├── screenwriting-structure/
│   │   ├── .claude-plugin/plugin.json
│   │   ├── skills/               # story-structure, structure-audit
│   │   └── structure-library/    # 42 beat maps + index
│   └── screenwriting-voices/
│       ├── .claude-plugin/plugin.json
│       ├── skills/               # character-voice, voice-dialogue
│       └── voice-library/        # 10 voice specs
├── .github/workflows/validate.yml
└── scripts/bump-version.sh
```

Plugin `source` paths in `marketplace.json` are relative to the repository root, not to `.claude-plugin/`.

## Validate before pushing

```bash
claude plugin validate .
```

CI runs the same check on every push and pull request, plus a structural check that catches the things the official validator does not: version drift between `plugin.json` and the marketplace entry, broken relative paths inside skill reference files, and missing `SKILL.md` files.

## Provenance

`screenwriting-structure` was built from a structural knowledge base synthesized from 17 craft guides, ~150 web sources, and original analysis of 42 screenplays. Its beat maps are original structural analysis — they describe and cite page positions in copyrighted screenplays for study and do not reproduce them.

`screenwriting-voices` was copied here from the installed v0.2.0. If you maintain it elsewhere, reconcile the two before pushing — this repo should become its source of truth, not a second copy of it.
