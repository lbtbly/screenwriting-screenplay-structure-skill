# The structure.md Format — Annotated Template

A `structure.md` is a **self-contained structural contract**: any writer (human, Claude, the structure-audit skill, an orchestrator) must be able to outline, draft, or judge the script from this file alone — without the framework library, the beat maps, or this skill. It is the exact analogue of `voice.md` in the sibling `screenwriting-voices` plugin: `voice.md` says how a mouth sounds, `structure.md` says where the story turns and why there. File naming: `structure/<project>.structure.md`, kept beside the screenplay.

## Rules of the format

1. **Every page figure carries its source.** A `Target %` is either a framework prescription ("Snyder: Break into Two at 23%") or measured evidence ("median 21% across 12 KB rom-coms"). Write which. A number with no provenance is a number nobody can argue with, which makes it useless.
2. **Four `Status` values and nothing else.** `planned` (designed, unwritten) · `drafted` (written, unassessed) · `working` (assessed, holds) · `broken` (assessed, fails). No "mostly," no "needs work," no empty cell on a beat that exists. Vocabulary drift is what makes a spec unauditable.
3. **Self-contained.** No references out. If a beat's name is framework jargon, the `What happens` column says what happens in this script, in this world, with these names.
4. **Under-specify rather than over-specify.** Fifteen committed beats and honest blanks beat forty beats of filler. A blank is auditable; a guess is not. Never fill an `Actual` column from intention — only from pages that exist.
5. **Never delete a Decision.** Supersede it with a new numbered, dated entry that names the one it replaces. The log is the file's memory; deleting from it re-opens settled questions.
6. **Targets are targets, not law.** A variance is a finding, not a failure. Legally Blonde's All Is Lost lands 17 points late and the script is stronger for it — the spec's job is to record the deviation and the reason, so a later pass argues with the reason instead of the number.

## The template, annotated

```markdown
# <Project title> — Structure Spec
**Format:** feature | tv-hour-network | tv-hour-premium | tv-half-single | tv-half-multi | limited | short | vertical
**Target length:** <n> pp   **Genre:** <primary> (+ <secondary>)
**Framework(s):** PRIMARY: <name> · SECONDARY: <name>
**Status:** premise | outline | treatment | draft <n>
**Last updated:** <date>
```

The header is what makes every percentage in the file computable. `Target length` is the denominator — without it a `Target %` cannot become a page number. `Format` selects which sections are live (the Act grid is TV-only). Naming a PRIMARY framework commits the spec to one beat vocabulary; a spec that borrows beat names from three frameworks at once cannot be audited, because no two of them agree on where the midpoint is.

```markdown
## Premise
- **Logline:** one sentence — protagonist, want, opposition, stakes.
- **Dramatic question:** the yes/no the ending answers.
- **Central dramatic argument:** the debatable proposition the story tests (Mazin).
```

The **logline** must name all four elements or the beat sheet has nothing to hang on: no want means no Commitment beat, no opposition means no Collapse. The **dramatic question** is answerable yes or no by the last page — "Does she win the case?" not "What will she learn?" The **central dramatic argument** is the hard one: state a claim someone could argue against. Good: *"institutional lies cost more than the truth they hide"* (Chernobyl). Bad: *"the story is about lies"* — that is a topic, and a topic cannot be tested, so every scene passes and the spec loses its ability to reject anything.

```markdown
## The five load-bearing beats
| Beat | Target p. | Target % | Actual p. | What happens | Status |
|---|---|---|---|---|---|
| Disturbance | | | | | planned / drafted / working / broken |
| Commitment | | | | | |
| Midpoint reversal | | | | | |
| Collapse | | | | | |
| Proof | | | | | |
```

The minimal spine, framework-independent. Every format has these in some form; **if one is missing or unplaceable, that is the finding** — write "unplaceable" in `Actual p.` and `broken` in `Status` rather than nominating the nearest scene. A good entry is a specific event with a page: "Donovan's hand on her thigh, p.100." A bad one is a condition ("she loses confidence") — conditions cannot be located, so they cannot be fixed.

```markdown
## Beat sheet
| # | Beat (framework term) | Target pp | Target % | Actual | Storyline | What happens | Status |
|---|---|---|---|---|---|---|---|
```

