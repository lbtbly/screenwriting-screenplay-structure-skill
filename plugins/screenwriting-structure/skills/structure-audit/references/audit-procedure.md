# The Audit Procedure — Measure, Compare, Report

Operational reference for Claude. Every mode in `SKILL.md` routes here. Run the passes in order; never
let a later pass start before the earlier one has produced numbers, because the whole value of this
skill is that measurement precedes judgement. Never rewrite anything in any pass.

| # | Pass | Output it must produce before the next pass starts |
|---|---|---|
| 1 | Measurement | Denominator + offset, scene inventory, act boundaries |
| 2 | Five-beat sweep | Five rows, each a page + % with its verdict, or the word ABSENT |
| 3 | Tolerance comparison | A severity per row, after the "what does it buy?" interrogation |
| 4 | Storyline | Thread table with page ranges, beat counts, convergence pages |
| 5 | Causality | One connector between every consecutive scene pair |
| 6 | Format-specific | Act grid / pilot audit / sequence audit as the format demands |
| 7 | Report | The fixed deliverable shape in §7 |
| 8 | Spec comparison | Only when a `structure.md` exists — target vs actual, drift analysis |
| 9 | Outline mode | **Replaces passes 1–7 when the input has no pages** — beat-numbered, adapted report |
| 10 | Compare mode | Two or three named maps, one table of the user's figures beside theirs, and a purchase verdict per deviation |

## 1. The measurement pass

### 1.0 Run the extractor first — do not start with greps

```bash
python3 ../assets/extract-structure.py SCRIPT.pdf     # or a .txt already made with pdftotext -layout
python3 ../assets/extract-structure.py SCRIPT.pdf --scenes   # every heading, no truncation
python3 ../assets/extract-structure.py SCRIPT.pdf --json     # machine-readable
```

It returns everything §§1.1–1.3 ask for in one pass: physical pages, printed numbering, the offset
and every point it drifts, A-pages, doubled printed numbers, scene headings with printed positions,
scene count, average and longest scene, and printed act labels. **Exit codes: 0 measured · 2 no text
layer · 3 unreadable.** Read the numbers back into the report; do not re-derive them by hand.

#### The confidence block — report it, do not consume it silently

Every figure the script emits says how it was obtained. This is the difference between a measurement
and a guess wearing a measurement's clothes, and it is the whole point of §1.

```
-- CONFIDENCE -------------------------------------------------------
Numbers read from      header (first 3 non-blank lines of each page)
Page numbers asserted  101   (read + interpolated + back-extrapolated)
  READ off the page    100   (99.0%)   <- MEASURED
  INFERRED             1   (1.0%)   <- NOT MEASURED   [0 interpolated, 1 back-extrapolated]
NUMBERING CONFIDENCE   HIGH   (threshold: high >= 90.0% read, medium >= 60.0%, low below that)
```

| Field | What it means |
|---|---|
| `READ off the page` | the page number was read from that page's own header or footer. **Measured.** |
| `INFERRED — interpolated` | both neighbours were read and the gap filled arithmetically |
| `INFERRED — back-extrapolated` | before the first read number; page 1 is conventionally unnumbered |
| `NUMBERING CONFIDENCE` | `high` ≥90% read · `medium` ≥60% · `low` <60% |
| `Printed body pages` + `basis` | always the **last directly read** printed number. Never extrapolated |
| `Trailing unnumbered` | sheets after the last read number, reported as unnumbered and **never renumbered** |
| `Numbers read from` | header, or `header + FOOTER` on a script that paginates at the foot |

**Rules, all of them mandatory.**

1. **State the confidence in the report whenever it is not `high`.** Quote the `!! WARNING` lines
   into §7's Assumptions section verbatim rather than deleting them. A medium- or low-confidence
   denominator makes every percentage in the report an estimate, and the reader is entitled to know
   which kind of number they are reading. When Harry Met Sally measures 84 of 136 page numbers
   (61.8%, `medium`) — that is a fact about the audit, not a detail.
2. **Never promote a `~`-prefixed page label into a citation.** In the scene and act lists `~57`
   means the label was inferred and `—` means the sheet is unnumbered. Only an unprefixed label was
   read off the page. Cite `p.57` only where the script printed `57`.
3. **`Trailing unnumbered` pages are not extra script pages.** Parasite's PDF p.144 is a NEON
   advertisement; the script's last printed page is 141. Do not add trailing sheets to the
   denominator, and do not assume they are blank either — say what they are or say you did not look.
4. **`NO PRINTED PAGE NUMBERS ANYWHERE` sends you to §1.1 rule 6**, not to a denominator of your own
   invention.
5. **A `low` confidence result is a finding about the file, not a licence to proceed quietly.** Widen
   every tolerance band before assigning a severity, and consider whether the file needs re-OCR.

In `--json` the same information is at `numbering.confidence` (including `thresholds_pct_read`),
`numbering.printed_body_pages_basis`, `numbering.trailing_unnumbered_pages`,
`scenes.average_length_basis`, per-heading `printed_basis`, and the top-level `warnings` list.

**Why not greps.** `pdftotext` writes a form feed (`\f`) immediately before the first character of
every page, and on most screenplays that first character *is* the page number. A line-anchored
pattern therefore never matches it — `^` sits before the form feed, not after it. On When Harry Met
Sally the old `grep -nE '^[ \t]*[0-9]+[A-Z]?\.?[ \t]*$'` returns 2 hits across 137 pages, both false;
the script returns 83 real ones. The obvious repair also fails: `[\f \t]` inside a POSIX bracket
expression matches a literal `f`, not a form feed. **Any manual pass must therefore pipe through
`tr '\f' '\n'` first, or split on `\f` in a script.** Nothing else works.

**If the script reports no text layer, stop.** A scanned PDF (The Big Bang Theory pilot: 52 pages,
0 extractable characters, CCITT page images) yields no measurement at all. Run OCR
(`ocrmypdf --force-ocr in.pdf out.pdf`) and re-run, or measure by hand and say so in §7's
Assumptions. Never report figures derived from an empty text layer — the physical page count is the
only trustworthy number on such a file.

**If there are no pages at all** — an outline, a beat sheet, a treatment — go to §9 now. §§1–7
assume pages and their report format demands citations an outline cannot supply.

### 1.1 Establish the denominator — PRINTED pages, always

Every percentage is computed against this number; get it wrong and every finding is wrong with it.

**The denominator is PRINTED body pages.** Not physical pages, not PDF pages. Every beat map in
`../../../structure-library/`, and every tolerance band in `measured-evidence.md`, was measured against
printed numbering. A percentage computed against a different denominator than the band it is compared
to is not a measurement, it is a category error — on When Harry Met Sally the two denominators are
122 and 137, a 12% gap, which is wider than most of the bands in §3. **State the denominator in the
headline verdict and use it for every percentage in the report.**

