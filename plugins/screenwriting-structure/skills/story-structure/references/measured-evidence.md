# Measured Evidence — Tolerances from 42 Beat Maps

Reference for Claude. Every figure below was measured off a script PDF in the library, not quoted
from a craft book. When this file and a framework disagree, this file is the evidence and the
framework is the claim. Use it to tell a structural problem from a harmless deviation, and to fill
the `Tolerance` column of a `structure.md` beat sheet.

Severity vocabulary: **error** (say it first, loudly), **warn** (raise it, ask the diagnostic
first), **note** (mention only if asked). Severity is not the spec's `Status` field — a beat outside
tolerance is not automatically `broken`.

---

## 1. The corpus

The evidence is 42 page-referenced beat maps (18 features, 24 TV episodes, ~380,000 words), each
built independently from its source PDF, with every beat row carrying a page citation and every
percentage computed against that script's own measured printed length. They were verified 2026-08-10
by adversarial spot-check of six files — page counts, PDF-to-printed offsets, 18 sampled beat rows,
headline claims, ~20 percentage recomputations — finding four errors, since corrected, and no
contradictions *between* maps. A later verbatim re-extraction of all eighteen features' turns did
find contradictions *within* maps, between a beat's percentage and the prose describing it; see the
caveat at the end of §2 before quoting any map's characterisation of a beat. It is a convenience
sample of one library's holdings: it measures what these 42 scripts do, not what scripts in general
do.

**Two caveats that must travel with every number:**

| Caveat | What it means when you cite a figure |
|---|---|
| **Draft, not film.** Every map is of the draft in the library, which is frequently *not* the release cut. Severance is a pre-production spec with a different protagonist; Raiders is the 1979 third draft with a different climax; Succession's draft has Kendall *winning* the deal; Barry kills NoHo Hank on p.34; Seinfeld's pilot is "The Stake Out" with Elaine named "Eileen". | Placements are measured from the page as written. Never tell a writer "the film does X at p.N" — say "the draft does". |
| **Several PDFs were OCR'd.** Where a PDF had no text layer the whole script was rendered and OCR'd page by page — Mean Girls (a 180°-rotated image scan) and Desperate Housewives (300 dpi, key pages verified visually) both declare this in their headers; Mulan logs an OCR artifact in its revision slugs. | Page numbers and sluglines from those files were spot-verified and are usable. **Quoted dialogue from them is a transcription, not authoritative** — do not quote it as exact wording. |

One known source defect: the No Country PDF is an 8-page excerpt (cover + pp.111–117); that map's
pp.1–82 were reconstructed from external page-numbered copies and pp.83–110 are marked `~est.` Treat
its interpolated pages as indicative only.

---

## 2. Headline finding, as an operating rule: check the middle, not the quarter mark

Of the eighteen features in the corpus, seventeen have a midpoint their map can locate — Oppenheimer
names none. **Fourteen of those seventeen — 82% — land between 47% and 55%**, over a full spread of
**45% to 67%**. All eighteen have a locatable first-act break, and only **ten of the eighteen — 56% —
fall in the conventional 19–25% zone**, over a full spread of **10% to 38%**. The midpoint's range is
22 percentage points; the first-act break's is 28.

| Script | Length | Act One break | % | Midpoint | % |
|---|---|---|---|---|---|
| The Father | 87 pp | pp.9–10 | 10–11% | pp.44–46 | 51–53% |
| No Country for Old Men | 117 pp | pp.12–13 | 10–11% | pp.57–59 | 49–50% |
| Parasite | 141 pp | pp.13–16 | ~11% | p.71 (the hinge) | 50.4% |
| Lady Bird | 110 pp | p.14 | 13% | pp.50–52 | 45–47% |
| E.T. | 113 pp | pp.21–22 | 19% | p.62 | 55% |
| Raiders of the Lost Ark | 104 pp | p.20 | 19% | p.52 | 50% |
| Legally Blonde | 117 pp | p.25 | 21% | pp.58–60 (fulcrum) | 50–51% |
| Mulan | 101 pp | p.21 | 21% | pp.47–53 | 47–52% |
| Aftersun | 100 pp | p.21 (frame) | 21% | p.48 (frame) | 48% |
| Oppenheimer | 197 pp | pp.41–43 | 21–22% | *none stated* | — |
| Juno | 101 pp | pp.21–24 | 21–24% | p.68 | **67%** |
| Everything Everywhere All at Once | 125 pp | p.29 | 23% | pp.63–64 | 50–51% |
| The Matrix | 126 pp | pp.29–30 | 23–24% | pp.60–63 | 48–50% |
| Mean Girls | 117 pp | p.29 (moral) | 25% | pp.58–59 | 50% |
| Dune | 110 pp | pp.32–33 | 29–30% | pp.60–61 | 55% |
| Erin Brockovich | 135 pp | pp.45–48 (hard) | 33–36% | p.68 | 50.4% |
| When Harry Met Sally… | 122 pp | pp.43–44 | ~36% | pp.63–64 | ~52% |
| Glass Onion | 134 pp | p.51 | 37–38% | p.61 / p.73 (rewind) | 45–46% / 54.5% |