The PRIMARY framework's beats in order, one row each. `Target %` comes from the framework; `Target pp` is that percentage against this script's length; `Actual` comes from pages that exist. The `Storyline` column is what stops the sheet from becoming an A-story-only document — if every row says A, either the script has one thread or the spec has stopped looking.

```markdown
## Storylines
| Thread | Whose | What it is | Beats | Converges at |
|---|---|---|---|---|
```

One row per thread, lettered A/B/C/D. `Converges at` is the load-bearing column: a thread that never converges is a subplot the audit will flag for deletion. Cite page numbers, not adjectives.

```markdown
## Act grid (TV only)
| Act | Pages | Length | % | What turns | Act-out | Button type |
|---|---|---|---|---|---|---|
```

TV only; delete for features. `Act-out` quotes or describes the last image or line before the break — not the act's subject. `Button type` names the mechanism (jeopardy / revelation / decision / innocent-in-jeopardy / series-engine) so the pattern across acts is visible; four identical button types in a row is a finding the grid should make obvious at a glance.

```markdown
## Genre contract
| Obligatory scene/element | Required by | Present? | Where |
|---|---|---|---|
```

The scenes the audience has already paid for. `Required by` names the genre or subgenre making the demand. `Present?` is `yes`, `absent`, or `subverted` — and **subverted requires the page where the subversion happens**, because an obligatory scene that is merely missing reads to an audience as an error, while one that is staged straight and then refused reads as an argument.

```markdown
## Decisions
Numbered, dated. Each: the choice, the alternative rejected, the reason.

## Open questions
## Change log
```

The Decisions log exists so a later pass cannot relitigate a settled question. Each entry needs all three parts — the choice alone is a note, the choice plus the rejected alternative is an argument, and only the reason survives contact with a reader who disagrees. **Open questions** are things genuinely undecided; moving one into Decisions is how the spec makes progress. **Change log** is one line per pass: date, what moved, why.

## Worked example — FEATURE

*Reverse-engineered from the Legally Blonde shooting draft (31 July 2000), 117 printed pp. Decision dates are illustrative.*