1. **Convert with layout preserved** — `pdftotext -layout`. Without it the right-margin page numbers
   and scene numbers merge into body text and the offset becomes unrecoverable.
2. **Harvest the printed numbering.** The script does this. Manual fallback, which genuinely runs:

   ```bash
   pdftotext -layout SCRIPT.pdf - | python3 -c '
   import re,sys
   for i,pg in enumerate(sys.stdin.read().split("\f"),1):
       for ln in [l for l in pg.split("\n") if l.strip()][:3]:
           m=re.search(r"(?:^\s*|\s\s+|[pP][.,\"’\s]{1,4})(\d{1,3}\s?[A-Za-z]?)\s*[.,\"’]?\s*$",ln)
           if m: print(f"PDF {i} = printed {m.group(1).strip()}"); break'
   ```

   It reads three lines per page because the number is not always first, and it accepts the number
   three ways: as the whole line, as the *trailing token* of a line — network drafts print a running
   header (`THE ROOKIE - Ep. 101 - "PILOT" - Revised Network Draft - 1/21/18    47`) and the number
   is the last thing on it — and after an explicit **page label**. That third form is the one a
   `\s\s+` tail pattern cannot see, because only a single space separates the label from the number:
   Mulan prints `MULAN EIGHTH DRAFT   12/21/96   p. 2.` and a two-space rule reads **3** of its 104
   pages. Verified yields with the pattern above: **101** on Mulan (3 without the label branch), 118
   on When Harry Met Sally, 105 on Lady Bird, 59 on The Rookie.

   **The one-liner over-counts and the script does not.** It takes the first thing on a page that
   looks like a number; it does not check that the sequence increases with the sheets. On When Harry
   Met Sally that is 118 raw hits against 84 the script accepts after reconciliation — the remainder
   are dates, scene numbers and OCR debris. Use the one-liner to see *whether* a script paginates and
   in what format; use the script for the count. And if a script paginates at the **foot** of the
   page (Only Murders in the Building), a header-only scan reads zero — the script retries the footer
   zone automatically and says so on its `Numbers read from` line.
3. **Compute the offset and verify it three times** — first body page, a middle page, the last page.
   Never assume it is constant. State it in this exact form:
   `Offset: PDF page N = printed page N−1.` Where it drifts, state every segment. The Rookie holds a
   single offset across all 60 body pages; When Harry Met Sally drifts nine times, PDF−1 to PDF−15.
4. **Exclude from the denominator** title page, cast/sets lists, epigraph pages, blank pages, and
   back matter after `END OF EPISODE` / `FADE OUT`. The denominator is body pages only. Page 1 is
   conventionally unnumbered — the first *printed* number is usually 2, and a script whose numbering
   starts at 2 has not lost a page.

   **The last printed page is the last one that prints a number — never one page further.** Sheets
   after it are unnumbered until you have looked at them and said what they are. Parasite's PDF
   p.144 is a NEON awards advertisement, so the script is 141 printed pages, not 142; Lady Bird's
   numbering is legible to p.103 and the last seven sheets carry none, so 103 is what was *measured*
   and 110 is what the beat map *extrapolates* — a distinction the beat map states out loud and the
   audit must too. The extractor reports these as `Trailing unnumbered` and refuses to renumber
   them; if you carry the extrapolation into the report anyway, label it as an extrapolation.
5. **A-pages and doubled numbers are the same phenomenon: printed numbering lagging physical pages.**
   A revised draft runs 12, 12A, 12B, 13, so printed 13 is the fourteenth sheet. Lady Bird instead
   prints `30.` on two consecutive sheets, then `50.` twice, then `70.` twice — three unnumbered
   inserts, and the reason its offset walks from PDF−2 to PDF−5 across 115 sheets. **In both cases
   cite locations by printed number and compute percentages against printed pages,** then state both
   counts once so the reader can see the gap: `122 printed pp (137 physical; 4 A-pages, offset drifts
   9 times)`. Never mix: a beat cited at printed p.61 must be scored as 61 ÷ printed length.
6. **No printed numbers at all** (retyped transcripts — Erin Brockovich is the corpus example).
   Then, and only then, the denominator is PDF pages. Say so in the headline verdict, mark every
   percentage approximate, and widen every tolerance band by ±3 points before assigning a severity:
   transcript page breaks fall mid-sentence and run long against standard pages, so the error is
   systematic and one-directional. Do not silently substitute physical pages on a script that *does*
   print numbers — that is the error this section exists to prevent.
7. **Multi-cam pages are double-spaced.** Convert at ≈1.9–2.4 pp/min before saying anything about
   runtime; never compare a multi-cam page count to a single-cam band. If the writer's stated count
   disagrees with your measurement, use yours and say so.

### 1.2 Scene inventory

The script emits the whole inventory (`--scenes`). What follows is what it is doing, and the manual
fallback when it is unavailable. **All three forms must be checked — a script that returns nothing
on form one is usually a numbered shooting script, not a script without scenes.**

1. **Plain sluglines.** The common case, and all that Lady Bird (124 headings) or The Rookie (86)
   require. Note the `tr` — without it the first slugline of every page is invisible:

   ```bash
   pdftotext -layout SCRIPT.pdf - | tr '\f' '\n' \
     | grep -nE '^[[:space:]]*(INT|EXT|I/E|INT\.?/EXT|EXT\.?/INT)[.,: ]'
   ```

2. **Numbered shooting scripts.** In a numbered draft the slugline begins with a *scene number*, not
   `INT.`, and the number is repeated in the right margin: `23   INT. SHAKESPEARE & CO. - DAY   23`.
   Form one returns **1 hit** on When Harry Met Sally for exactly this reason. Match the number:

   ```bash
   pdftotext -layout SCRIPT.pdf - | tr '\f' '\n' \
     | grep -nE '^[[:space:]]{0,40}[0-9]{1,3}[A-Za-z]{0,2}[.)]?[[:space:]]{1,8}[A-Z]' \
     | grep -viE 'CONT|OMIT'
   ```

   **The gap is the discriminator, not the indent.** `pdftotext` may indent the whole block 25
   columns, so an indent ceiling throws away real sluglines; but the scene number is repeated beside
   *continuation* lines too, including character cues —
   `20                    ALICE                    20`. A slugline body follows its number by one to
   eight spaces; a cue sits 20–40 columns away. Second net: **scene numbers only ever increase.** A
   line whose number is not greater than every number already accepted is a continuation artefact,
   not a scene. Exclude `OMITTED` scenes (`22 OMIT`) from the count and say how many there were.
