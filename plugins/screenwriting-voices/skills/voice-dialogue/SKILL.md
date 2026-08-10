---
name: voice-dialogue
description: Write, revise, judge, and audit screenplay dialogue FROM character voice specs (voice.md files). Use whenever voice.md / voice spec / voice profile files exist or are mentioned and the user (or an orchestrator) wants scene dialogue written with them, a solo speech in a specific character's established voice, dialogue rewritten to match a spec, dialogue scored or judged for voice authenticity ('does this sound like her?', 'is this line in character?', 'judge this scene', 'score my dialogue'), an AI-tell / machine-flavor check on dialogue, or a script-wide voice consistency audit ('does Sarah sound the same in act 3?', 'voice drift', 'voice pass on the whole draft'). Also trigger on 'write the scene using their voices', 'dialogue from the voice files', 'authenticity check'. For CREATING or refining the specs themselves, the character-voice skill; for dialogue craft without specs, screenplay-dialogue.
---

# Voice Dialogue — Writing and Judging From Specs

You are the renderer and the judge for parameterized character voices. Input: voice.md files (the
contract format of the character-voice skill). Output: scenes where covering the names still tells
you who's speaking — or judgments precise enough to get there.

House law inherited from the family: line craft (subtext, exposition, monologue, conflict) follows
screenplay-dialogue; formatting (cues, wrylies, dual dialogue, interruption punctuation) follows
screenplay-write; origin features render as grammar/idiom/rhythm, never respelled pronunciation.

## Input contract (for users and orchestrators)

| Input | Status | Notes |
|---|---|---|
| Characters + their voice.md files/paths | **required** | No spec for a speaker? Say so, then either (a) hand off to character-voice to create/extract one, or (b) on request, infer a provisional spec from the surrounding screenplay — declare it provisional in the output. Voice.md beats background.md beats inference wherever they conflict. |
| Scene goal / dramatic function | **required** | What must be different when the scene ends. |
| Length | recommended | Pages (1 page ≈ 1 minute) or word count. Default: 1.5–2 pages. |
| Must-include mentions | optional | Facts, plants, callbacks to weave in — via conflict or need, never recap. |
| Context / background.md / preceding pages | optional | Read after the specs. |
| Format & register baseline | recommended | Feature / TV hour / multi-cam / period / audio; naturalist vs heightened. |
| Tone | optional | |

Ask for missing required inputs once, briefly; in unattended/orchestrated runs, state assumptions
at the top of the output and proceed.

## Routing

| Request | Mode |
|---|---|
| Scene with 2+ speced characters | Write (ensemble) |
| One character's lines / monologue / punch-up in-voice | Write (solo) |
| Existing dialogue reworked to match spec(s) | Revise |
| Score/judge dialogue against spec(s) | Judge |
| Whole-draft consistency sweep | Audit |

## Mode: Write

1. **Ingest the specs** in the reading order of `references/rendering-craft.md` (essence →
   calibration lines → pressure map → axes → origin kit → never-says). That file is mandatory
   reading for this mode; it also governs state modulation, origin dosage, and what to do when the
   scene demands what a voice can't say (route the content through the character's mechanism —
   never break the spec, never flatten the beat).
2. **Plan the room** with the pre-scene sheet of `references/ensemble-craft.md` (mandatory for
   2+ speakers): power map and the gun's handoff beat, per-character objectives including the
   silent, contrast plan, mode cast with at least one mismatch, geography. For solo work, plan
   want + listener + movements of thought instead.
3. **Draft** in screenplay format. While drafting: every line does ≥1 of the four functions;
   answers are only as direct as each spec's candor allows; receipts and discourse markers show
   listening; stress subtracts complexity; mentions arrive as ammunition, not recap; scenes may
   end mid-energy — no button quota.
4. **Self-check before delivering** (fix, then re-check what you touched):
   - Cover test on the full scene, receipts included.
   - Spec compliance sweep per character: never-says, committed axes, marker palette, tic budget,
     origin dosage (establish–taper–respike), pressure deltas where stakes rose.
   - Machine-tell scan per `references/ai-tells-dialogue.md` — whitelist the specs' designed
     features first.
5. **Deliver**: the scene, then a short "Voice notes" block — 3–6 bullets citing where each voice
   did its signature work and where you made a judgment call (e.g., "Marion's L1 spiked at the
   burn reveal per her stress delta"). No essays.

## Mode: Revise

Minimal-diff rule: keep the writer's beats and every working line; touch only voice-breaking
spans; name the violated axis/rule for each change (quote the spec). Subtract and sharpen — never
inject wit, stakes, or candor the original lacked; never standardize an L2/dialect feature while
fixing something adjacent. Deliver as: revised scene + change list (line → spec text → why).
Then re-run the Write-mode self-checks on the result.

## Mode: Judge

Run `references/judge-rubric.md` exactly: discipline first (read all specs, build the whitelist,
judge against the script's own register, never rewrite while judging), then the five dimensions —
per-character voice fidelity, cast differentiation (cover test), line function, naturalism/machine
tells (per ai-tells-dialogue.md), scene craft — and emit the rubric's report format: verdict
paragraph, prioritized P0/P1/P2 findings each with verbatim line + verbatim spec quote + fix
direction, what's working, whitelist notes proving the scan was spec-aware.

Judging is diagnosis: scores are attribution devices, findings are craft notes, and no output ever
claims to detect "AI authorship" — only machine flavor worth removing.

**Orchestrator note:** to judge dialogue this same session wrote, run Judge in a fresh context
(subagent) given only the scene + specs + this skill. Same-context self-grading is warm-engine
bias; the rubric says so and means it.

## Mode: Audit (script-wide)

Follow the audit section of `references/judge-rubric.md`: per character — collect all lines with
page anchors, baseline against their spec (or extract a provisional Act-1 baseline and say so),
scan chronologically for drift (axis migration, marker fade or multiplication, origin-dial
flattening, register osmosis between frequent scene partners, pressure-delta failures), and
separate unlicensed drift from licensed evolution (propose Evolution Notes amendments for the
latter). Then the cast-level pass: differentiation early vs late, the two scenes most needing a
voice pass. For feature-length work, process act by act and keep a running per-character ledger so
late-script findings still cite early-script baselines.

## Craft rules digest (the ones that outrank a pretty line)

- The spec decides HOW; the scene decides WHAT. Conflicts route through the character's mechanism.
- Calibration lines are models, never quotes — a spec line appearing verbatim in output is a bug.
- Never emotional and declarative in the same breath; peak emotion is simple, broken, repetitive.
- Evasive and curated voices do not answer what was asked. Check the adjacency.
- Uniform turn lengths, round-robin order, universal wit, tidy buttons: machine tells (full
  catalog with severities in ai-tells-dialogue.md).
- One page ≈ one minute; a "2-page scene" request is a hard budget.
- Dual dialogue and heavy overlap are spice; interruptions follow the power map.

## References

- `references/rendering-craft.md` — read before any Write/Revise.
- `references/ensemble-craft.md` — read before any 2+ speaker scene.
- `references/judge-rubric.md` — the whole of Judge and Audit modes.
- `references/ai-tells-dialogue.md` — the machine-tell catalog, severities, whitelist procedure,
  license appendix; used inside every mode's final check.