(An earlier version of this file counted fourteen locatable midpoints against a twelve-row table and
left the gap open. **That is now resolved**: the corpus is eighteen features, seventeen locatable
midpoints, eighteen locatable first-act breaks. Every row is above; nothing is held back.)

**The outliers, named rather than dropped.** Juno's midpoint at 67% is the extreme of the set and the
only one far outside the band — its map attributes this to a catalyst front-loaded to p.4 (4%), which
pushes everything downstream. Lady Bird at 45–47% and Glass Onion's stated midpoint at 45–46% sit
just below the floor; Glass Onion moves inside the band if scored on what its own map calls the "true
structural midpoint," the rewind at p.73 (54.5%). E.T. and Dune both sit at the 55% ceiling.
Oppenheimer names no structural midpoint at all, attaching centre-language to three different
non-overlapping blocks (46–50%, 50–52%, 54–56%) — the honest answer for a film built on two
interleaved timelines, and a reminder that "no locatable midpoint" is a real reading, not a gap.

Two scripts disclaim three-act architecture and still have a locatable centre. Aftersun declares both
turns absent from the holiday body and relocates them to its 4.8-page memory frame (break p.21/21%,
midpoint p.48/48%); The Father opens "the script has no act structure in the conventional sense" and
then names both beats outright (pp.9–10/10–11%, pp.44–46/51–53%). **Even scripts that refuse the
paradigm keep a middle.**

**Operating rules. Apply in this order:**

1. **Midpoint outside 47–55% → error.** This is the one placement the corpus agrees on. A story
   whose centre sits at 40% or 62% has a real problem: either the middle is misidentified or the
   second act is lopsided. Three scripts are outside it and each names its reason (above); "Juno did
   it" is not a defence unless the catalyst is front-loaded the way Juno's is.
2. **First-act break outside 10–38% → warn, gently, and only after asking the diagnostics in §3.**
   Inside 10–38% there is no finding to report: that band *is* the measured corpus, end to end.
3. **Never flag a first-act break merely for missing 25%.** A break at 13%, 21%, 30% or 36% is inside
   measured practice, and only ten of eighteen scripts hit 19–25% at all. Snyder's 20–25% and Field's
   Plot Point I are prescriptions, not measurements.

**This inverts how most beat-sheet tools behave.** They police the quarter mark hard and treat the
midpoint as a refinement — Field's emphasis, inherited by Snyder. The measurement says the opposite.
A midpoint at 50% with a first-act break anywhere from 10% to 38% describes almost every script here;
a break at exactly 25% with a midpoint at 40% or 60% describes none. Check the middle first.

**A caveat about the maps themselves — and the reason this file exists.** Eight of the eighteen use
"exact centre," "dead centre" or "exactly the halfway mark" for a beat their own percentage shows is
not centred — including E.T. and Dune at 55%, Lady Bird at 45–47%, Juno at 64–67%, and The Father,
whose prose says "~50%" for a beat its own row dates 51–53%. In two the arithmetic is demonstrably
wrong: Oppenheimer labels pp.106–110 "dead centre" of a 197-page script (its own row: 54–56%), and
Glass Onion labels pp.70–73 "dead centre" of a 134-page one (its own row: the rewind at 54.5%). In a
third, Parasite, two different beats are each called the centre. The pull toward confirming the
theory is strong enough to bend careful prose in nearly half the corpus. **Measure the percentage;
never accept a beat's label as its placement** — including in maps written by this KB.

---

## 3. The late-break licence — and its mirror

The four scripts with the latest Act One breaks each pay for the delay the same way: **they run
complete small stories in the space before the break.**

