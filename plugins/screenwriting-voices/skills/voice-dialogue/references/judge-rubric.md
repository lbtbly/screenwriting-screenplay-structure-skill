# The Judge Rubric — Scoring Dialogue Against Voice Specs

How to evaluate dialogue when voice.md files exist. The judge's product is a diagnostic report a
writer can act on: every claim cites a line, names the axis or rule it violates, and quotes the
spec text it violates. Scores are diagnostic attribution, not ground truth — the rubric exists so
two runs of the judge disagree about numbers, not about problems.

## Judge discipline (before any scoring)

1. **Read every voice.md fully first.** Build each character's whitelist: origin features, licensed
   tics, register range, stylized-baseline notes. The AI-tells scan (see `ai-tells-dialogue.md`)
   loads this whitelist before it fires anything.
2. **Judge against the script's own register, not naturalism.** Sorkin patter, verse, multi-cam
   symmetry, period formality: the spec and the format set the baseline.
3. **Never rewrite while judging.** Diagnosis and surgery are separate passes; a judge that fixes
   as it goes stops seeing.
4. **Fresh context for pipelines.** If the same session wrote the dialogue, an orchestrator should
   run the judge in a fresh context with only: the scene, the voice.md files, this rubric. Judging
   your own just-written lines with the reasoning that produced them still warm is grading your own
   homework.
5. **Quote to accuse.** A violation claim has three parts: the line (verbatim, with scene/page or
   line number), the spec text it breaks (verbatim), one sentence of why. No third part, no claim.

## The five dimensions

Score each 1–5. Anchors below; between-anchor scores take the lower anchor's label.

### D1 — Voice fidelity (scored PER CHARACTER)
Does each line sit inside its speaker's spec?
Check, in order: Never-says violations (automatic cap at 2 for that character) · axis compliance
(directness, certainty, register, tempo... — flag the moved axis by name) · marker fidelity
(openers, tags, address, concession style) · origin-feature correctness (right features for the
declared L1/variety, right dosage for the intensity dial, rule-governed — a wrong dialect rule is
a P0 fidelity failure, not a style note) · state modulation (did the Under Pressure deltas fire in
the pressure beats? a character at their baseline while their house burns is a fidelity failure of
the modulation layer) · tic budget (licensed tics present but ≤ their natural frequency; unlicensed
recurring tics flagged).
- 5: every line survives; the spec's signature move is audibly driving choices.
- 4: 1–2 soft drifts, no never-says or origin-rule breaks.
- 3: pattern of drift on one axis, or one never-says break.
- 2: multiple axes ignored, or origin features wrong/misdosed.
- 1: the spec is decoration; any character could own these lines.

### D2 — Differentiation (scored for the CAST)
Run the cover-the-names test: strip cues, shuffle nothing, read. Attribute each line.
- 5: 95%+ attributable; even receipts ("Uh-huh." / "Grand." / "Great great.") sort correctly.
- 4: leads attributable; one supporting pair blurs.
- 3: leads only; support cast interchangeable.
- 2: only content (who knows what) distinguishes speakers, not voice.
- 1: one voice wearing name tags.
Also flag: marker collisions (two characters sharing an opener/tag not by design), register-distance
collapse (all voices within one notch on register + texture + length), and symmetrical turn lengths
across different-verbosity specs.

### D3 — Line function
Every line does at least one job: reveals character, advances the scene, carries subtext, or
earns its keep as entertainment (the four functions, per the screenplay-dialogue skill). Flag
lines doing zero jobs, and exposition delivered as exposition (recap between people who both know,
"Remember when", unprompted backstory).
- 5: most lines do two jobs; zero freeloaders.
- 3: a few freeloaders or one naked exposition beat.
- 1: information-delivery formation throughout.

### D4 — Naturalism / machine tells
Run the `ai-tells-dialogue.md` scan (whitelist first; severity and density rules as specified
there). Score from findings: 5 = nothing above P2 · 4 = isolated P1s under density threshold ·
3 = P1 density reached, or one P0 · 2 = multiple P0s · 1 = cluster escalation across scenes.
Report tells as craft notes with fixes, never as authorship accusations.

### D5 — Scene craft (interaction layer)
From `ensemble-craft.md` and `rendering-craft.md`: is the power map audible and does the voice
shift when the gun changes hands · listening evidence (each line registers the previous one, or
refuses it visibly) · mode choreography (no emotional+declarative in one breath; mismatches
engineered, not accidental) · turn-taking realism (interruptions, overlaps, silence-as-turn where
the specs license them) · question→answer adjacency (evasive/curated characters must not answer
everything asked).
- 5: the scene turns; power handoff lands; silence is used.
- 3: functional volley, but everyone cooperates and nobody misfires.
- 1: interview transcript.

## Report format

```markdown
# VOICE JUDGMENT — <scene/script id>
Specs loaded: <files> · Format baseline: <naturalist drama / multicam / period / ...>
Verdict: <one honest paragraph — the note you'd give the writer over coffee>

Scores: fidelity <per char: NAME n/5, ...> · differentiation n/5 · function n/5 ·
naturalism n/5 · scene craft n/5   (diagnostic, not a grade — read the findings)

## Findings (prioritized)
P0 — <finding>. Line: "<verbatim>" (<where>). Spec: "<verbatim spec text>". Why: <1 sentence>.
    Fix direction: <1 sentence, subtract-and-sharpen, never inject>.
P1 — ...
P2 — ...

## What's working
<2-4 specific things to keep, with line cites — a judge that only finds faults gets ignored>

## Whitelist notes
<origin/dialect/tic features detected and correctly NOT flagged — proves the scan was spec-aware>
```

## Script-wide voice audit (drift detection)

For a full draft, per character:
1. **Collect** — pull every line of the character across the script (with scene/page anchors).
2. **Baseline** — their voice.md; if none exists, extract a provisional spec from Act 1 and say so.
3. **Scan chronologically** for drift: axis migration (hedging creeping into an absolute voice),
   marker fade (tics vanish after p. 40 — or worse, multiply), origin-dial flattening (L1 features
   strong in act one, gone by act three, with no story reason), register osmosis (two characters
   converging the longer they share scenes — sometimes intentional; ask), pressure-delta failures
   at the big scenes.
4. **Distinguish drift from arc.** Evolution Notes in the spec license change; drift is unlicensed
   change. If the change tracks story events, propose an Evolution Notes amendment instead of a fix.
5. **Report** per character: baseline → observed timeline (act by act) → top 5 drift examples with
   page cites and spec quotes → licensed-evolution notes → fix list. Then a cast-level summary:
   differentiation early vs late (run D2 on an early scene and a late scene), and the two scenes
   most in need of a voice pass.

## Calibration expectations (what good judging looks like)

Real produced scripts run 4–5 on these dimensions — if a Succession excerpt scores 2, recalibrate
the judge, not the scene. A deliberately voice-swapped rewrite must fail D1/D2 loudly. A scene
whose French-L1 character says "I am here since one hour" must show that line in Whitelist notes,
not in Findings — flagging it is a judge failure and goes in the report as a correction to the
judge run, not as a finding.