```markdown
# Legally Blonde — Structure Spec
**Format:** feature
**Target length:** 117 pp   **Genre:** studio romantic comedy (+ fish-out-of-water campus comedy, courtroom third act)
**Framework(s):** PRIMARY: Save the Cat 15-beat · SECONDARY: Snyder story-DNA — Fool Triumphant with a Golden Fleece prize-swap
**Status:** draft 3
**Last updated:** 2000-07-31

## Premise
- **Logline:** A Bel Air sorority queen dumped for being "too blonde to be serious" talks her way into Harvard Law to win her ex back — and, defending a fitness mogul accused of murder, discovers the frivolous expertise everyone mocks her for is the only thing in the building that can crack the case.
- **Dramatic question:** Will Elle be taken seriously on her own terms — and does she still want him?
- **Central dramatic argument:** Expertise the culture codes as frivolous is real expertise, and the institutions that despise it are worse at their own job for excluding it.

## The five load-bearing beats
| Beat | Target p. | Target % | Actual p. | What happens | Status |
|---|---|---|---|---|---|
| Disturbance | 13 | 11% (Snyder) | 8 (7%) | The Ivy: "I need to marry a Jackie, not a Marilyn" | working |
| Commitment | 27 | 23% (Snyder) | 25 (21%) | Boxster and moving van roll onto Harvard Yard, wordless | working |
| Midpoint reversal | 59 | 50% (Snyder) | 58 (50%) | Dewey's trailer — the law used for someone other than herself | working |
| Collapse | 80 | 68% (Snyder) | 100 (85%) | Donovan's praise, then his hand on her thigh | working — see D2 |
| Proof | — | 77–100% (Snyder) | 107–111 (91–95%) | The perm cross-examination; Chutney confesses | working |

## Beat sheet
`Target %` = Snyder's prescribed slots. `Target pp` = those slots against 117 pp. `Actual` = measured off the draft.
| # | Beat | Target pp | Target % | Actual | Storyline | What happens | Status |
|---|---|---|---|---|---|---|---|
| 1 | Opening Image | 1 | 1% | 1–2 (1–2%) | A | The signature card through the Delta Gamma house; feet-first to the Queen | working |
| 2 | Theme Stated | 6 | 5% | 5–7 (4–6%) dramatised; 60 (51%) spoken | A | The low-viscosity-rayon takedown; then Stromwell's "an image and a good hook can get you into a room" | working — see D1 |
| 3 | Set-Up | 1–11 | 1–9% | 1–15 (1–13%) | A/B | Sorority world, Warner, the Ivy, the mourning week | working (runs 4 pts long; catalyst sits inside it) |
| 4 | Catalyst | 13 | 11% | 8 (7%) | B | The break-up — a rom-com opening on its own third act | working |
| 5 | Debate | 13–27 | 11–23% | 9–24 (8–21%) | A | Grief; Town & Country; the advisor; the LSAT montage; admission | working (heroine never doubts; everyone else does) |
| 6 | Break into Two | 27 | 23% | 25 (21%) | A | Harvard Yard, the pink love seat off the truck | working |
| 7 | B Story | 32 | 27% | 33 (28%) | B | Emmett on the benches hands her the real curriculum | working |
| 8 | Fun and Games | 32–59 | 27–50% | 25–51 (21–44%) | A/B | Sorority tactics against Harvard; every gag is also a failure | working |
| 9 | Midpoint | 59 | 50% | 51–61 (44–52%), fulcrum 58–60 | A/C | Bunny tail thrown → work montage → Dewey → theme stated → internship | working |
| 10 | Bad Guys Close In | 59–80 | 50–68% | 63–100 (54–85%) | A | The Windham case, the withheld alibi, the ethical test, the pool boy | working — see D2 |
| 11 | All Is Lost | 80 | 68% | 100 (85%) | A | The hand on the thigh; Sarah misreads it through the glass | working |
| 12 | Dark Night of the Soul | 80–90 | 68–77% | 101–103 (86–88%) | A/C | "It turns out, I am a joke"; the palm tree back in the car | working (2 pp against a prescribed 10) |
| 13 | Break into Three | 90 | 77% | 103 (88%) | C | Stromwell spins around in the salon chair, nails drying | working |
| 14 | Finale | 90–117 | 77–100% | 105–116 (90–99%) | A/B/C/D | Brooke fires Donovan → Prada entrance → Rule 3:03 → the perm → Warner refused → Sarah → Emmett | working (12 pp against 25) |
| 15 | Final Image | 117 | 100% | 116–117 (99–100%) | A/D | The Blonde Legal Defense Club table; Sarah newly blonde | working |

## Storylines
| Thread | Whose | What it is | Beats | Converges at |
|---|---|---|---|---|
| A | Elle | The competence spine: law school → internship → the Windham case | 33 thrown out · 53 a right answer · 56 the resume · 61 the internship · 75 the client's secret · 107 the witness · 116 the club table | 63 (absorbs the case) · 110 (the perm) |
| B | Elle / Warner→Emmett | Stated love object refused; actual one earned by argument | 8 break-up · 33 the bench · 79–85 the Volvo · 95 Emmett spends his credibility · 113 Warner refused · 115–116 the kiss | 109 ("Have a little faith" returns into A) · 112 (the reaction two-shot) |
| C | Paulette | The class mirror and the theme's proving ground | 37–40 intro · 58 first client · 69–71 Bend & Snap · 92–93 the payoff · 98 "You're going to make a great lawyer" | 58 (A meets C at exactly 50%) · 103 (C delivers A's Break into Three) |
| D | Sarah | Rival to partner — carries the full rom-com beat sheet B is denied | 36 the fiancée reveal · 50 the betting pool · 78 grudging respect · 92 "We'll drink it after we win" · 100–101 betrayal misread · 114–115 apology and union | 105–107 (the courtroom) · 116–117 (newly blonde, Final Image) |

## Genre contract
| Obligatory scene/element | Required by | Present? | Where |
|---|---|---|---|
| Meet-cute | rom-com | subverted — a bench and a piece of usable information, no attraction beat | 33 |
| Third-act declaration | rom-com | subverted — played straight for four lines, then wrist-locked | 113–114 |
| The kiss | rom-com | yes — 1.5 pp at 98% | 115–116 |
| Rival / triangle | rom-com | yes — one character carries both antagonisms | 36 |
| Fool underestimated by the Establishment | Fool Triumphant | yes | 26–29 |
| The Insider who knew her before and sells her out | Fool Triumphant | yes — "You're not smart enough" | 49 |
| Transmutation / new name | Fool Triumphant | yes — the twinset; "Delta. Gamma." as her jail alias | 62, 74 |
| The institution converts, not the Fool | Fool Triumphant | yes | 116–117 |
| A cross-examination the hero wins alone | courtroom third act | yes | 107–111 |

## Decisions
1. **2000-01-12 — Dramatise the theme on p.5; state it at the midpoint.** Rejected: a spoken thesis in Snyder's page-5 slot. Reason: the rayon takedown proves the claim before the audience knows there is one; Stromwell's line at p.60 gives them language for it exactly when they need it. Snyder requires the theme be *present* by p.5, not spoken.
2. **2000-02-03 — Play "Bad Guys Close In" (54–85%) as a winning streak, not a descent.** Rejected: the prescribed deterioration, with losses accumulating from the midpoint. Reason: nothing has to be taken away if the achievement can be *poisoned* — Donovan's single gesture at p.100 retroactively re-prices forty pages of earned success. The section builds resentment instead of jeopardy, and the crisis when it arrives is single-cause, which is what makes a 2-page Dark Night and a 12-page finale survivable. Consequence accepted: All Is Lost lands 17 points late.
3. **2000-02-03 — Route the complete rom-com beat sheet through the rival, not the love interest.** Rejected: giving Emmett the canonical obstacle / jealousy / grand-gesture set. Reason: in a story about a woman's competence, running the emotional architecture through Sarah keeps the ending from being about a man. Cost accepted: a blind beat-sheet reader would identify Sarah as the love interest.

## Open questions
- Margot's lucky scrunchie (p.18) is planted and never paid. Cut the plant or build the payoff?
- The parents vanish from p.25 to a single TV cutaway at p.112.
- The Dylan McDermott chase (p.22) is the only set-piece carrying no plot.

## Change log
- 2000-01-12 — D1 logged; Theme Stated split across p.5 and p.60.
- 2000-02-03 — D2, D3 logged; back-half beats 10–14 re-targeted against the winning-streak design.
```