| Script | Break | What the long first act contains |
|---|---|---|
| Glass Onion | p.51 / 37–38% | An entire fake detective story — invitation, puzzle boxes, gathering, Blanc's arrival — run to completion and then killed on the page. The latest first-act curtain in the set. |
| Erin Brockovich | pp.45–48 / 33–36% | A full job-hunt story with its own crisis — the situation turns at p.13 (~10%), the problem arrives at p.19 (~14%), and the dramatic question isn't asked until p.48. A soft plot point and a hard one, twenty pages apart. |
| When Harry Met Sally… | pp.43–44 / ~36% | Three separate, complete meetings across three time blocks; the love story's real inciting incident (the bookstore) doesn't arrive until ~30%. |
| Dune | pp.32–33 / 29–30% | The gom jabbar test (pp.24–28) and the departure as a self-contained movement, plus the theme statement at p.13 and the antagonist's plan stated in plain language at pp.20–21. |

**The early-break licence is the mirror image**, and it buys something different. The four earliest
breaks — The Father (pp.9–10 / 10–11%), No Country (pp.12–13 / 10–11%), Parasite (pp.13–16 / ~11%),
Lady Bird (p.14 / 13%) — purchase a long, undirected second act in which the audience does not yet
know what *kind* of story it is watching. No Country runs eighty pages before the genre resolves;
Parasite's second act is a con whose real subject is not revealed until p.71; Lady Bird's has no
goal-obstacle spine at all. Three of the four are the corpus's least conventional films. **An early
break is a purchase, not an accident** — so the diagnostic runs the other way: ask what the
undirected stretch is *for*. If the answer is "the writer had nothing to withhold," warn.

**The diagnostic — ask this before flagging any long first act:**

> Does the material before the break constitute a *complete* small story — with its own question,
> its own crisis and its own answer — or is it only setup for the story that follows?

- **Complete small story → do not flag.** A long first act is affordable when it isn't only setup.
  Erin Brockovich's investigation is engaging before the case exists; Dune's Act I contains its own
  internal test, not preparation for one.
- **Only setup → warn.** A late break is paid for in audience patience, and setup alone does not pay
  it. Note the Dune map's caveat about itself: a 30% first act works "only at epic scale and with a
  novel's brand equity behind it."

The same licence operates in TV. The Rookie's first commercial break does not arrive until 35%
(p.21), and it pays for that by installing the series engine on a single page — the "T.O. match
game" on p.10 creates three permanently mismatched two-handers in twelve lines. Its remaining breaks
land at 48%, 62% and 82%: the classic feature turn positions.

---

## 4. Measured page counts by format

| Format | Scripts measured | Measured range | Stated convention | Source | Verdict |
|---|---|---|---|---|---|
| Feature | 18 scripts | 87–197 pp | 90–120 pp | **measured** | Confirmed for the centre; the tails are real (The Father 87, Oppenheimer 197) |
| Network hour | The Rookie 60, Desperate Housewives 59 | 59–60 pp | 50–60 pp | **measured**, n=2 | Confirmed, at the top of the range |
| Cable hour | Breaking Bad 57 | 57 pp | 55–80 pp | **measured**, n=1 | Confirmed |
| Premium/streaming hour | Succession 72, Mare 80, Poker Face 65, Black Mirror 64, Chernobyl 54, Severance 53 | 53–80 pp | 55–80 pp | **measured**, n=6 | Confirmed; note the 27-page spread *within one format* |
| Multi-cam half-hour | Big Bang Theory 51, Mom 47, Seinfeld 44 | 44–51 pp | 42–58 pp double-spaced | **measured**, n=3 | Confirmed |
| Single-cam half-hour | Ted Lasso 39, The Bear 37, Only Murders 37, The Office 37, Barry 35, Weird City 35, Abbott 34, BEEF 34, Russian Doll 30 | **30–39 pp** | 25–34 pp | **measured**, n=9 | **Correction. 30–39 pp is the real band** |
| Half-hour drama | The Bear 37, Barry 35, BEEF 34 | **34–37 pp** | 28–36 pp | **measured**, n=3 | Convention runs slightly low; the band is 34–37 |
| Animated TV | BoJack 4x11 39 | 39 pp | — | **measured**, n=1 | New data point, no convention to test |

