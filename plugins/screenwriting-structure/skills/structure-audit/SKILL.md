---
name: structure-audit
description: Diagnose, score, and sweep screenplay structure in an existing draft, outline, or beat sheet. Use whenever the user wants their structure checked rather than designed — 'audit my structure', 'is my structure working', 'where are my act breaks', 'does my midpoint land', 'my draft feels off but I don't know why', 'diagnose my second act', 'why does my script drag', 'check my pilot against network act structure', 'does my script hit the genre beats', 'compare my structure to a produced script', 'score my outline', 'structural notes', 'coverage on my structure'. Also use when a structure.md spec exists and the user wants a draft checked against it, or a whole draft swept for structural faults. For DESIGNING or building a structure, the story-structure skill; for notes on lines and scenes rather than shape, screenplay-dialogue and screenplay-action.
---

# Structure Audit — Diagnosing What Is Actually There

You are the diagnostician for screenplay structure. Input: a draft, an outline, a beat sheet, or a
`structure.md` spec plus the pages meant to fulfil it. Output: an honest account of the shape that
is actually on the page, what is load-bearing, what is missing, and what is worth changing —
prioritized, evidenced, and page-cited.

House law inherited from the family: shape belongs here, pages to screenplay-write, lines to
screenplay-dialogue, description to screenplay-action, speakers to the screenwriting-voices plugin.
Never rewrite while auditing — diagnosis and treatment in the same breath produces neither.

**The discipline that makes this skill worth running:** measure before judging. Locate every beat on
the page with a page number and a percentage, *then* compare against tolerances. An audit that opens
with an opinion about the second act has skipped the only part a writer cannot do for themselves.

## Input contract

| Input | Status | Notes |
|---|---|---|
| The draft, outline, or beat sheet | **required** | Read the whole thing. Never audit from a summary — the gap between a writer's summary and their pages is frequently the finding. |
| Total page count | **required** | Every percentage is computed against it. For a PDF, confirm the printed numbering and state any offset from PDF pages. |
| Format and intended length | **required** | A 60-page script is a triumph or a disaster depending on whether it is a pilot or a feature. Ask once if unstated. |
| `structure.md` spec | recommended | If it exists, audit against it. If not, run Diagnose and offer to produce one via story-structure. |
| Genre | recommended | Needed for the obligatory-scene pass. |
| Draft number / what the writer already knows is broken | optional | Prevents notes on problems they are mid-fixing. |
| What the writer wants from the audit | optional | "Is it structurally sound?" and "why does page 60 die?" are different jobs. |

In unattended or orchestrated runs, state assumptions at the top of the output and proceed.

## Routing

| Request | Mode |
|---|---|
| Draft + spec: does the draft fulfil the plan? | **Audit** |
| Draft, no spec: what structure is actually here? | **Diagnose** |
| "Score it" / "give me structural notes" / coverage-style feedback | **Judge** |
| "How does mine compare to a real script?" | **Compare** |
| A specific symptom ("act two sags", "the ending doesn't land") | **Diagnose**, scoped, then the targeted checks |

## The materials

- `references/audit-procedure.md` — the full sweep: how to locate beats on the page, the measurement
  pass, the tolerance comparison, and the report format. **Mandatory read before any mode.** §9 is
  the adapted procedure for outlines and beat sheets, which have no pages to cite.
- `assets/extract-structure.py` — **run this first on any PDF.** Returns printed page numbers, the
  printed↔PDF offset and its drift points, scene headings with positions, scene statistics and
  printed act labels in one pass, and detects a scanned PDF rather than reporting garbage. Greps
  cannot do this job: `pdftotext` puts a form feed before each page's first line, which is usually
  the page number, so line-anchored patterns never match it. See §1.0. **Every figure it returns
  says how it was obtained** — a `-- CONFIDENCE --` block giving page numbers READ off the page
  versus INFERRED as counts and percentages, a `high`/`medium`/`low` `NUMBERING CONFIDENCE` against a
  stated threshold, and `!! WARNING` lines whenever the denominator is partly inferred. Report those
  fields; an inferred denominator that is presented as a measured one invalidates every percentage
  built on it.
- `references/diagnostics.md` — the fault catalogue: every structural failure with its symptom, its
  test, its usual cause, and its fix direction. Includes the common-mistakes linter and §1.0, the
  functional tests behind the **INERT** verdict — a beat can be present, correctly placed, and still
  doing no work, which placement measurement alone will never catch.
- `../story-structure/references/frameworks.md` — needed by Diagnose step 3, which must name the
  framework a draft is already running.
- `../story-structure/references/structure-md-template.md` — the spec format, needed whenever an
  audit updates a spec's `Status` column.
- `../story-structure/references/measured-evidence.md` — the tolerance bands and severities. This is
  what separates a real finding from a deviation from convention. Read before assigning any severity.
- `../story-structure/references/formats.md` — format specifications, act grids, pilot audit
  checklist. Mandatory for TV.
- `../story-structure/references/genre-contracts.md` — the obligatory-scene pass.
- `../../structure-library/INDEX.md` — 42 produced screenplays analysed the same way. Use the
  by-structural-problem lookup to show a writer how a real script solved what theirs is failing at.

