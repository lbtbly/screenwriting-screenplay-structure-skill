---
name: character-voice
description: Design, extract, work up, refine, and audition parameterized character voice specs (voice.md files) for screenwriting. Use whenever the user wants to create or define a character's voice, build a 'voice spec', 'voice sheet', 'voice profile' or voice.md; give a character an accent, dialect, non-native English (French, Russian...), regional or period voice; extract a voice from an existing script; run a voice WORKUP on a screenplay — find what's missing or inconsistent in a character's dialogue and complete the voice along every axis; check whether cast voices are distinct; generate an 'audition scene'; or open the Voice Designer HTML. Trigger on 'design a voice', 'voice for my character', 'make her sound like', 'voice.md', 'what's missing in his voice', 'is she consistent across the script', 'complete the voice from my draft', 'my character is French/Southern/from...'. For WRITING scene dialogue from finished specs, the voice-dialogue skill; for general dialogue craft, screenplay-dialogue.
---

# Character Voice — the Spec Layer

You design **voice.md files**: self-contained rendering contracts that let any writer (the user,
you, the voice-dialogue skill, an orchestrator) produce a character's dialogue with the character's
fingerprint intact. This skill owns the spec layer; the craft of the individual line lives in the
screenplay-dialogue skill, and screenplay formatting lives in screenplay-write. Adopt their rules
where they touch this work — the cover-the-names test, the ban on phonetic dialect spelling
(generalized here beyond period pieces), and the two-tic maximum are inherited house law.

**The prize:** cover the character names and a reader can still tell who's speaking. Voices that
pass are built from a committed *stack* of axis values plus one signature move — not from an
accent, a catchphrase, or a quirk.

## Routing

| The user wants | Workflow |
|---|---|
| A new voice from scratch (conversation) | 1. Interview |
| A voice.md for a character who already has script pages | 2. Extract |
| A COMPLETE voice from a screenplay — all axes covered, gaps and inconsistencies challenged, missing pieces proposed | 3. Workup |
| A critique/upgrade of an existing spec, or "do my voices differ?" | 4. Refine |
| To hear a spec before trusting it | 5. Audition |
| The interactive designer page | 6. Designer |
| A scene WRITTEN from specs, or dialogue judged against them | hand off to **voice-dialogue** |

Formats: everything here works for features, TV drama, multi-cam, shorts, and audio.

## The materials

- `references/axes.md` — the 16-axis taxonomy with notch definitions and corpus exemplars. Read
  it before your first voice in a session; skim the relevant group when a single axis is in play.
- `references/voice-md-template.md` — the annotated format, its rules, and a worked example.
  Every voice.md you produce follows it.
- `references/dialect-and-l1.md` — the method and feature kits for origin work: French deep kit,
  Spanish/Russian/German/Mandarin/Arabic quick kits, Indian English, AAVE, Southern, NYC, London,
  Irish, Scottish. **Mandatory read before giving any character an L1, dialect, or literacy
  marking.**
- `references/exemplars.md` — a study map of the user's own Script Library: which produced voices
  demonstrate which mechanism.
- `references/voice-workup.md` — the full workup procedure (coverage sweep, inconsistency
  taxonomy, resolution rules, provenance tiers, report format). Mandatory read before Workflow 3.
- `assets/voice-designer.html` — the standalone designer page. `assets/voice.blank.md` — empty
  template.

Non-negotiables, whatever the workflow: specs are self-contained (a renderer needs nothing but the
file); origin renders as grammar, idiom and rhythm — never respelled pronunciation (the auteur
exception and its conditions live in dialect-and-l1.md); at most two tics; literacy/L2 "mistakes"
are systematic transfer features from the kits, never random errors; specificity over stereotype —
an origin is a *person's* subset of 3–5 features, not a nationality costume. Under-specify rather
than over-specify: 8–12 committed values beat 16 shrugs, and a spec past ~180 lines is a costume
trunk.

## Workflow 1 — Interview (create from scratch)

Voice flows from biography, so start with the person, not the dials.

1. **Intake** (one batch of questions, not twenty): who/where/when — age, upbringing place and
   class, education, occupation, era; what they want long-term; how they see themselves; what
   their speech must survive (which rooms, which listeners). If the user has a background.md or
   pages, take them.
2. **Find the signature move first.** Propose 2–3 candidate mechanisms (the incongruity or engine
   that makes the voice: erudition-as-hiding-place, service-warmth-over-menace, hedges-then-
   scalpel) and let the user pick or counter. Everything else arranges itself around this.
3. **Commit the load-bearing axes.** Walk the five groups (stance, syntax, lexicon, sound, origin)
   proposing values with a one-line rendering note each — but only commit axes that matter for
   this character; leave the rest unstated. Where the user gave a trait ("she's honest"), translate
   it to the axis and notch ("candor: radical — tells truths that cost her").
4. **Origin, if any.** Open dialect-and-l1.md; pick 3–5 signature features WITH the user, set the
   intensity dial, define code-switch triggers. Never assign the whole kit.
5. **Pressure map.** Ask the two questions that unlock it: "What does their anger look like — hot
   or cold?" and "Who unlocks the tenderness?" Fill the state deltas (the law: stress subtracts
   complexity, amplifies signature, until the breaking point).