3. **OCR corruption.** Scanned drafts mangle the one token the detector depends on. Real corpus
   mutations of `INT.`/`EXT.` on When Harry Met Sally: `Err.` `E:XT.` `UT.` `Erl'.` `Ilff.` `IN'l'.`
   `IN'r.` `IN'!'.` `rNT.` `INT,` `EXT,` `E.XT.` — and `CONTINUED:` arrives as `CONTIHUED:`,
   `CON'l'INUED:`, `CONTINtJED1`, so an exact-match exclusion silently readmits them as scenes.

   ```bash
   pdftotext -layout SCRIPT.pdf - | tr '\f' '\n' \
     | grep -nE "^[[:space:]]{0,40}([0-9]{1,3}[A-Za-z]{0,2}[.)]?[[:space:]]{1,8})?[EIUR][^[:space:]]{0,5}[.,:][[:space:]]+[A-Z]" \
     | grep -E '[A-Z]{4,}' | grep -viE 'CONT|OMIT'
   ```

   The trailing `[A-Z]{4,}` is load-bearing: without it the pattern also takes dialogue
   (`Really,   Marie.`). With it, 80 lines on When Harry Met Sally and no dialogue among them.
   **Never report a scene count from a corrupted source as a total.** Report it as a floor, with the
   scene numbers you could not recover: the script recovers 116 headings spanning a sequence that
   runs to 140, and says so.
4. Record scene count, average scene length (**printed** body pages ÷ scenes), longest scene, and the
   longest stretch of pages with no scene change. Measured here: The Rookie 86 scenes / 0.70 pp
   average, Lady Bird 124 / 0.89, When Harry Met Sally ≥116 / ≤1.05.
5. Flag for later, never as findings on their own: a feature average over ~3 pp (Field's ceiling is
   4 pp, dialogue scenes 2–3); any scene over 6 pp; a run of sub-eighth-page headings, usually a
   montage the parser has shredded — check `MONTAGE`, `INTERCUT`, `SERIES OF SHOTS`.
6. The 40–60-scene feature range describes the corpus; it is not a target. Lady Bird runs 124 and
   Field's ceiling is irrelevant to it. Never report scene count as a fault — it locates density, it
   does not score.
7. Harvest structural punctuation for §1.3 (again through `tr`):
   `tr '\f' '\n' | grep -nE '(CUT TO:|SMASH CUT|MATCH CUT|DISSOLVE TO:|FADE (OUT|TO BLACK)|MONTAGE|INTERCUT|SUPER:|TITLE:|CHYRON)'`.

### 1.3 Act boundaries

**When they are printed.** The script lists them with printed pages. Manual fallback — and note that
the first act label of a script sits at the very top of its own page, so *this is the pattern the
form feed breaks most often*: without `tr`, `ACT ONE` on The Rookie is invisible and the grid comes
out one act short.

```bash
pdftotext -layout SCRIPT.pdf - | tr '\f' '\n' \
  | grep -nE '^[[:space:]]*(TEASER|COLD OPEN|PROLOGUE|TAG|ACT [A-Z0-9]+|PART [A-Z0-9]+|END OF [A-Z]+([[:space:]]+[A-Z]+)?)[[:space:]]*\*?[[:space:]]*$'
```

The trailing `\*?` matters on production drafts: `END OF ACT FOUR` carries a revision asterisk in the
right margin and a length-limited or `$`-anchored pattern drops it. Verified on The Rookie: all ten
labels, `ACT ONE` through `END OF EPISODE`. Beware bare `PILOT`, `SHOW` and `EPISODE` — they are act
labels only in `END OF …` form; standing alone they are character cues, and The Rookie has one.

Build the grid directly from the labels: act, printed pages, length, % of script, cumulative %.
Report the act-out page as the last page of the act, not the first page of the next.

**When they are not printed.** Infer, and mark every inferred boundary `[inferred]` — never present
an inference as a printed fact. Infer, in this order of reliability, from: (1) the five-beat sweep —
commitment closes act one, collapse closes act two, so the beats locate the boundaries and not the
reverse; (2) a hard time or place discontinuity coinciding with a valence flip — a chyron, a music
cue, a `SUPER:`; (3) sparingly used punctuation — six `CUT TO:`s in fifty-four pages marks something
each time; (4) the regularity test — This Is Us prints nothing, inferred acts 8.5/9/10/9/8.3/8.1 pp.

**Never infer a fault from the absence of printed act breaks, or soundness from their presence.**
Severance prints four acts on a commercial-free show; This Is Us prints none on a network hour.

### 1.4 Locating a beat that carries no label

Scripts do not announce their turns. Use all four; require two to agree before recording a page.

1. **Window first.** Compute the page window from the measured band before reading — midpoint 47–55%
   of measured length (a 110-page script: pp.52–61). Widen only after the window fails.
2. **Vocabulary harvest, as candidates only.** Commitment:
   `grep -niE "\b(I'm in|I'll do it|deal|we have a deal|I quit|resign|sign(ed)? (the|this|it)|no going back|last chance|find out)\b"`.
   Collapse: isolation and stillness — a character alone, an unanswered phone, a funeral, a
   departure. A grep hit is never the evidence; it is where you start reading.
3. **The state-change test.** A beat is where the answer to a standing question changes. Write one
   line for the state before the candidate and one for after — who wants what, from whom, by what
   tactic. If both lines are the same sentence, it is not a beat however large it is.
4. **The downstream test — decisive.** Mentally delete the candidate. If the next twenty pages still
   play without rewriting, it is not load-bearing. A real turn is inherited by everything after it.