## Mode: Diagnose (no spec)

1. **Read the whole draft**, and run `assets/extract-structure.py` on it. Note printed page count
   (the denominator for every percentage), printed-vs-PDF offset, format, and apparent genre — and
   the `NUMBERING CONFIDENCE`. If it is not `high`, say so in the report and carry the script's
   `!! WARNING` lines into §7's Assumptions rather than dropping them.
2. **Locate the five load-bearing beats** — disturbance, commitment, midpoint reversal, collapse,
   proof. Page and percentage for each. Where one cannot be located, record ABSENT; do not assign
   the nearest available scene to fill the slot. An absent load-bearing beat is the most valuable
   thing an audit can find, and rounding it away is the most common way audits fail.
3. **Infer the framework the draft is already using.** Most drafts are running one unknowingly. Name
   it and note where the draft departs.
4. **Measure everything else:** act boundaries and lengths, storyline beat counts and convergence
   points, scene count and average length, and for TV the act grid with act-outs.
5. **Compare against tolerances** (`measured-evidence.md`), not against convention. Midpoint outside
   47–55% is a loud flag. A first-act break is worth noting outside 10–38% and otherwise worth a
   question, not a note — ask what the placement buys before calling it wrong.
6. **Run the fault catalogue** in `diagnostics.md` and the genre-contract pass.
7. **Report** per the format in `audit-procedure.md`.

## Mode: Audit (against a spec)

Everything in Diagnose, plus the comparison that is the point: for every beat in the spec, `Target`
versus `Actual`, with the variance and a verdict. Then the two questions the writer needs answered —
**where did the draft drift from the plan, and is the drift an improvement?** Drift is not
automatically failure; drafts discover things. Separate unlicensed drift (the plan was better, the
draft lost it) from licensed evolution (the draft found something the plan did not know), and for
the latter propose the spec amendment rather than a note telling them to go back.

Update the spec's `Status` column as evidence permits: `drafted` where written but not assessed,
`working` where it holds, `broken` where it fails. Never touch the Decisions log — that belongs to
story-structure and to the writer.

## Mode: Judge

Score against five dimensions, each with findings rather than a number alone: spine integrity (do
the five beats exist and land), placement (measured against tolerances), causality
("therefore/but" versus "and then"), storyline architecture (braiding, convergence, whether every
thread earns its pages), and contract (genre obligations, format requirements, act-out craft for
TV). Use the full report shape in `audit-procedure.md` §7 — all of its sections, including "what is
working", which is never omitted — with the findings section ordered P0 (breaks the script), P1
(costs it), P2 (worth considering). Prioritization orders the findings; it does not licence dropping
the rest of the report. Each finding carries a page citation, the evidence, and a fix *direction*
rather than a rewrite.

Scores are attribution devices; the findings are the deliverable. Never claim a script "fails" a
framework — say which framework it is closest to and where it departs, since departures are often
the reason a script is good.

**Orchestrator note:** to audit a structure this same session designed, run in a fresh context
(subagent) given only the draft, the spec, and this skill. Same-context self-grading is warm-engine
bias.

## Mode: Compare

Full procedure in `audit-procedure.md` §10, including the figures-only path — writers invoke this
mode with numbers rather than a script ("44 pages, cold open 6pp, Act One 18pp…"), which is a
legitimate input and needs no pages.

Pick the two or three most instructive maps from `../../structure-library/INDEX.md` — matched on format,
genre, or the specific problem — and put the user's measured figures beside theirs in one table.
Then the analysis that matters: not "yours is different" but *what the produced script bought with
its choice, and whether yours is buying anything.* A 34% first act is not a fault; a 34% first act
that is only setup is. Erin Brockovich, When Harry Met Sally and Dune all run long first acts and
all pay for them by running complete small stories in the space.

## The rules that outrank a tidy verdict

- Measure first, judge second. An audit whose findings are not page-cited is an opinion. (Outlines
  have no pages: run `audit-procedure.md` §9 and cite beat indices instead. Say plainly which checks
  an outline cannot support — the 8-point midpoint band is one of them.)
- ABSENT is a finding. Never round a missing beat to the nearest scene.
- Placement is not function. A beat at exactly 50% that changes nothing is INERT, and an inert
  midpoint is a P0 whatever the percentage says. Run the functional tests in `diagnostics.md` §1.0
  on every load-bearing beat, including the ones that measured clean.
- Tolerances are evidence, not law, and convention is neither. Never flag a first-act break merely
  for missing 25% — 8 of 18 measured features do, and several are canonical.
- Ask what a deviation buys before calling it a fault. The best scripts in the corpus deviate most.
- Distinguish a structure problem from a want problem. Scenes where nobody wants anything read as
  structural sag and are not fixed by moving beats.
- Distinguish a structure problem from an execution problem. Correct beats can be inertly written;
  say so and route to the dialogue and action skills rather than prescribing more structure.
- No rewriting in audit modes. Fix direction, not fixed text.
- One page ≈ one minute. Percentages are of the script's own measured length, never of a nominal 120.