**The single-cam correction is the one that matters.** The widely repeated "25–34 pages for a half
hour" is low by roughly five pages against nine measured scripts; only two of the nine (Abbott 34,
BEEF 34) fall inside it. Use 30–39 pp; do not flag a 38-page single-cam pilot as overlong. **The
half-hour drama band is 34–37 pp** against three scripts — narrow sample, so state the n if you cite
it.

**Multi-cam page-to-minute ratio, measured directly:** Seinfeld ≈1.9 pp/min (44 double-spaced pages
≈ 23 minutes, about 30 seconds per page); Big Bang Theory ≈2.1–2.4 pp/min (51 pages ≈ 21–22 minutes).
A double-spaced multi-cam page is worth roughly half a single-spaced page, and the ratio is stable
enough to estimate runtime from page count.

---

## 5. Act architecture — labels are a drafting tool, not a scheduling artifact

| Prints act breaks | Does not print act breaks |
|---|---|
| The Rookie (5 acts), Desperate Housewives (4 + teaser), Breaking Bad (4 + teaser), Severance (4 + prologue + tag), Abbott Elementary (3 + cold open + tag), Big Bang Theory (2 + cold open + tag), Mom (2 + cold open + tag), Seinfeld (2), Weird City (3), BoJack (3 + cold open), Only Murders (act-outs only), Black Mirror (4 UK "PARTS") | Succession, Chernobyl, Mare of Easttown, This Is Us, The Office, Ted Lasso, Russian Doll, Barry, BEEF, The Bear, Poker Face, The Afterparty |

The obvious correlation — network and basic cable print acts, premium doesn't — holds, but it is not
the rule it is usually stated as. Two exceptions carry the lesson:

- **Severance prints four acts, a prologue and a tag** on what became an Apple TV+ show with no
  commercial breaks: network architecture as a drafting discipline, not a scheduling requirement.
  Three of its five act-outs are stillness rather than jeopardy (p.4 a door opening, p.27 a silent
  room, p.52 two jailers waiting), and its Act 2 runs 16 pages — 30% of a 53-page script.
- **This Is Us prints nothing** despite being a network hour: no ACT ONE, no teaser header, no FADE
  IN, six `CUT TO:`s in 54 pages. Its *inferred* act lengths — **8.5 / 9 / 10 / 9 / 8.3 / 8.1 pp** —
  are more regular than several scripts that do print them. The acts were designed; only the labels
  are missing.

**Generalization for the linter: act labels are a drafting tool that survives independently of
whether anything is scheduled to interrupt the episode.** Never infer a problem from the absence of
printed act breaks, nor sound structure from their presence. Scripts that omit the labels still turn
on a schedule — Succession's central turn lands at 58–60%, where a four-act hour puts its third
act-out; Barry's land at 31% / 49% / 71% / 86%, feature architecture at half-hour scale.