**What a midpoint looks like on the page.** Not the biggest scene: the scene after which the
protagonist's *tactics* change. Three signatures measured in the corpus — the goal is enlarged and
the climax's terms stated aloud ("if, and only if, you find me the evidence"); an apparent victory
that is a defeat or the reverse; a reveal that *voids* the pursuit rather than escalating it
(Parasite's p.71, which a three-act pass mislabels as a complication).

## 2. The five-beat sweep

Locate all five; give each a printed page (or range) and a % of measured length — which per §1.1 is
always printed body pages, the same denominator the §3 bands were measured against. This is the spine.

| Beat | Function it must perform | Evidence that confirms it | The near-miss that gets mistaken for it |
|---|---|---|---|
| **Disturbance** | Something arrives from outside the protagonist's control and makes the ordinary world unavailable | A scene the protagonist did not initiate whose consequences persist past the next scene | An atmospheric bad day; backstory announced in dialogue; a threat that is retracted; the opening image |
| **Commitment** | The protagonist *chooses*, after resistance, and cannot cheaply return; the dramatic question forms here | A cost paid to enter (money, job, relationship, a lie told), a retreat closed, and every following scene inheriting the choice | Agreement with no cost; a decision made *for* the protagonist by someone else; instant acceptance with no debate phase, which reads as staged |
| **Midpoint reversal** | The middle flips: goal upgraded, voided or re-described; reactive becomes proactive | Tactics change after it; stakes restated at a new scale; frequently the climax's terms spoken aloud | The largest set piece; a complication that escalates without reframing; whatever scene sits at the literal page centre |
| **Collapse** | The plan fails at maximum personal cost; support is stripped; old and new ways both fail | A loss the protagonist cannot undo, isolation staged physically, a whiff of death | A setback solved within two pages; a sad scene with no strategic consequence; an antagonist win that costs the protagonist nothing personal |
| **Proof** | The crisis choice enacted through action under maximum cost; answers the dramatic question | The protagonist does what was established as impossible or refused earlier; a stated setup is paid; external and internal reverse in the same action | The loudest action sequence; an outcome delivered by coincidence or offscreen; a resolution that only *reports* the result |

**Three sweep rules.** (1) **The protagonist need not perform the physical act** — The Rookie's hero
disarms himself and is used as bait; another character fires. The test is whether the protagonist's
*choice* causes the outcome. (2) **A split beat is a legitimate reading:** Erin Brockovich turns the
situation at ~10%, delivers the problem at ~14%, and does not ask the dramatic question until ~36% —
record every component with its page rather than picking one. (3) **A relocated beat is a placement
finding, not a presence finding:** Erin Brockovich runs a full dark night at 29–33%, *before* the act
break. Record where it is; never record it missing.

### 2.1 Recording ABSENT

ABSENT is the most valuable result this skill produces. Protect it.

1. **Never round a missing beat to the nearest scene.** Filling the slot converts the audit's best
   finding into false reassurance, and it is the most common way audits fail.
2. **Three tied candidates is evidence of absence, not abundance.** Name all three, state that
   deleting any of them requires no downstream change, record ABSENT.
3. Keep four verdicts distinct. **ABSENT** — performed nowhere; no page, do not write one.
   **UNPLACEABLE** — performed, but spread across a run of scenes with no single hinge; record the
   range. **RELOCATED** — performed outside the expected window; record the actual page, and the
   finding is placement, not presence. **INERT** — present, inside its band, and failing its
   functional test; record the page and price it as ABSENT. The first three are verdicts about
   *where* the beat is; INERT is the verdict about whether it does anything, and it is the one this
   pass will otherwise miss, because a beat at 50% that changes nothing downstream reads as on-plan.
   Run the five functional tests in `diagnostics.md` §1.0 before writing any verdict in this column.
4. **ABSENT can be the correct reading of a good script.** Oppenheimer's map names no midpoint at all.
   Say "no locatable midpoint," give the reason you can see, and do not manufacture one.
5. Severity: an ABSENT commitment, midpoint or proof is **P0**; an ABSENT disturbance or collapse is
   **P0** if the spine fails without it, **P1** if the function is carried elsewhere. **INERT takes
   the same severities as ABSENT** — an inert midpoint is P0 whatever its percentage, because the
   back half inherits nothing and every downstream finding is a symptom of it.

## 3. The tolerance comparison

Convert measurements into severities using `../../story-structure/references/measured-evidence.md` §6.
Nothing here compares the script to convention. **Procedure:** (1) express each located beat as page
+ % of measured length; (2) look up the measured band and its `n`; (3) take the severity from that
file — `error` / `warn` / `note`; (4) run §3.1; (5) only then map to a report priority.

| Measured-evidence severity | Report priority | Condition |
|---|---|---|
| `error` | **P0** | The beat is ABSENT, or the deviation compounds with a causality or storyline failure |
| `error` | **P1** | The beat is present and located but far outside the band, with no purchase named |
| `warn` | **P1** | Outside the band *and* the interrogation found no purchase |
| `warn` | — | Inside the band **and passing its functional test**: there is no finding. Do not report it. |
| `note` | **P2** | Mention only if it bears on another finding or the writer asked |
| *(verdict `INERT`, §2.1)* | **P0 / P1** | Present and in-band but failing its functional test (`diagnostics.md` §1.0). Priced as ABSENT — P0 for commitment, midpoint or proof; P0/P1 for disturbance or collapse. **This row overrides the placement rows**, which cannot see the fault |

**Operating rules. Apply in this order and do not reorder them.**

1. **Midpoint outside 47–55% → loud flag, stated first.** This is the one placement the corpus
   agrees on (14 of 17 locatable midpoints; full range 45–67%).
2. **A first-act break inside 10–38% produces no finding.** That band is the measured corpus end to
   end. Outside it, warn gently and only after the interrogation.
3. **Never flag a first-act break merely for missing 25%.** Only 10 of 18 measured features sit in
   19–25%, and several that miss it are canonical.
4. **Beats with no measured band** — disturbance, collapse, proof — are checked for *presence*, not
   placement. Position alone is not a finding; severity is `note`.
5. **Use measured length bands, not conventions.** Single-cam half-hour is 30–39 pp, not 25–34.
   Cite the sample size whenever n ≤ 3.
6. **Never flag** the absence of printed act breaks, an act-out for lacking a cliffhanger, or an act
   for being long without first asking what work the length does.
7. **Never accept a beat's label as its placement** — including in this plugin's own beat maps, eight
   of which call a beat "dead centre" that their own percentages place elsewhere. Recompute.
8. **Never accept a beat's placement as its function.** Before mapping any in-band row to "no
   finding", run that beat's functional test (`diagnostics.md` §1.0). Placement is the only property
   the corpus measures, so this table is blind to a beat that sits at 50% and changes nothing; an
   INERT verdict is priced by function and outranks every placement row above.

### 3.1 The "what does it buy?" interrogation

Run this before any deviation is written up as a fault. All four questions, with page cites.

1. **What does the deviation purchase?** Name the thing on the page. For a long first act: does the
   pre-break material run a *complete* small story — its own question, crisis and answer — or is it
   only setup? For an early break: what is the undirected stretch *for*?
2. **Is the purchase delivered, and where?** One page citation. "It builds character" is not a
   delivery; a scene is.
3. **What would be lost by normalising it?** If nothing, the deviation is inert and the fault stands.
4. **Is there a produced precedent, and does this script pay the same price?** Look it up in
   `../../../structure-library/INDEX.md`. Precedent without the same payment is no defence — "Juno did
   it" only holds if the catalyst is front-loaded the way Juno's is.

**Decision rule.** Q1 and Q2 answered with page cites → not a fault; move it to "what is working" or
to open questions. Q1 unanswerable → a fault, reported at the band's severity. The best scripts in
the corpus deviate most, so a deviation you cannot price is a question, not a verdict.

## 4. The storyline pass

1. **Assign every scene one dominant thread** — A, B, C, or ensemble. Ensemble scenes are counted
   separately, never split across threads.
2. **Build the table:** thread · whose · what it is · page range · scene count · page equivalents ·
   % of the script · beat count · converges with A at p.__ . Then run all six tests.

| Test | Pass condition | Failure is |
|---|---|---|
| **Convergence** | Every thread rejoins the A-story before the climax; name the page | A thread that never rejoins — a defect, P1 minimum |
| **Beat-count floor** | ≥ 3 beats | Fewer than 3 is a runner, not a storyline. Either name it a runner in the report or say it needs growing — do not score it as a failed thread |
| **Thematic load** | The B story states or tests the central dramatic argument in different terms from A | A B story that is only "the love story" with no argument attached — the theme has nowhere to be tested |
| **Braid vs parallel** | Cutting the thread breaks the A-story's schedule | If it cuts clean, it is parallel, not braided. Say which. George in Erin Brockovich is childcare before he is a boyfriend, so his exit is a logistics crisis |
| **Rotation** | No thread disappears for so long it needs re-introducing on return | Measure the longest gap in pages; a thread absent for more than ~15% of the script and then re-explained is the finding |
| **Format ratio** | Beat counts near the format spec in `../../story-structure/references/formats.md` | Report the gap, not a verdict — The Rookie's C-track survives on 6 beats and ~6.5% and its map names that as the honest cost of three-hander structure |

3. **Name the thinnest thread** and say whether its thinness is designed or accidental — the test is
   whether its flaw is legible in a single image.

## 5. The causality pass

The Parker/Stone rule, run as a procedure rather than quoted as an aphorism.

1. **Build the scene list** from §1.2 — one line per scene: page, who wants what from whom, what
   changes by the end of it. **Write exactly one connector between every consecutive pair:**
   THEREFORE, BUT, or AND THEN. Never sample — clusters are the finding and sampling hides them.
2. **Map the AND THENs onto the page axis.** Report clusters and page ranges, never a total: a total
   is a score, a cluster is a location the writer can open the file to.
3. **Thresholds.** An isolated AND THEN at an act or sequence boundary is normal — a new movement is
   starting. Three consecutive is a sag. A run spanning more than ~10% of the script is P1, or P0 if
   it overlaps an ABSENT midpoint.
4. **The failure signature.** For each scene ask: *which later scene breaks if I cut this one?* Name
   it. If nothing breaks, the connector into that scene is AND THEN however good the scene is — a
   scene that can be moved anywhere is a scene caused by nothing.
5. **Separate the two lookalikes before reporting.** If the connector fails because nobody in the
   scene wants anything, the fault is a *want* problem and moving beats will not fix it. If the beats
   are causally sound and the pages are still inert, the fault is *execution* — say so and route to
   the dialogue and action skills rather than prescribing more structure.
6. **Report a run as three citations:** the page range, the last causally-linked beat before it, and
   the first scene after it that is caused by something. That is the whole finding.

## 6. Format-specific passes

Specifications live in `../../story-structure/references/formats.md`; run them from there.

**6.1 TV act grid and act-out audit.** Build the grid from §1.3 — act, pages, length, %, cumulative %,
what turns, the act-out, the button type (formats.md §4.1). For each act-out record: page, %,
button type, the question left open across the break, and how the next act opens (resolves
immediately / delays / no cutaway). Then four tests. (a) Does any act resolve its own question in the
first lines of the next *without* replacing it with new material? That, not the act-out, is the
fault. (b) Are all buttons the same type? Four identical cliffhangers exhaust an audience; rotation
is craft. (c) Judge each button by what it *reveals*, not by what it leaves unresolved — measured
act-outs are often transgression or stillness rather than jeopardy. (d) Compare act lengths to the
grids in formats.md §2.2–2.7 and ask what a long act is doing, never whether it is long.

**6.2 Pilot audit.** Run every row of formats.md §3.2 with a page citation and a judgement of
efficiency; a row with no page is the finding. Then the series-engine tests (§3.3) and the pilot type
(§3.1). Name the page that installs the engine; if there is none, say the show is a closed-ended
story. Where a row is deliberately unsettled — a question standing where a protagonist should be, a
hero who never states a want — say what substitutes for it rather than scoring it missing.

**6.3 Feature sequence audit.** Divide into eight sequences of ~12–15 pp and name, for each, its own
dramatic question, its mini-goal, its partial resolution, and the dangling cause it throws into the
next. **A sequence with no question of its own is where the sag is**, and the finding is that
sequence's page range. Cross-check set-piece spacing and the obligatory-scene pass in
`../../story-structure/references/genre-contracts.md`.

## 7. The report

Fixed order. Do not reorder, do not omit a section, do not open with an opinion.

**1 — Headline verdict.** One paragraph, six sentences maximum, no bullets, containing: format,
measured length and the denominator/offset statement; the framework the draft is closest to; the
state of the five-beat spine in one clause; the single most consequential finding. Never say a script
"fails" a framework — say which it is closest to and where it departs, since departures are often the
reason a script is good.

**2 — The measurement table.** Every row page-cited; ABSENT rows carry the word ABSENT and no page.
Append the act grid (TV), the storyline table and the scene statistics as separate tables below it.

| Beat | Target (source) | Actual | Variance | Verdict |
|---|---|---|---|---|
| Midpoint reversal | 47–55% [measured, n=17] | p.61 / 55% | +0 pts | on-plan |
| Commitment | 10–38% [measured, n=18] | p.9 / 8% | −2 pts | drifted — early |
| Collapse | ~75% [convention] | ABSENT | — | broken |
| Disturbance | ~10–12% [not measured] | p.12 / 11% | in band | **INERT** — in place, changes nothing |

**3 — Findings, prioritized.** P0 breaks the script · P1 costs it · P2 is worth considering. Each
carries an ID, a one-line claim, the evidence with page citations, the downstream consequence, a fix
*direction* (never fixed text), and your confidence.

**4 — What is working.** Never omit this section and never let it run shorter than three page-cited
items. Include at least one deviation a template-following audit would have flagged and you are
deliberately not flagging, with the reason it is paid for. This is not politeness — it is what stops
a writer cutting the load-bearing thing.

**5 — Open questions for the writer.** Deviations whose purchase you could not determine, ambiguities
of intent, and any assumption you made about format, length or genre. Batch as one set; do not drip.

**6 — Assumptions and limits.** Unattended runs: state what you assumed and any pages you could not
read. Always: percentages are of this script's measured length in **printed** pages (§1.1), never of
a nominal 120 and never of the physical sheet count.

### 7.1 A well-formed finding versus a badly-formed one

**Badly formed** — no page, no measurement, the symptom restated as the diagnosis, a prescription
that is not an action, and it could be pasted onto any script ever written:

> P1 — Act two sags. The middle of the script loses momentum and the stakes feel low. Consider
> strengthening the midpoint and raising the stakes.

**Well formed:**

> **P0 — No midpoint reversal (pp.48–66 / 43–59%).** Across the whole window no scene changes Nora's
> goal, information or posture: on p.47 she is asking Duvall for the ledger using flattery, and on
> p.66 she is asking Duvall for the ledger using flattery. Three candidates — the hospital visit
> (p.52), the car argument (p.58), the flashback (p.63) — and deleting any of them requires no change
> to the following twenty pages. **Consequence:** the back half inherits nothing, which is why
> pp.60–85 read as repetition rather than escalation and why the causality pass returns nine
> consecutive AND THENs across pp.58–74. **Fix direction:** the material exists — Duvall's conditional
> yes on p.79 states the terms the climax pays and arrives 18 pages late; moving that function forward
> is one option, promoting the p.58 argument into a goal change is another. Which depends on what you
> want the second half to be about. **Confidence:** high — tactic-repetition and deletion tests agree.

## 8. Auditing against a `structure.md` spec

Everything in §§1–7, plus the following. If this session designed the spec, run the audit in a fresh
context given only the draft, the spec and this skill — self-grading is warm-engine bias.

1. **Validate the spec before comparing to it.** Do `Target %` and `Target p.` agree with the stated
   target length? If the spec is internally inconsistent, say so in the headline verdict before
   comparing anything, or you inherit its errors.
2. **Build target-versus-actual** for the five-beat table and every beat-sheet row, with variance in
   both pages and percentage points. Verdict vocabulary is fixed: `on-plan` (inside tolerance) ·
   `drifted` (present, outside tolerance) · `absent` (planned, not findable on the page) ·
   `unplanned` (on the page, not in the spec).
3. **Classify every drifted / absent / unplanned row.** Drift is not failure; drafts discover things.

| Class | Test that establishes it | What the report does with it |
|---|---|---|
| **Unlicensed drift** | The spec named a function; the page performs it nowhere; nothing replaced it | Report as a finding at the beat's severity |
| **Licensed evolution** | The function *is* performed, by different material, and the new version pays a setup the plan did not have | Propose the spec amendment — the exact row rewritten in the spec's vocabulary. Never a note telling the writer to go back to plan |
| **Unresolved** | The page is compatible with both readings | Open questions, phrased so the writer can settle it in one line |

4. **Classify by function, not by label.** A beat renamed is not drift. A function unperformed is
   drift whatever it is called. Run the state-change and downstream tests from §1.4 before assigning
   a class.
5. **Write permissions — this is a hard boundary.**

| Spec field | Audit may write? |
|---|---|
| `Status` (five-beat table and beat sheet) | **Yes — the only field the audit writes.** |
| Everything else — `Target`, `Actual`, Premise, Beat sheet rows, Storylines, Act grid, Genre contract | No. Propose changes as a diff in the report; the writer or story-structure applies them |
| `Decisions` | **Never.** Do not add, edit, reword or supersede a Decision. That log belongs to story-structure and to the writer |

6. **`Status` assignment rules.** `drafted` — written, unassessed. `working` — located, in tolerance,
   proved load-bearing by the deletion test. `broken` — located but failing its function, or ABSENT.
   Never write `planned`; that is the designer's. **Never mark a row `working` on placement alone** —
   placement is the only property the corpus measures, and a script can be perfectly placed and dead.
   A target you disagree with is a *finding*, not an edit: say so, give the measured band and the
   `n`, and leave the cell alone.


## 9. Outline mode — auditing a document with no pages

An outline, beat sheet, treatment, step outline or card stack is a legitimate audit input — the input
contract in `SKILL.md` names all of them — but §§1–7 assume pages exist and §7 demands citations an
outline cannot supply. **Route here from §1.0 the moment the input has no pagination.** Never fake a
page number by dividing a beat count by a target length and calling the result p.47; a fabricated
citation is worse than an honest beat number, because the writer cannot check it.

### 9.1 The denominator becomes the beat sequence

**Total beats replaces printed pages as the denominator.** Number every beat 1..N in document order
before measuring anything, and print the numbers in your output so the writer and you are counting
the same items. Fix the unit first and say which you used — a "beat" is one outline entry, one card,
or one bulleted step, whichever the document is made of. Do not silently merge two bullets or split
one; the denominator has to be the writer's units, not yours.

Then compute each beat's position three ways and report the first:

1. **Position in sequence** — `(index − 0.5) ÷ N`. **This is the primary measure.** Measured against
   all 42 maps in `../../../structure-library/` (1,817 beats, median 41 beats per map, range 32–67), it
   predicts a beat's true page percentage with a **median error of 3.2 percentage points; 69% of
   beats land within 5 points, 90% within 8.8.**
2. **Cumulative word share** — words before the beat plus half its own, over total words. Secondary,
   and *worse* than counting: median error 4.4 points, only 55% within 5. Outline entries are written
   at wildly different densities, and a writer who describes their climax in one line has not made it
   shorter. Use it only as a cross-check, and when the two disagree by more than ~10 points say so —
   that disagreement is itself a finding about where the writer's attention is.
3. **Block proportion** — beats per act or section ÷ total beats, as a percentage. This is the figure
   that goes in the act grid, and it is the sturdiest number an outline yields.

### 9.2 What that precision does and does not license

A ±3-point median with a ±9-point tail is coarser than every band in §3. Act on it accordingly.

| Question | Answerable from an outline? | Why |
|---|---|---|
| Is a load-bearing beat **ABSENT**? | **Yes — fully.** This is what outline mode is *for* | Presence is a function question, not a placement question. §2's five-beat table, §2.1's three verdicts and the state-change and downstream tests from §1.4 all work verbatim on prose |
| Is the beat **grossly** misplaced? | **Yes** | A midpoint at beat 8 of 40 (19%) is early by 28 points — far outside any measurement error |
| Is the beat inside the 47–55% midpoint band? | **No.** Say so explicitly | The band is 8 points wide and the estimator's p90 error is 8.8. Report the position, name the band, and record `indeterminate — outline precision`. Do not convert it into a severity |
| First-act break inside 10–38%? | **Usually yes** | A 28-point band survives a 3-point estimator. This is the one placement test outline mode can run cleanly |
| **Causality** (§5) | **Yes — and it is the highest-value pass here** | THEREFORE / BUT / AND THEN needs only two consecutive beats and a stated want. Outlines hide AND THEN runs better than drafts do, because summary prose supplies connective tissue the scenes do not |
| **Storyline** (§4) | **Yes**, except page ranges | Thread assignment, beat counts, convergence points and rotation gaps all express in beat numbers. The beat-count floor of 3 is already a beat-count test |
| Act grid and act-outs (§6.1) | **Partly** | Act *proportions* yes; act *lengths* in pages no. Button type is assessable only where the outline states what closes the act |
| Scene count, average scene length, longest scene | **No.** Omit the row | An outline entry is not a scene. Never present beat count as scene count |
| Execution faults — inert scenes, flat want, dialogue | **No** | There are no pages. Say the audit could not reach them, and that a beat-sound outline can still produce a dead draft |
| Runtime, format length compliance | **No** | Route to story-structure to set a target length instead of scoring one |

**The rule that keeps this honest:** an outline audit reports *presence, order and proportion*. It
does not report placement to a resolution finer than about ten points, and it says so in §6 of the
report rather than leaving the reader to assume page-level rigour.

### 9.3 Two failure modes specific to outlines

1. **Density is not weight.** A beat with three sentences is not more load-bearing than a beat with
   six words. Run the §1.4 downstream test — delete the beat, ask whether the rest still plays — and
   let that, never the word count, decide what is load-bearing. Lady Bird's page-quarter payoff
   ("She opens it. She got in.") would be the shortest line in any outline of it.
2. **An outline can be causally perfect and structurally empty.** Summary prose narrates
   *consequence* by default — "and so she confronts him" reads as THEREFORE whether or not the pages
   would earn it. Before crediting a connector, require the outline to name **who wants what from
   whom** in the beat. Where it does not, the connector is unproven: record it as `AND THEN [want
   unstated]`, which is a different and more useful finding than a false THEREFORE.

### 9.4 The adapted report

Same six sections in the same order as §7, same prohibitions, three substitutions.

- **Every page citation becomes a beat citation:** `b.17/40 (42%)`, never `p.47`. Ranges are
  `b.17–19`. If the outline has its own section headings, cite those too — `b.17 "Act Two: the
  hospital"` — because that is what the writer will search for.
- **Section 1, headline verdict,** replaces the denominator/offset statement with the beat statement:
  *"Outline, 40 numbered beats, no pagination; percentages are positions in the beat sequence, ±3
  points, and are not compared to bands narrower than 10 points."* Also state the intended format and
  length if known, and that it is the writer's claim rather than a measurement.
- **Section 2, the measurement table,** loses its Variance column wherever the band is narrower than
  the estimator, and gains a Precision column:

| Beat | Target (source) | Actual | Verdict | Precision |
|---|---|---|---|---|
| Commitment | 10–38% [measured, n=18] | b.6/40 / 14% | on-plan | sufficient — band is 28 pts |
| Midpoint reversal | 47–55% [measured, n=17] | b.21/40 / 51% | indeterminate | insufficient — band is 8 pts, estimator ±9 |
| Collapse | ~75% [convention] | ABSENT | broken | n/a — presence, not placement |

- **Section 4, what is working,** and **section 3, findings,** are unchanged in form; the fix
  direction is often "this is a question for the pages" rather than a structural move, and saying so
  is not a hedge.
- **Section 6, assumptions and limits,** must carry two fixed sentences: the estimator's precision,
  and the fact that no execution-level fault can be found in a document with no scenes. **Offer the
  re-audit:** the same beats measured against pages once pages exist, which is the moment the
  midpoint row stops reading `indeterminate`.

## 10. Compare mode — the user's shape against produced maps

Compare is the one mode that can run without a script. Writers invoke it with numbers — *"my
multi-cam pilot is 44 pages, cold open 6pp, Act One 18pp, Act Two 16pp, tag 4pp"* — and the whole
value of the mode is that those five numbers are enough to find something, provided you compare the
right thing. **The failure mode is a survey**: five maps, a wall of figures, and the verdict "yours
is different." Different is not a finding. What the produced script *bought* is.

### 10.1 Figures-only input

**Do not refuse the job for want of a script, and do not ask for pages you do not need.** Validate,
declare, proceed — in that order.

1. **Check the arithmetic.** The parts must sum to the whole. 6 + 18 + 16 + 4 = 44 ✓. A shortfall is
   itself the first finding: name the unaccounted pages and ask what is in them (main titles, an
   act break the writer did not count, overlapping boundaries), because a writer who cannot account
   for their own page total usually cannot locate their act break either.
2. **Check the figures against the format band** in `../../story-structure/references/formats.md`
   §2.2–2.7 before comparing them to anything. A length outside the measured band is a finding that
   needs no corpus at all.
3. **Declare the numbers as claims, not measurements.** They are the writer's report of their own
   document. Say so once, in the headline, and never let a claimed figure acquire the authority of a
   measured one by sitting in the same table as one — tag the row's source.
4. **State what cannot be assessed, as a list, before the table.** Without pages there is no five-beat
   sweep, no placement percentage for any beat, no INERT verdict, no causality pass, no storyline
   table, and no execution-level finding of any kind. For multi-cam specifically, joke rhythm,
   punchline-out discipline, scene count and act-out craft are all invisible to a page count. Naming
   the missing checks is what keeps the comparison honest; a Compare that reads like a full audit is
   a worse deliverable than one that admits it is a shape check.
5. **Then run it.** Act architecture, act ratios and unit proportions are exactly the properties a
   page count *can* carry, and they are the properties this library measures best.

Offer the full audit at the end, once — not as a condition of doing this one.

### 10.2 Selecting the maps

**Format first, always.** A multi-cam is compared to multi-cams; nothing is learned by putting a
44-page multi-cam beside a 120-page feature, and the percentages actively mislead because a multi-cam
page runs about 30 seconds. Use the length table and the `Multi-cam` / format lines in
`../../../structure-library/INDEX.md` to get the format cohort, then narrow **on genre or on the
specific problem** — INDEX's by-structural-problem lookup exists for exactly this.

**Two or three maps. Never more, never one.** One map is an anecdote; a survey is a reading list. Two
or three is the smallest number that can show a *range*, and the range is what tells the writer
whether their figure is outside the corpus or merely at one end of it. Where the format cohort is
small enough to take whole — multi-cam is three — take it whole and say so, because then the range
is the corpus rather than a sample of it.

Name every map you picked and why, in one clause each. A map chosen without a stated reason reads as
the one you happened to remember.

### 10.3 The comparison table

One table. Rows are structural units; columns are the user's figures and each map's, expressed **both
in pages and as a percentage of that script's own length**, because raw page counts are not
comparable across scripts of different lengths. The variance column is measured **in points against
the corpus range** the chosen maps form, not against an average — an n of three has no meaningful
mean, but it has a real floor and ceiling.

| Unit | Yours (claimed) | Map A | Map B | Map C | Corpus range | Variance |
|---|---|---|---|---|---|---|
| Cold open | 6 pp / 14% | … | … | … | 0–25% | inside |
| Act One | 18 pp / 41% | … | … | … | 27–50% | inside |

**Then the row that per-unit rows cannot produce: the derived relation.** Every unit can sit inside
the range while the shape is still wrong, because the rows are blind to the proportions *between*
them. Always add at least one ratio row — for two-act comedy, Act One : Act Two — and compute it for
every map. This row is where Compare earns the mode, and in practice it is where the finding is.

### 10.4 The analysis rule

For every deviation the table shows, run §3.1's interrogation with the maps supplying Q4. The
question is never *does yours differ* — it is **what did the produced script buy with its choice, and
is yours buying anything?**

1. **Name the purchase in each map, from the map's own text, with pages.** "Act Two is longer" is not
   a purchase. "Act Two fragments into eight scenes across five sets and spends them on two obstacles,
   a reversal and a return" is.
2. **Ask what the user's figure buys in the same currency.** If the produced scripts all spend their
   long unit on collision and the user's long unit is the installing one, the question is whether the
   installation is doing work the corpus does elsewhere — often in the cold open — or is simply setup.
3. **A deviation with a named purchase is not a fault.** It goes to "what is working," with the
   precedent beside it. A deviation whose purchase the writer cannot name is the finding, priced by
   how much of the shape depends on it.
4. **Never convert a range into a target.** The corpus floor is not a minimum and the ceiling is not
   a cap; three scripts cannot license a rule. Report position within the range, and reserve the word
   *fault* for the thing that has no purchase.

### 10.5 Worked example — a 44-page multi-cam pilot, figures only

**Input:** 44 pages; cold open 6, Act One 18, Act Two 16, tag 4. Sums to 44 ✓. 44 pp is inside the
measured multi-cam band (44–51) and sits exactly at its floor — the same length as Seinfeld.

**Maps:** the whole multi-cam cohort, which is three: `../../../structure-library/tv-seinfeld-pilot.md`
(44 pp, the length twin), `../../../structure-library/tv-big-bang-theory-pilot.md` (51 pp, the
library's primary measured multi-cam sample) and `../../../structure-library/tv-mom-pilot.md` (47 pp,
the cold-open-plus-two-acts-plus-tag shape the user is running).

| Unit | Yours (claimed) | Seinfeld (44) | Big Bang Theory (51) | Mom (47) | Corpus range | Variance |
|---|---|---|---|---|---|---|
| Cold open | 6 pp / 14% | none | pp.1–13 / 13 pp / 25% | pp.1–9 / 9 pp / 19% | 0–25% | inside; shortest of the two that have one |
| Act One | 18 pp / 41% | pp.1–22 / 22 pp / 50% | pp.14–27 / 14 pp / 27% | pp.10–26 / 17 pp / 36% | 27–50% | inside |
| Act Two | 16 pp / 36% | pp.23–44 / 22 pp / 50% | pp.28–49 / 22 pp / 43% | pp.27–43 / 17 pp / 36% | 36–50% | inside, at the floor |
| Tag | 4 pp / 9% | placeholder only, p.44 (`MONOLOGUE TO COME`) | pp.50–51 / 2 pp / 4% | pp.44–47 / 4 pp / 9% | 0–9% | same 4 pp as Mom |
| **Act One : Act Two** | **1.13** | **1.00** | **0.64** | **1.00** | **0.64–1.00** | **+0.13 above the ceiling — outside the corpus** |

**Headline: every unit is in range and the shape is still the outlier. Your Act One is longer than
your Act Two — 18 against 16 — and none of the three produced multi-cams does that.** Two are exactly
equal (Seinfeld 22/22, split at the mathematical centre of the document; Mom 17/17) and the third
runs Act Two eight pages longer than Act One (BBT 14/22). The ratio row is the only row that flags, and
it is invisible to every row above it.

**What each produced script bought with its Act Two — the purchase, in the maps' own terms:**

- **Big Bang Theory** spends the imbalance on a chase. Act One is *one continuous 14-page scene in one
  set* auditing all five principals against each other; Act Two fragments into eight scenes across
  five sets — two obstacles (the locked door pp.36–38, the man pp.39–42), the climax revealed in
  reverse (p.43), a dark night on the stairs (pp.44–45) and a return that states the series engine
  (p.48). Its map's phrase: *Act One is a microscope; Act Two is a chase.* Note where the cost went:
  the inciting incident is carried entirely by a **13-page cold open**, which is what lets Act One
  stay short enough to be a single room.
- **Mom** buys with construction rather than length. The acts are equal to the page and built in
  opposite directions — Act One is 7 scenes averaging 2.4 pp (breadth: install every relationship
  once), Act Two is 3 scenes averaging 5.7 pp including an **8-page two-hander** (depth: collide them).
  *Establish, then collide.* Act One is a montage of obligations; Act Two is the bill coming due.
- **Seinfeld** buys a second question. Act I hands Jerry a problem and a stupid solution; Act II
  executes it and **closes the ostensible goal at 70%** (p.29), then spends its last third on the
  question the episode was actually about, named at 80% (pp.35–36) — thirteen pages after the plot was
  solved. A 22-page second act is what makes room for the story to change subject.

**The question back to the writer, which is the deliverable.** All three spend Act Two on something
Act One cannot do: fragmenting, colliding, or re-asking. Yours is the shortest unit in the script.
So — *what are the extra two pages of Act One doing, and does Act Two still have room?* Two answers
are legitimate and one is not. If your Act One is running Mom's breadth pass, seven-odd short scenes
installing a relationship each, 18 pages is cheap and the finding is about Act Two instead: 16 pages
is where you have to fragment, collide **and** re-ask, and it is the corpus floor. If your 6-page cold
open is not carrying the inciting incident the way BBT's 13 pages do, Act One is carrying it, and 18
pages is the receipt — that is a purchase, and it makes the cold open the thing to look at. But if
Act One is 18 pages of setup with no complete movement in it, the ratio is the fault and it is a P1:
the pages are in the half of the script that cannot spend them.

**Limits, stated in the report, not omitted from it.** Three maps are a cohort, not a law — 1.00 is
not a target and 0.64 is not a licence. All figures above the ratio row are the writer's claims;
Seinfeld, BBT and Mom are measured `[M]`. And nothing here can see whether the beats work: with no
pages there is no five-beat sweep, no midpoint percentage, no INERT test, no causality pass, and no
view of the two properties that decide whether a multi-cam plays at all — roughly three jokes a page
and almost every scene going out on one.
