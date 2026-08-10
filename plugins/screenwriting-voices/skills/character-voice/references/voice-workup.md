# The Voice Workup — Extract, Challenge, Complete

Extraction answers "what does the page show?" A workup answers three harder questions: what does
the page show, what does the page CONTRADICT about itself, and what is the page silent about that
a whole voice needs? The deliverable is a complete draft voice.md — every axis addressed — where
every value is labeled by how it was earned, plus a report the writer can argue with.

Use this workflow when the user has an existing screenplay (or episodes) and wants a character's
voice made whole: "build her full voice from my draft and tell me what's missing," "is he
consistent?", "complete this voice."

## Stage 1 — Collect, with context

Gather every line of the character with scene/page anchors — and per scene, note two things plain
extraction skips: **who they're talking to** and **what the stakes are**. Both are needed later to
tell inconsistency apart from its two lookalikes (state modulation and interlocutor-shift).
Reported speech is not evidence: what other characters SAY about how this character talks is a
claim to test, not a feature to record.

Sample-size floor: under ~15 lines, say so up front — the workup will be mostly proposals, and
the report should read as a design document, not an analysis.

## Stage 2 — Coverage sweep (all axes, no skipping)

Walk the FULL checklist — the 16 axes of `axes.md`, humor (style + target + off-switch), the four
marker palettes (openers, tags, concession, address), listening behavior, every origin layer,
every engine field (signature move, obsessions, metaphors, taboos, tics, never-says), every
pressure state (anger, fear, grief, deceit, tenderness), and evolution. For each item assign:

- **EVIDENCED** — two or more instances; quote the best one.
- **THIN** — a single instance; quote it, flag it.
- **SILENT** — nothing on the page. Silence on an axis is a finding, not a blank: a script that
  never shows the character afraid has not disproven a fear-voice; it has left it undesigned.

Output as a compact table (item · status · best quote or "—"). This table IS the "what's missing"
answer; everything SILENT or THIN feeds Stage 5.

## Stage 3 — Challenge pass (the inconsistency taxonomy)

Scan chronologically for the six ways a script argues with itself about a voice. Every finding
needs two quoted lines with page anchors — one finding, one pair, no vibes.

1. **Unmotivated axis flips.** The hedger goes absolute, the clipped voice turns cascading — with
   no stakes change, no listener change, no arc beat in between.
2. **Marker instability.** An opener or tag that owns act one and vanishes by act three; a new tic
   appearing on page 70; the same discourse palette drifting between characters.
3. **Register osmosis.** The character converges toward whoever they share the most scenes with.
   (Sometimes intentional — a courtship, an apprenticeship. That's the classification question.)
4. **Origin wobble.** L1/dialect features strong early and gone late with no proficiency arc; or
   dosage spikes at random rather than at pressure; or wrong-kit features (universal-donor errors
   — a French speaker dropping articles Russian-style). Never "correct" an auteur register — test
   it for internal consistency instead.
5. **Pressure-shadow.** The stakes rise and the voice doesn't move. A character whose biggest
   scene sounds like their smallest has no modulation layer — usually the single most important
   gap the workup finds.
6. **Cast collision.** This character and another share a fingerprint (same markers, same rhythm,
   swap-test failure in shared scenes). Not strictly an internal inconsistency, but the spec being
   built should deliberately resolve it, so it belongs in the report.

Classify every finding as exactly one of:
- **CONTRADICTION** — the script is simply inconsistent; a side must be chosen.
- **ARC** — the change tracks story events; encode it in Evolution Notes, don't fix it.
- **STATE** — the change tracks scene pressure or listener; encode it in Under Pressure /
  register range. (Check stakes and interlocutor from Stage 1 BEFORE calling anything a
  contradiction — most false findings die here.)
- **AUTHOR'S CHOICE** — evidence genuinely balanced; the writer decides.

## Stage 4 — Resolution

For CONTRADICTION and AUTHOR'S CHOICE findings, propose a resolution each — with a recommended
default and what it costs ("keep the act-one hedger: the act-three verdicts become earned peaks;
keep the act-three voice: rewrite ~6 early lines, listed"). Interactive sessions: batch these as
one set of questions, don't drip them. Unattended runs: take the evidence-majority side, and log
every such call in the report under "Decisions made for you."

## Stage 5 — Completion (proposing what makes it whole)

For every SILENT and THIN item, propose — never silently invent:
- **Axes**: 2–3 candidate values per gap, each consistent with the evidenced axes and the
  signature move, one recommended. A gap proposal that contradicts an evidenced axis is wrong by
  definition.
- **Mandatory sections with no page evidence** (usually Under Pressure states the story never
  visited, the joke if the character never jokes on the page, missing-state calibration lines):
  write full drafts in-voice, because a spec with holes in these sections isn't usable.
- **Signature move**: if the sweep didn't surface one, propose it FIRST and revisit the axis
  proposals under it — the mechanism disciplines every other guess.

## Stage 6 — Assemble with provenance tiers

Deliver the draft voice.md with every value tagged:
- **[E]** evidenced — with scene/page cites collected in Provenance.
- **[I]** inferred — no direct instance, but implied by evidenced material (a voice that's
  clipped, sealed, and interrupts probably yields-never; say the reasoning in one clause).
- **[P]** proposed — invention pending the writer's approval.
Calibration lines follow the same rule: real quoted lines marked by state, plus [P] lines for the
states the script never showed. On approval, strip the tags and save the clean spec.

## The workup report (delivered BEFORE the spec)

```markdown
# VOICE WORKUP — <character>, <script>
Lines sampled: <n> across <scenes> scenes · Confidence: <full / partial / mostly-design>

## Coverage
<the Stage-2 table>

## Findings
<numbered; each: classification · the two quoted lines with pages · resolution
 (chosen or proposed) · what it costs>

## Open questions for the writer
<the AUTHOR'S CHOICE batch, with recommended defaults>

## What would make this voice whole
<3–6 sentences: the shape of what's missing — usually the modulation layer, the joke,
 and one axis nobody committed to — and what the [P] sections propose>
```

Then the tagged draft spec. Two hand-offs close the loop: the audition workflow (WF5) is the
fastest way to test the [P] sections — generate the pressure beats the script never wrote; and
once the spec is approved and clean, the voice-dialogue skill's Audit mode enforces it against
every future draft.