6. **Write the calibration lines yourself** — 6–10, varied labeled states, final-draft quality.
   These are the hardest and most valuable part; show them and revise on reaction.
7. Assemble per the template, deliver as `voices/<name>.voice.md`, and offer an audition (WF5).

## Workflow 2 — Extract (reverse-engineer from pages)

1. **Collect the corpus**: every line of the character from the provided script(s). If parsing a
   screenplay file, character cues are the uppercase centered names; take all their speeches, note
   scene positions for provenance.
2. **Read for the mechanism before the metrics.** First pass: what's the signature move? Second
   pass, per axis group: where do they sit, with 2–3 quoted lines as evidence per committed axis.
3. **Mine the special layers**: markers (openers/tags/receipts — count them, they're the
   fingerprint); listening behavior; repetition habits; origin features actually present (match
   them to kit features by rule, and respect what the writer licensed — extraction never
   "corrects" an auteur register); pressure scenes vs. rest scenes → the state deltas; any arc
   (early vs. late lines) → Evolution Notes.
4. **Calibration lines: quote the real ones.** Pick the 6–10 most voice-defining actual lines,
   label their states. Extraction uses real lines; only invented voices get invented lines.
5. Write the spec with a **Provenance** block (source, scenes sampled, sample size) and a
   confidence note if the sample is thin (under ~25 lines: say which sections are inference).

## Workflow 3 — Workup (extract + challenge + complete)

Extraction records what the page shows; the workup also interrogates what the page contradicts
and what it never covered, then proposes what makes the voice whole. Full procedure:
`references/voice-workup.md` — read it before running one. The shape:

1. **Collect with context** — every line, plus per-scene interlocutor and stakes (needed to tell
   inconsistency apart from state modulation and listener-shift).
2. **Coverage sweep across ALL axes** — every axis, marker palette, origin layer, engine field,
   and pressure state graded EVIDENCED / THIN / SILENT. Silence is a finding, not a blank.
3. **Challenge pass** — six inconsistency types (unmotivated axis flips, marker instability,
   register osmosis, origin wobble, pressure-shadow, cast collision), each finding backed by two
   quoted lines with pages, then classified: CONTRADICTION / ARC / STATE / AUTHOR'S CHOICE.
4. **Resolve** — propose a side for each contradiction with its cost; batch the writer's-choice
   questions; in unattended runs take the evidence-majority side and log it.
5. **Complete** — 2–3 candidate values per gap (one recommended, consistent with the signature
   move), and full in-voice drafts for mandatory sections the script never visited.
6. **Deliver** — the workup report (coverage table, findings, open questions, "what would make
   this voice whole"), then the draft spec with provenance tiers: [E] evidenced, [I] inferred,
   [P] proposed. Strip tags on approval; suggest the audition (WF5) to test the [P] sections and
   the voice-dialogue audit to enforce the finished spec on future drafts.

## Workflow 4 — Refine / critique

Run these checks on an existing spec (or a cast of them), report findings with quotes, propose
edits as minimal diffs:
- **Distinctness across the cast**: pairwise, are any two specs within a notch on register +
  verbosity + tempo with overlapping markers? Predict where the cover test will fail; fix by
  moving the cheapest high-yield layer (markers, listening behavior, momentum) rather than
  inventing tics.
- **Spec smells**: axes all mid-scale (no commitments) · tic count over two · origin feature salad
  (more than 5) or costume lexicon without grammar · missing/empty Under Pressure · calibration
  lines that all sound the same state · essence line that describes personality but not speech ·
  never-says list that nothing in the story would ever test.
- **Playability**: the casting test (can you rule actors out?), the joke test (can you write their
  joke from the spec alone?), the read-aloud test on the calibration lines.

## Workflow 5 — Audition

Generate a **one-page audition scene** that stress-tests the spec: a neutral beat, a pressure beat
(pick the state the story will actually use), and the character's joke — against a deliberately
plain scene partner so the voice carries the page. Then: ask the user which lines feel off, trace
each complaint to an axis or kit feature, patch the spec (not just the scene), and promote the best
2–3 audition lines into the calibration set. The audition is the true "preview" the Designer's
rough composite points at. (For full scenes with multiple designed voices, hand off to
voice-dialogue.)

## Workflow 6 — The Designer page

`assets/voice-designer.html` is a standalone offline page (open in any browser): per-axis
hand-written morph lines on fixed beats, origin grammar samples, eight preset stacks, a
rough rule-based composite (honestly labeled as approximation), and voice.md export/import that
round-trips with this skill. When the user brings a designer-exported spec: treat it as a draft —
its calibration lines are composite placeholders; run WF4 checks, then WF5 to replace them with
real lines. When the user asks for the designer, give them the file (copy it out of assets) rather
than describing it.

## Working with the rest of the family

This skill never restates line-level dialogue craft (subtext, exposition, monologue shape,
rhythm) — that's screenplay-dialogue's territory; point there when the user's problem is the
line, not the speaker. When specs exist and the user wants scenes or judgments, voice-dialogue
consumes what you produced. Suggested project convention: `voices/<character>.voice.md` beside the
screenplay, one file per speaking character that matters.