## Worked example — TV

*Reverse-engineered from The Rookie 1x01 "Pilot," Revised Network Draft, 60 printed pp. Decision dates are illustrative.*

```markdown
# The Rookie 1x01 "Pilot" — Structure Spec
**Format:** tv-hour-network
**Target length:** 60 pp   **Genre:** police procedural (+ workplace ensemble drama with comedy)
**Framework(s):** PRIMARY: network hour act grid · SECONDARY: procedural engine + multi-protagonist rookie structure
**Status:** draft — Revised Network Draft
**Last updated:** 2018-01-21

## Premise
- **Logline:** On the day his divorce is final a 43-year-old Pennsylvanian talks his way through a bank robbery, moves to LA and becomes the LAPD's oldest rookie — and across his first two shifts, under a T.O. who won't call him her partner and a watch commander trying to break him, he saves a child, gets a fellow officer shot, and has to decide whether the uniform is a midlife crisis or a calling.
- **Dramatic question:** Does he put the uniform back on?
- **Central dramatic argument:** A life already lived is a qualification, not a disqualification — the experience that makes him wrong for the job is the only thing that lets him do it.

## The five load-bearing beats
| Beat | Target p. | Target % | Actual p. | What happens | Status |
|---|---|---|---|---|---|
| Disturbance | 2 | 3% (teaser convention) | 2–4 (3–7%) | The robbery; he rises three times to screen Stacy's reach for the alarm | working |
| Commitment | 6 | 10% (teaser convention) | 5 (8%) | "How do you think I'd look in uniform?" → song → `Six Months Later` | working |
| Midpoint reversal | 30 | 50% (KB median, network hour) | 29–31 (48–52%) | A comic bat call becomes a missing toddler; he spots the unicorn on the truck | working |
| Collapse | 48 | 80% (KB median: last act-out) | 49–53 (82–88%) | Bradford shot on Nolan's tip; Grey: "This is your fault… You're done" | working |
| Proof | 54 | 90% (KB median, network hour) | 54 → 56–58 (90–97%) | The infant inhaler; then he sets his gun on the island as bait | working |

## Beat sheet
Carried by the Act grid at this stage: in a network hour the printed acts *are* the beat vocabulary. Per-beat rows get added only where an act reads `broken`.

## Storylines
| Thread | Whose | What it is | Beats | Converges at |
|---|---|---|---|---|
| A | Nolan & Bishop | ~47 of 86 scenes, ~34 pp, ~56% of line volume | 1–5 origin · 10–13 the contract · 15–21 case #1 and its consequence · 26–31 over-reach and rescue · 40–47 the order disobeyed · 49–58 blame and redemption | 10 (the T.O. match game creates all three tracks) · 47–49 (his mistake delivered into B) |
| B | Lucy & Bradford | ~17 scenes, ~12 pp, ~21% | 5–7 the pre-shift arrest · 18–20 the Spanish trap · 23–24 Ghost Head · 43–45 Aimee · 48–51 the ambush and the shooting | 48 (the address by text) · 51–53 (the hospital) · 58 (the montage) |
| C | Jackson & Song | ~7 scenes, ~4 pp, ~6.5% — the thinnest and cleanest arc | 14 the taser · 42–43 the leverage play · 51 freezing under fire · 53–54 the riot act · 55 the bathroom stall · 58 "I'm scared" | 51 (paid off inside someone else's action sequence) · 58 |
| Spine | Nolan vs Sgt. Grey | The only thread present in all five acts | 11 the "walking mid-life crisis" speech · 23 · 31–32 the V.O. · 39–40 "Officer Dumptruck" · 52 "You're done" · 55 "Take him with you" · 58–59 the contract | 59–60 (roll call #3 — grudging respect, then next week's crime) |

## Act grid
| Act | Pages | Length | % | What turns | Act-out | Button type |
|---|---|---|---|---|---|---|
| (de facto teaser, unlabelled) | 1–5 | ~4.5 pp | 7.5% | A divorced man survives a robbery by talking and sees his future | "How do you think I'd look in uniform?" → song → `Six Months Later` | Decision / premise |
| ACT ONE | 1–21 | 21 pp | 35.0% | Premise, precinct, three rookies, three T.O.s, first radio call; Nolan senses a lie and does not push | Rey stabbing Carlo; Nolan throws her through a glass hutch; Carlo is his first dead body | Consequence / tragedy |
| ACT TWO | 22–29 | 8 pp | 13.3% | He lies to his peers, buys a call off the radio, talks a bat out of a psychotic man's hands | "The unicorn took him" — CAMERA PULLS UP over thousands of Hollywood cars | Innocent in jeopardy / ticking clock |
| ACT THREE | 30–37 | 8 pp | 13.3% | The boy is found alive; Nolan is graded, hazed, taken home to his civilian life | "At first we think… Nolan hooked up with his Captain. But then we see that it's Lucy" | Revelation / reversal |
| ACT FOUR | 38–49 | 12 pp | 20.0% | Day Two; the BOLO; he disobeys a direct order and passes the tip to Lucy | Trunk full of AR-15s; Bradford shot; "Officer down! Shots fired!" over Lucy's open channel into Nolan's car | Jeopardy + guilt |
| ACT FIVE | 50–60 | 11 pp | 18.3% | Selby escapes, Nolan is blamed and benched, finds the inhaler, is reinstated, offers himself as hostage | `END OF EPISODE` — Grey reads out a carjacking crew: "So hunt harder…" | Series-engine button |

## Genre contract
| Obligatory scene/element | Required by | Present? | Where |
|---|---|---|---|
| An act-out at every printed break | network hour | yes — 4 of 4, types rotated | 21, 29, 37, 49 |
| Case-of-the-week engine, demonstrated more than once | procedural | yes — 5 cases, 4 generation methods (dispatched / stumbled into / poached / issued) | 15, 18 & 43, 26, 40 |
| An antagonist who cannot be arrested | series drama | yes — re-contracted, not resolved | 11, 59 |
| Ensemble introduced in behaviour, not bio | pilot | yes — 9 principals by p.10; the civilian world by p.34 | 5–13, 32–34 |
| Something only this protagonist can do | pilot | yes — the same trait pays twice | 42, 54 (set up p.16) |
| A recurring ritual / machine room | procedural | yes — roll call ×3, one per shift | 9–10, 39–40, 59–60 |
| Promise of the next episode | network pilot | yes — the last spoken line is a new BOLO | 59–60 |

## Decisions
1. **2017-11-08 — No printed teaser; Act One runs 21 pp (35%) to the first commercial break.** Rejected: labelling pp.1–5 `TEASER` and holding Act One to the conventional 10–13 pp. Reason: setup debt. Nine regulars, three permanent partnerships, an antagonist and the whole T.O. engine must be installed before the middle acts can run lean at 8 pp; a HIGH ENERGY SONG and a `Six Months Later` chyron do the act break's work for free. Condition of survival: pp.5–21 must stay relentlessly incident-driven — six locations, nine introductions, two cases.
2. **2017-11-22 — Rotate act-out types; place the only non-physical button at 62%.** Rejected: four jeopardy cliffhangers. Reason: after a child rescue the audience needs a different hook, and a five-line sex reveal holds a break because Capt. Zoe is set up eight lines earlier and the consequence is institutional, not romantic. Pattern locked: jeopardy → jeopardy → revelation → jeopardy.
3. **2017-12-06 — Let Act One's out resolve in Act Two's first lines.** Rejected: carrying the guilt across the break. Reason: an act that answers its own question must ask a different one before it goes anywhere else — Act Two pays for the fast restart by opening Bishop's son as a new serialized thread inside the same page (p.22).
4. **2017-12-06 — The protagonist does not win the climax.** Rejected: the network-conventional beat where the hero makes the arrest. Reason: Nolan disarms himself as bait and Song fires the shot (p.58). The rookie's contribution is nerve, not marksmanship — the theme is bought with the conventional beat.

## Open questions
- The C-track runs on ~4 pp and is carried by two lines ("You're not ready to be a cop…" p.54; "I'm scared" p.58). Does the arc survive a table read at that compression?
- Act Five flips time of day inside continuous action (pp.51, 55–57).
- Continuity artifacts: "43" (p.1) vs "the forty year old rookie" (p.10); 7-Adam-21 (p.18) vs 7-Adam-19 (p.43 onward).

## Change log
- 2017-11-08 — D1 logged; act grid re-cut to 21 / 8 / 8 / 12 / 11.
- 2017-11-22 — D2 logged; p.37 act-out changed from a jeopardy button to the reveal.
- 2017-12-06 — D3, D4 logged; Bishop's-son thread moved into p.22; climax re-blocked.
```

