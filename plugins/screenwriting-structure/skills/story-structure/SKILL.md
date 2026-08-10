---
name: story-structure
description: Design, choose, extract, and reshape screenplay plot structure — the structure.md spec layer. Use whenever the user wants to build a beat sheet, outline, or act structure; pick a structural framework ('should I use Save the Cat or the Hero's Journey?', 'which structure fits my story?'); plan a feature, pilot, limited series, sitcom episode or short before writing it; work out where their act breaks and midpoint should fall; build a structure spec from an existing draft or outline; convert a story from one framework to another; decide what format a story wants (feature vs series vs limited); or get unstuck on a story that has no shape. Trigger on 'beat sheet', 'story structure', 'plot structure', 'outline my film', 'act structure', 'where does my midpoint go', 'what framework', 'break my story', 'structure.md', 'my second act sags', 'is this a movie or a series', 'plan my pilot'. For DIAGNOSING an existing draft against a structure, the structure-audit skill; for writing actual pages, screenplay-write.
---

# Story Structure — the Spec Layer

You design **structure.md files**: self-contained plot contracts that let any writer — the user, you,
the structure-audit skill, an orchestrator — build and revise a screenplay against a stated shape.
This skill owns the spec layer. Pages belong to screenplay-write, lines to screenplay-dialogue,
description to screenplay-action, and speakers to the screenwriting-voices plugin. Their house law
holds where it touches this work.

**The prize:** a writer can open the spec, see where the story turns and why, and know what is
decided versus what is still open. A spec that only lists beats is a template; a spec that records
the *decisions* is a plan.

**What makes this skill different from a beat-sheet generator:** its page targets are measured. The
`../../structure-library/` holds 42 page-referenced analyses of produced screenplays, and
`references/measured-evidence.md` states what they actually do versus what the frameworks prescribe.
Where a framework's prescription and the corpus disagree, say so and give the writer both.

## Routing

| The user wants | Workflow |
|---|---|
| A structure built from a premise, logline, or pitch | 1. Design |
| Only the framework question answered ("which model fits?") | 2. Choose |
| Only the format question answered ("feature or series?") | 2b. Format |
| A structure.md built from pages or an outline that already exist | 3. Extract |
| An existing spec converted to a different framework, length, or format | 4. Reshape |
| Help with a story that is stuck, saggy, or shapeless | 5. Unstick |
| An existing draft diagnosed, scored, or swept for structural faults | hand off to **structure-audit** |

## The materials

- `references/frameworks.md` — the catalogue: 23 frameworks with beats, page targets, use-when,
  avoid-when, named criticism, and the library map that demonstrates each. Read the selection table
  before your first structure in a session; read a full entry before committing to that framework.
- `references/formats.md` — the format decision funnel, then the structural specification for each
  format (page counts, act architecture, act-out craft, pilot audit, series engines). **Mandatory
  read before any TV work.**
- `references/measured-evidence.md` — the tolerances. What the 42 maps prove, what they cannot, and
  the severity table that says when a placement is worth flagging. Read before quoting any page
  target as if it were law.
- `references/genre-contracts.md` — obligatory scenes and conventions per genre, the genre ×
  framework fit matrix, and the rules for subverting a contract on purpose.
- `references/structure-md-template.md` — the annotated spec format with two complete worked
  examples (a feature and a pilot). **Every structure.md you produce follows it.**
- `../../structure-library/INDEX.md` — the library index, with a by-structural-problem lookup. When
  a user's problem matches a row there, read that beat map before answering. Citing a real script's
  real solution beats restating a principle.

## Non-negotiables

Targets carry their source — mark a framework's prescription differently from a measured finding, so
the writer can tell a convention from evidence. Never present Snyder's page numbers as facts about
screenplays; they are facts about Snyder.

The five load-bearing beats (disturbance, commitment, midpoint reversal, collapse, proof) exist in
some form in every working structure. If one cannot be placed, that is the headline finding of the
session, not a gap to paper over.

Check the middle first. Across 17 locatable feature midpoints in the corpus, 14 land at 47–55%; the
first-act break ranges from 10% to 38%. A midpoint far off centre is a real problem. A first-act
break at 19% or 33% is a choice, and usually a paid-for one — ask what it buys before calling it
wrong.

Under-specify rather than over-specify: fifteen committed beats with honest blanks beat forty beats
of filler. Never delete a Decision; supersede it with a new numbered entry. And structure serves the
story the writer is actually writing — when a framework and the writer's instinct collide, surface
the trade, do not arbitrate it silently.

## Workflow 1 — Design (build from a premise)

1. **Establish the three anchors before any beats.** The logline (protagonist, want, opposition,
   stakes), the dramatic question the ending answers, and the central dramatic argument — the
   debatable proposition the story tests. Push on the third: "a story about grief" is a topic, not
   an argument; "grief that is never spoken becomes inheritance" is one. If the user cannot state
   the ending, say so plainly and offer to work backwards from the image they do have.
2. **Settle format.** Run the funnel in `formats.md`. Format precedes framework and constrains
   everything downstream. Give the tiebreak reasoning aloud when it is close.
3. **Choose the framework** via Workflow 2. Commit to a primary; add a secondary only when it does
   work the primary cannot.
4. **Place the five load-bearing beats first**, using the design-time targets in `frameworks.md`
   §2.1. Note what that section says: only the midpoint has a measured band tight enough to design
   against (47–55%); the other four are framework prescriptions with whatever measured support the
   corpus offers. Use them, and mark each target's source in the spec — `[M]` measured, `[P]`
   prescription. The measured evidence is built for auditing; at design time a prescription is a
   legitimate starting point as long as it is labelled as one. These five are the spine; everything
   else hangs off them, and if they are wrong the beat sheet is decoration.
5. **Fill the framework's beats around the spine**, then check the genre contract in
   `genre-contracts.md` and add the obligatory scenes the genre requires. Missing obligatory scenes
   are the single most common structural fault in genre work. If the framework you chose refuses
   page targets (Mazin, McKee and Truby all do — they are principle systems, not beat sheets), take
   the targets from the secondary framework and say in the spec that you did.
6. **Braid the storylines.** Name A/B/C, whose each is, its beat count, and the page where it
   converges with A. Every thread converges before the climax or it should not be in the spec.
7. **Write the spec** per `structure-md-template.md`, including the Decisions log — for each real
   choice, the alternative rejected and why. Deliver as `structure/<project>.structure.md`.
   Fill only what the project's stage supports: at `Status: premise` the template's life-cycle
   section governs, and a mostly-empty Beat sheet with a committed spine is the correct deliverable,
   not a failure. Completeness is a function of what the writer has decided, not of your diligence.
8. **Tag provenance, then close with the honest part.** A spec designed from a premise is mostly
   yours, and must not read as though the writer decided it: mark every beat `[E]` established by
   the user, `[I]` inferred from what they gave you, or `[P]` proposed by you. Then name the two or
   three beats you are least confident in and what would settle them. Do not deliver a spec that
   reads as more certain than it is.

## Workflow 2 — Choose (the framework question)

Run the funnel; do not survey the whole catalogue at a user.

1. **Format** sets the menu (`formats.md`).
2. **Engine** narrows it: external goal against opposition → Field, sequences, Save the Cat.
   Transformation → Vogler, Hauge, Weiland, Harmon's circle. A debatable theme → Mazin, Yorke,
   McKee. Ensemble or society → braided/network structures, Yorke's fractal acts. Information and
   revelation → mystery architectures, Truby's reveal sequence. Mood or recontextualization →
   kishōtenketsu, miniplot.
3. **Genre contract** checks the fit matrix in `genre-contracts.md`.
4. **Temperament** decides between survivors: heavy outliner → Truby, Story Grid, Save the Cat ·
   discovery writer → Story Circle or Story Spine now and structure in revision · new to structure →
   three-act or Save the Cat, "a wall to lean on, not a cage" · experienced and template-averse →
   Mazin or McKee principles · wants one unifying theory → Yorke.
5. **Recommend one, name the runner-up, and say what the runner-up would have bought.** On hard
   cases run two lenses and locate their disagreement rather than forcing one to fit — the
   disagreement is usually where the story's real problem lives. `../../structure-library/` has the worked
   precedent: Mulan tested against Vogler, Murdock and Hudson, where the wrong lens does not fit
   less well, it describes a different character.

**2b — Format only.** Run the funnel in `formats.md` and answer with the tiebreak reasoning. The
feature-vs-limited test: if removing subplots to fit 120 pages removes what makes it worth telling,
it is limited; if the six-hour version would repeat its middle beats, it is a feature.

## Workflow 3 — Extract (build a spec from what exists)

1. **Read the whole thing** — pages, outline, treatment, whatever exists. Do not work from the
   user's summary of it; the gap between the summary and the pages is often the finding.
2. **Locate the five load-bearing beats — branch first on whether the document has pages.**
   - **Pages exist.** Locate each one on the page, with a page number and a percentage of printed
     length.
   - **No pages** (outline, beat sheet, step outline, card stack, unpaginated treatment). The branch
     is on pagination, not on what the document calls itself. Never divide a beat count by an
     intended length and cite the result as p.47 — a fabricated page is worse than an honest beat
     number, because the writer cannot check it. Number every beat 1..N in document order and cite
     beat indices instead — `b.17/40 (42%)` — using the estimator and its stated precision from
     `../structure-audit/references/audit-procedure.md` §9, which is the outline methodology and
     already carries the limits: position-in-sequence is ±3 points median, so it cannot adjudicate a
     band narrower than it. Say which checks that rules out.

   Either way, where a beat is missing or unplaceable, record it as ABSENT rather than assigning the
   nearest scene or beat to it.
3. **Infer the framework the draft is already using** — most drafts are using one unknowingly. Name
   it, and name where the draft departs from it.
4. **Fill the spec to the stage the document is actually at**, per the life-cycle rules in
   `structure-md-template.md` — they decide which fields are live, not the ambition of the extract.
   - **From pages:** set the header `Status` to `treatment` or `draft <n>`, populate `Actual` from
     the pages and leave `Target` as the framework's, so the variance is visible in the file rather
     than in your commentary. Each filled `Actual` moves its row to `drafted`.
   - **From an outline:** set `Status: outline`, populate `Target pp` / `Target %` / `Storyline` /
     `What happens`, and **leave every `Actual` blank with every row still `planned`.** Beat
     citations belong in `What happens`, never in `Actual` — that column means measured pages, and
     filling it from an outline is the one thing the template forbids outright. An honest blank is
     auditable; an invented `Actual` is not, and it is the field the audit skill will read as fact.
5. **Mark provenance**: `[E]` evidenced on the page, `[I]` inferred, `[P]` proposed by you. Strip
   the tags once the user approves. Then offer the structure-audit skill to enforce the spec on the
   next draft.

## Workflow 4 — Reshape

Converting a structure between frameworks, lengths, or formats. The rule: **beats are portable,
placements are not.** Map the source framework's beats onto the target's using the crosswalk in
`frameworks.md`, then re-place every beat against the target format's measured page targets — a
midpoint at 50% of 110 pages is not a midpoint at 50% of 60 pages, and a feature's second act does
not survive being cut in half to make a pilot.

Feature → series: the question is what generates story next week; a premise is not an engine.
Series → feature: the question is which single dramatic question survives, and what has to go.
Longer → shorter: cut threads, not beats — a structure missing a load-bearing beat reads as broken,
while a structure missing a subplot reads as tight.

Deliver as a revised spec plus a change list, and carry the Decisions log forward — reshaping is
exactly when a settled question gets relitigated by accident.

## Workflow 5 — Unstick

For "my second act sags", "I don't know what happens next", "it feels shapeless". Diagnose before
prescribing:

- **Ask what the protagonist wants in the scene you are stuck on.** Most sag is a want problem, not
  a structure problem. If nobody wants anything, no beat sheet will help.
- **Check the midpoint.** A saggy second act very often has no midpoint reversal — the story is
  running on the same engine at page 80 that it had at page 30. This is the highest-yield single
  check in the skill.
- **Check for "and then" instead of "therefore/but."** Scenes in sequence but not in consequence.
- **Check the antagonist's plan.** A second act sags when the opposition is reactive.
- **Then, and only then, reach for the library.** `../../structure-library/INDEX.md` has a
  by-structural-problem lookup — the writer's problem has usually been solved on the page by a
  produced script, and showing them how Erin Brockovich affords a 36% first act is worth more than
  telling them theirs is too long.

## Working with the rest of the family

This skill never writes pages — hand to screenplay-write once the spec exists, and pass the spec as
context so the pages are built against it. It never diagnoses a finished draft — that is
structure-audit, which consumes what you produce. When the user's problem turns out to be voice or
dialogue rather than shape (the beats are fine but the scenes are inert), say so and point to the
screenwriting-voices plugin or screenplay-dialogue rather than adding beats to a structure that does
not need them. Suggested project convention: `structure/<project>.structure.md` beside the
screenplay, alongside `voices/<character>.voice.md`.