**Act-out craft, measured.** Three of Breaking Bad's four act-outs are transgressions, not jeopardy —
Walt pointing a gun at approaching sirens (p.3), blackmailing Jesse (p.31), assaulting a teenager
(p.43): the buttons measure appetite, not danger. Abbott Elementary does the inverse — its biggest
reversal (Ava's sign, p.22) is deliberately *not* the act-out, because two further pages convert it
into Janine's own mistake so the act buttons on self-inflicted humiliation. The act-out is chosen
for what it reveals, not for what it leaves unresolved. **Never flag an act-out for lacking a
cliffhanger.**

---

## 6. Tolerance table

`n` is the number of scripts behind the band. Where `n` is blank the corpus does not measure the
beat, and **position alone is not a finding** — check for presence, not placement.

| Beat (spec term) | Framework target | Measured band | n | Severity outside | Ask before flagging |
|---|---|---|---|---|---|
| **Midpoint reversal** | 50% | **47–55%** (14/17, 82%); full range **45–67%** | 17 | **error** | Is the beat you measured actually the centre — a reversal or re-description — or did you mislabel a complication? Parasite's p.71 voids the goal rather than escalating it; a three-act pass mislabels it. Note that a script may legitimately have *none*: Oppenheimer's map names no midpoint at all. |
| **Commitment** (Act One break / Break into Two) | 20–25% (Snyder) · 25% (Field) | **10–38%** (only 10/18 in the 19–25% zone) | 18 | **warn**, and only outside the band | Inside 10–38% there is no finding. Outside it: does the pre-break material run a *complete* small story, or does a very early break buy an undirected second act (§3)? Never flag for missing 25% — most of the corpus misses it. |
| **Disturbance** (inciting incident / catalyst) | ~10–12% | *not measured as a band* | — | **note** only | Is it present and does it change the protagonist's situation? Erin Brockovich turns the situation at ~10% and delivers the problem at ~14%, then defers the dramatic question to 36% — a legitimate split, not an error. |
| **Collapse** (all is lost) | ~75% | *not measured as a band* | — | **note** only | Individual maps cluster near 71–86% (Barry 71% then 86%; WHMS 86–88%). Too few measured to police. Check that something is actually lost — Legally Blonde's crisis leaves every success intact and destroys only her belief she earned them. |
| **Proof** (climax / final image) | 90–100% | *sits very late where measured* | — | **note** only | EEAAO's Final Image is pp.124–125 / 99–100%; Dune's climax pp.107–109 / 97–99%; Oppenheimer defers its opening cutaway (p.8) to p.195 of 197. A late climax is normal; flag only if there is no climax. |
| **Protagonist handoff** | not in any framework | ~87% where it occurs | 2 | **note** | Parasite hands off at p.89 and No Country at pp.102–103 (87%). If a script does this, it is a choice with precedent, not a fault. |
| **Feature length** | 90–120 pp | **87–197 pp** | 18 | **warn** below 87 / above 197 | Is the outlier structural (Oppenheimer's dual timeline) or is it bloat? |
| **Single-cam half-hour length** | 25–34 pp | **30–39 pp** | 9 | **warn** outside | Use the measured band, not the convention. |
| **Half-hour drama length** | 28–36 pp | **34–37 pp** | 3 | **note** | n=3. Say the sample size. |
| **Multi-cam half-hour length** | 42–58 pp | **44–51 pp** | 3 | **note** | Double-spaced pages; convert at ≈1.9–2.4 pp/min before judging runtime. |
| **Premium hour length** | 55–80 pp | **53–80 pp** | 6 | **note** | 27-page spread inside one format. Almost nothing is out of range. |
| **Network hour length** | 50–60 pp | **59–60 pp** | 2 | **note** | Real network hours sit at the top of the stated band. |
| **Printed act breaks** | required by format | *no correlation strong enough to police* | 24 | **never flag** | Severance prints four on a streaming show; This Is Us prints none on a network show. Absence proves nothing. |
| **Act length regularity (TV)** | equal acts | measured acts are often wildly unequal | — | **note** | The Rookie's Act One is 35% of the script; Severance's Act 2 is 30%. Ask whether the long act is doing extra work, not whether it is long. |

---

## 7. What the corpus cannot tell you

State these limits whenever you cite a number as though it settles something.

- **42 scripts is a sample, and small per cell.** Several bands rest on n=1, n=2 or n=3; one more
  script could move the cable-hour or animated-TV "range" by twenty pages. Give the n when it is low.
- **It skews toward acclaimed and produced work — survivorship.** The corpus can say what working
  scripts did. It cannot say a script doing otherwise will fail, because the scripts that did
  otherwise and failed are not in the library and were never measured.
- **TV is pilot-heavy.** 23 of 24 TV maps are pilots or first episodes (the exception is BoJack
  4x11). **Mid-season and finale structure is entirely unmeasured.** Do not transfer pilot tolerances
  to episode 6 or a finale: installing a world, an engine and a series question is not their job.
- **Every map is of a draft**, and nine catalogued drafts differ from the release cut by a
  *structural* fix, not a polish — who wakes up first, who wins the deal, whether the hero is present
  at his own climax. The corpus measures scripts at the stage where they still had those problems.
- **No measurement can tell you whether a beat is good.** Placement is the only property measured.
  EEAAO lands eleven of fifteen Save the Cat beats within three points and three exactly; its
  apparent formlessness is entirely in the *content* of the beats. A script can be perfectly placed
  and dead. Position is a diagnostic prompt, never a verdict.
- **On hard scripts one framework is not enough.** Where a script resists a single lens, run two and
  surface the disagreement rather than resolving it — the disagreement is the finding. Mulan against
  Vogler and Hudson does not merely fit one better; the two lenses describe *different characters*.

*Compiled 2026-08-10 from the 42 beat maps in `../../../structure-library/`. Every figure above is
traceable to a named map; where a claim and a map disagree, the map governs. Index and per-map
verification notes: `../../../structure-library/INDEX.md`.*