## Life cycle of the spec

The same file is written once and filled in over time. Which fields are live depends on the header's `Status`.

- **premise.** Fill the Premise block (all three items) and choose the PRIMARY framework. Fill `Target p.` and `Target %` on the five load-bearing beats; leave `Actual p.` blank and every `Status` at `planned`. The Beat sheet may be empty. Decision #1 is almost always the framework choice and why. **Do not** write a Genre contract yet — you do not know the genre's demands until you know the ending.
- **outline.** Populate the Beat sheet with `Target pp` / `Target %` / `Storyline` / `What happens`. Name the Storylines and their convergence pages. Draw the Act grid (TV) with intended act lengths and intended act-outs. Write the Genre contract with `Present?` as `planned` or `absent`. Everything is still `planned`.
- **treatment / draft n.** `Actual` columns fill in as pages exist, and only from pages that exist. Each filled `Actual` moves its row from `planned` to `drafted`. Variance is recorded, not corrected: if the Commitment lands at 21% against a 23% target, write 21% — do not adjust the target to match the draft.
- **after an audit.** `drafted` becomes `working` or `broken`. Every `broken` row gets either an Open question or a Decision. The Change log gets one line per pass.

**Handoff to `structure-audit`.** The audit skill reads the header (for the denominator), the five load-bearing beats, the Beat sheet's Target-vs-Actual columns, the Act grid, and the Genre contract, and returns a verdict per row. It may set `Status` values, add Open questions, and append to the Change log. It **may not** rewrite `Target` figures or edit existing Decisions — an auditor who moves the target destroys the evidence the audit exists to produce, and a Decision reopened by a tool is a Decision that will be relitigated every pass. If the auditor disagrees with a Decision, it files an Open question naming the Decision number. A spec with honest blanks is auditable; a spec with invented `Actual` figures is not.
