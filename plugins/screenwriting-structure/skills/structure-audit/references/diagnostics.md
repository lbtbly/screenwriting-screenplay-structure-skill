# Diagnostics — The Fault Catalogue

Reference for Claude, used by `structure-audit`. This is a differential-diagnosis manual, not a
prescription list. **The symptom is not the disease.** "Act two sags" is a complaint, not a finding;
six different faults produce it and four of them are not structural at all. Every entry below exists
to separate one cause from its neighbours.

**Rules of use.**

1. **Measure first.** Never open a fault entry before the beat locations exist on the page with page
   numbers and percentages. Run the measurement pass in `audit-procedure.md`, then come here.
2. **Run the Test before naming the fault.** A fault named without its test being run is an opinion
   with a label on it.
3. **Tolerances live in `../../story-structure/references/measured-evidence.md`**, not here. Midpoint
   outside 47–55% is an error; a first-act break anywhere in 10–38% is not a finding at all. Never
   flag a break for missing 25% — only ten of eighteen measured features hit 19–25%.
4. **ABSENT is a finding, and so is INERT.** Do not round a missing beat to the nearest available
   scene, and do not credit a beat for sitting in the right place — placement is the only property
   the corpus measures, so the tolerance pass cannot see a beat that does nothing (§1.0).
5. **Fix direction, never fixed text.** Diagnosis and treatment in the same breath produces neither.
6. **Precedents are drafts, not films.** Every citation below is measured off the draft in the
   library. Say "the draft does X at p.N", never "the film does".

**Entry format.** Fault name · **Symptom** (what the writer or reader reports) · **Test** (the check
that confirms or rules it out) · **Cause** (what usually produced it) · **Direction** (where to push,
not what to write) · **Precedent** (a produced script that faced the same pressure).

---

## 1. Spine faults — a load-bearing beat missing, misplaced, or doing no work

### 1.0 The functional tests — and the INERT verdict

The three verdicts in `audit-procedure.md` §2.1 are all about *where* a beat is, and so is the
severity table that prices them. That leaves the most common real-world spine fault invisible: a beat
that is present, sits at 50%, and does nothing. The tolerance pass returns *inside the band, no
finding*, and the writer is sent to fix a second-act sag by moving beats that are already in the
right place. Hence a fourth verdict.

**INERT** — the beat is **present and in-band and fails its functional test.** Record the page, then
price it as the audit prices ABSENT: functionally the script does not have the beat. Keep it distinct
from the three placement verdicts (**ABSENT**, performed nowhere · **UNPLACEABLE**, performed across
a run of scenes with no hinge · **RELOCATED**, performed outside the window) and from §7.2, which is
the opposite reading — there the beats *do* their work and the prose is flat, and the fix is at line
and image level. Here the pages can be excellent and the beat still changes nothing. **The
discriminator: §7.2 asks how the beat is written, §1.0 asks what is different because of it.**

Every test below is a question about the twenty pages that follow, and not one of them mentions a
page number. Run the downstream test (`audit-procedure.md` §1.4) alongside: a beat that passes its
functional test cannot be deleted without rewriting what comes after it.

| Beat | The functional test — run it against the scene | INERT looks like | A library map where the beat passes |
|---|---|---|---|
| **Disturbance** | Name what the protagonist can no longer do after this scene that they could do before it, and name a later page where that unavailability is still binding. If the ordinary world is still available, the scene is information, not a disturbance. | A threat retracted inside its own sequence; bad news the protagonist absorbs and carries on from; an event that changes what the audience knows and not what the protagonist can do. | Erin Brockovich, p.19 (~14%) — the pro-bono file. The A-story it opens **runs p.19 → p.133**; nothing downstream is available without it. Note the split: the situation turns first at p.13 (~10%), and neither event is a decision. |
| **Commitment** | Does the protagonist *choose*, at a cost, with the alternative alive on the page? Name the thing given up and the door that closes. If they could resume the previous life at the end of the scene and nobody would stop them, they were carried. | Agreement with nothing paid for it; a debate that ends in the option the protagonist wanted all along; a cost named in dialogue and never charged. | The Matrix, pp.29–30 (23–24%) — the refused option is spoken at the moment of choosing: "You take the blue pill and the story ends." The map's note is the point: the script gives the hero agency for the *turn* and none for the crossing five pages later (pp.33–34). |
| **Midpoint reversal** | Does the protagonist's method, information or goal change such that **the second half cannot run the first half's engine**? Write the tactic in force in the scene before and the tactic in force twenty pages later. Same tactic, same information, same goal is INERT, whatever sits at the centre. | Escalation — the same pursuit, larger; a revelation the protagonist never acts on; a big set piece at centre after which everybody resumes what they were doing. | E.T., p.62 (55%) — the instructive case because the form is unusual: the stated goal *arrives* at the midpoint rather than reversing, and its arrival inverts the want, *can Elliott keep him?* becoming *can Elliott give him up?* One line of dialogue, no reversal of fortune, and the second half cannot be played on the first half's engine because every act of help is now an act of loss. See §8.5. |
| **Collapse** | Name the object of the loss and name what cannot be rebuilt by the next scene. Then check that *support* goes and not only advantage. | A setback solved within two pages; a loss the protagonist is quietly relieved by; despair with no object attached to it. | Legally Blonde, p.100 (85%) — every achievement is left intact and what dies is the mentor and the female alliance inside ninety seconds (Sarah's misreading, p.101). The move is *poison the achievement rather than remove it*, and the test still passes because something built is seen to die. |
| **Proof** | Recast the decisive action to another character in the script. Does it still play? If any competent person in the cast could perform it, there is no proof. Then: does the action enact the choice the collapse posed, at a cost only this protagonist can pay? | The protagonist present at, and not the cause of, the outcome; the loudest sequence standing in for the decisive one; a climax that only *reports* the result. | Raiders, pp.94–97 (90–93%) — this draft relocates the hero's climax to the rescue: Marion dies in seconds without him, he cuts four bindings with a bayonet, and the Ark reaches Washington only because he lashes it to his whip at p.96. §3.3 and §4.1 hold the negative half of the same case at p.94. |

**How INERT is priced.** As ABSENT, and for the same reason — a beat that does not perform its
function is a beat the script does not have, whatever page it sits on. **An inert midpoint is P0
regardless of placement.** It is the one fault that manufactures the rest: the back half inherits
nothing, so repetition, AND THEN runs and a finale answering the opening question all follow from it,
and every one of them will be misdiagnosed while the measurement table reads *on-plan*. An inert
commitment or proof is P0 on the same logic. An inert disturbance or collapse is P0 if the spine
fails without it, P1 if the function is demonstrably carried elsewhere. Write the verdict in the
measurement table as `INERT (p.N / N%)` — never `on-plan`, which is what a placement-only pass puts
in the cell.

- **Direction** — Never move an inert beat; placement is the one thing it has right. The fix is the
  Direction line of §§1.1–1.5 for the beat concerned, and the finding must say so, because a writer
  told the midpoint sits at 50% and then told the middle sags will move it and make the script worse.

### 1.1 No disturbance
- **Symptom** — "It takes a while to get going." Readers describe the world accurately and cannot say what the story is.
- **Test** — Name the page where the protagonist's situation changes against their will. If the answer is a scene where they *decide* something, the disturbance is absent: a decision is a commitment, not a disturbance. If nothing changes, you have a situation, not a story.
- **Cause** — The writer built a premise (a character in a condition) and mistook it for a plot. Chamberlain's diagnosis: telling a situation, not a story.
- **Direction** — Find the event already implied by the setup and let it happen *to* the protagonist, on the page, early. Ask what the setup's want ironically produces.
- **Precedent** — Erin Brockovich splits it: the situation turns at p.13 (~10%) when she talks her way into a job, and the *problem* — the pro-bono file — arrives at p.19 (~14%). Two separate events, neither of them a decision.

### 1.2 No real commitment (the protagonist is carried into act two)
- **Symptom** — The act-two world arrives but feels unearned; the second act plays as things happening near the hero.
- **Test** — At the act-one break, ask: did the protagonist *choose*, and can they easily go back? If the break is a relocation, an assignment, an arrest or an accident with no refusal phase before it, the beat is a transport, not a commitment. Instant acceptance also fails the test — a debate must precede it or the choice reads as staged.
- **Cause** — The writer plotted the world change and skipped the character's consent to it.
- **Direction** — Give the protagonist a real off-ramp and make them refuse it on the page. The turn should form the question the middle will answer.
- **Precedent** — The Matrix, pp.29–30 (23–24%): the red pill is framed explicitly as a choice between two stories — "You take the blue pill and the story ends." Erin Brockovich runs the opposite and pays for it: the protagonist is fired at ~30% and bottomed out (pp.39–45) so that Plot Point I at pp.45–48 is a *resurrection* rather than a decision — legitimate, but it costs a whole sequence of collapse to buy.

### 1.3 No midpoint reversal — the highest-yield single check
- **Symptom** — "It sags in the middle." The second half feels like more of the first half.
- **Test** — Two questions, in order. (a) Locate the centre beat and compute its percentage; outside 47–55% is an error. (b) Then the harder one: **is the story running the same engine at p.80 as at p.30?** State the dramatic question in force before the midpoint and the one in force after. If they are the same sentence, there is no midpoint regardless of what sits at 50%. Reactive-before / proactive-after is the character-side version of the same check.
- **Cause** — The writer escalated the existing goal instead of turning it. Escalation is not reversal.
- **Direction** — At centre, either flip the protagonist's relationship to the goal, void the goal, or hand the audience information that re-prices everything already seen. Do not add another obstacle.
- **Precedent** — E.T., p.62 (55%): "E.T. phone home" is a **want-reversal**, not an escalation — the first half runs on *can Elliott keep him?*, the second on *can he give him up?*, so every step toward the goal is a step toward amputation. Compare The Matrix, which splits the beat: an audience midpoint (Cypher, pp.60–61) the hero never learns about, and a hero midpoint (the Oracle, p.73 / 58%).

### 1.4 No collapse
- **Symptom** — The third act begins but nothing was risked; the finale feels procedural.
- **Test** — Name what the protagonist *loses* in the 70–85% band. If the answer is "momentum" or "confidence" with no object attached, the collapse is absent. Then check the three components: pain, emotion, and paradox (the character only *seems* furthest from the goal). Placement is weakly measured — individual maps cluster 71–86% — so check for presence, not position.
- **Cause** — The writer protected the protagonist, or spent the low point on plot setback rather than on cost.
- **Direction** — Strip support, not just advantage. Something built must be seen to die; it need not be a person.
- **Precedent** — Legally Blonde, p.100 (85%): the crisis leaves **every success intact** and destroys only her belief that she earned any of them. The general move is *poison the achievement rather than remove it* — which is why the preceding stretch (54–83%) can be played as a winning streak. Note the placement is 17 points later than Snyder prescribes and survives because the cause is single (one man, one gesture) and the solution is planted in the very next scene.

### 1.5 No proof
- **Symptom** — The ending happens; the protagonist is present for it.
- **Test** — At the climax, does the protagonist *do* something whose cost only they can pay, and does it enact the choice the crisis posed? If the decisive action could be performed by any competent person in the cast, there is no proof. A very late climax is normal (Dune pp.107–109 / 97–99%; EEAAO's final image at 99–100%) — flag only absence, never lateness.
- **Cause** — The plot resolves and the character arc is assumed to have resolved with it.
- **Direction** — Make the transformation happen through action under maximum cost, in the same moment the external question is answered.
- **Precedent** — Raiders, p.94 (90%): the Ark is opened and Belloq destroyed **with Indy off-screen, being marched to a wall to be shot.** The draft's own recovery is p.96 — he runs back into the burning tent and drags the Ark out on his whip, so the object reaches Washington only because of him. See §4.1 for the full worked case.

### 1.6 The ending answers a different question
- **Symptom** — "The ending doesn't land," from a reader who cannot fault any individual scene.
- **Test** — Write the dramatic question formed at the commitment. Write the question the climax answers. Compare. If they differ, either the ending is wrong or the commitment is — and Billy Wilder's rule applies: a third-act problem is usually a first-act problem.
- **Cause** — The draft discovered a better story in the middle and never went back to re-ask the opening question. This is often licensed evolution, not failure (see the Audit mode's drift test).
- **Direction** — Decide which question the script actually wants. Then move the *commitment*, not the ending — the ending is usually the honest one.
- **Precedent** — Legally Blonde replaces the stated goal (Warner) with a new one (worth) at p.51 and never argues about it again, so the p.113 refusal of the reconciliation reads as payoff rather than reversal. Erin Brockovich states the terms of its own climax aloud at the midpoint — "find me the evidence to back all this up" (p.68) — which is precisely what is delivered at p.130.

---

## 2. Pacing and placement faults

### 2.1 The saggy second act — and its five distinct causes
The label is useless; the cause determines the fix. Run these in order and stop at the first hit.
- **Symptom** — "It drags after page 40." Readers skim. Often reported as "act two" regardless of where the drag actually is.
- **Test (a): no midpoint** — §1.3. Most common single cause. Fix: turn the centre.
- **Test (b): repetition without escalation** — Do two or more sequences use the same tactic against the same obstacle? "Never the same tactic twice"; each failure must breed a new complication. Fix: rotate variables.
- **Test (c): no subdivision** — Can you name the dramatic question of each 12–15 page block? If the middle is one undifferentiated block, it has no internal shape. Fix: sequences, each with its own question and partial answer.
- **Test (d): the antagonist has no plan** — §3.4.
- **Test (e): the scenes have no wants** — §7.1. This is *not* a structure fault and must not be treated as one.
- **Direction** — Name which of (a)–(e) it is in the finding. A note that says "act two sags" and prescribes a midpoint when the real cause is (e) will make the script worse.
- **Precedent** — Raiders rotates four variables at once across eleven set-pieces — terrain, antagonist, tempo, tool — and never repeats a combination; two of the eleven (the map room pp.56–60, the periscope pp.86–89) have no antagonist and almost no dialogue, placed immediately before the loudest sequences.

### 2.2 The long first act that is only setup
- **Symptom** — "It takes too long to start." Reader impatience concentrated before the break.
- **Test** — The licence question, and it is the only one that matters: **does the material before the break constitute a complete small story — its own question, its own crisis, its own answer — or is it only preparation for the story that follows?** Complete small story: do not flag. Only setup: warn. Never flag on the percentage alone.
- **Cause** — Worldbuilding, or the theme buried behind exposition.
- **Direction** — Either give the pre-break material a question it answers, or cut into the story later. Check whether the theme statement is sitting behind the worldbuilding.
- **Precedent** — The four latest breaks in the corpus all pay the same way. Glass Onion (p.51 / 37–38%) runs an entire fake detective story and then has Blanc destroy it on the page in one speech. Erin Brockovich (pp.45–48 / 33–36%) runs a complete job-hunt story with its own crisis. When Harry Met Sally (pp.43–44 / ~36%) runs three separate complete meetings. Dune (pp.32–33 / 29–30%) contains the gom jabbar as a self-contained test plus the antagonist's plan in plain language at pp.20–21 — and its own map warns the 30% act works "only at epic scale and with a novel's brand equity behind it."

### 2.3 The rushed third act
- **Symptom** — "The ending feels abrupt" — or the inverse complaint, that everything after the collapse happens at once.
- **Test** — Measure the pages after the collapse and count the threads that must close in them. A short third act is not a fault; an *unpurchased* one is. Ask whether the exhaustion work (the hero running out of options) was already done in act two, and whether the solution's mechanism is planted before the finale needs it.
- **Cause** — A late collapse with no pre-staged mechanism, so the finale must both despair and solve.
- **Direction** — Do not lengthen the third act. Move the mechanism earlier and let the finale execute.
- **Precedent** — Legally Blonde runs a 12-page finale after an 85% collapse and a two-page dark night, and gets away with it because the plot's permission slip (Brooke losing faith in Donovan) is planted in the scene immediately after the turn, pp.103–104. E.T.'s act three is 12 pages, 11% of the script, because the death-and-resurrection at pp.98–100 does the work a longer third act would do. Glass Onion plants Klear at p.47, diagnoses it as an explosive at p.92 and hands it over at p.128, so when the courts fail at p.127 the finale reads as consequence rather than escape hatch.

### 2.4 The false climax
- **Symptom** — The script peaks around 65–75% and the real ending feels smaller than what preceded it.
- **Test** — Rank every sequence by scale of consequence. If the largest is not the last, either the finale is under-built or the peak is misplaced. Then the distinguishing question: is the early peak *consumed* by the story — does it change the question — or does it merely exhaust it?
- **Cause** — The writer spent the best idea when it arrived rather than where it was needed.
- **Direction** — Either raise the finale's cost above the early peak, or convert the peak into a reversal that creates the finale.
- **Precedent** — A deliberately *earned* early peak: Only Murders closes its own case at the end of act two — "That's our answer. Suicide" (p.23, 62%) — with fourteen pages still to run, and re-opens it not on evidence but on three separate scenes of loneliness. Glass Onion kills its announced murder-mystery game at pp.50–51 (38%) so the real one has room, and the killing generates the grudge that makes the villain talk.

### 2.5 The ending that arrives after the climax
- **Symptom** — "It has three endings." Readers report the script "keeps going."
- **Test** — Locate the climax, then list every scene after it and what each closes. A scene that closes a live dangling tension is denouement; a scene that adds new information or a new emotional movement is a second ending. Length alone is not the test — count *functions*.
- **Cause** — Subplots that never converged near the climax, now being closed one at a time.
- **Direction** — Converge the threads *before* the climax so the resolution has less to do. Do not simply cut the last scenes; the problem is upstream.
- **Precedent** — Parasite runs twelve pages of resolution (91–100%) across two epistolary movements, a flashback, a fantasy and a final reversal — and needs all three because its argument is that nothing changed, and one ending cannot prove a negative. No Country runs fifteen pages after its protagonist dies at ~p.102 (87%), which its own map concedes is the script's thinnest stretch. When a long tail is *not* argued for like this, it is a convergence failure.

### 2.6 The "two movies" script
- **Symptom** — "It feels like two different films." The reader can summarise both halves and cannot summarise the script.
- **Test** — Name the page in the first half where the protagonist **caused** the second half. If no such page exists, the halves are adjacent rather than connected. Second check: does the second half's antagonist, object or pressure originate in the first half's action?
- **Cause** — A premise that ran out, replaced rather than developed.
- **Direction** — Do not blend the halves. Find the first-half decision that could produce the second half and make it consequential.
- **Precedent** — Parasite is the positive control: the hinge is a doorbell at p.71 (50.4%), and the woman at the door is the housekeeper the Kims got fired at p.51. Every weapon in the last twenty pages was installed as a joke in the first fifty, and the register is graded rather than switched — dread enters at p.44, p.51, pp.59–60, p.70, all before the hinge.

---

## 3. Causality faults

### 3.1 "And then" instead of "therefore / but"
- **Symptom** — "It's episodic." Scenes could be reordered without damage.
- **Test** — Take any three consecutive scenes and insert the connector aloud. If "and then" is the only word that fits between two beats, the chain is broken there. Do this at every act junction first — that is where it usually breaks.
- **Cause** — Beats generated from a list of desired events rather than from consequence.
- **Direction** — Do not add causality by inserting connective scenes. Make each scene's outcome *create* the next scene's problem.
- **Precedent** — Raiders makes the accounting explicit: Indy burns the Flying Wing (p.74), so the Ark must travel by road, which *creates* the truck chase (pp.77–80), which puts it on a boat, which puts him on a submarine. No Country runs its entire middle on one gadget — the transponder, pp.26–59 — so causality is mechanical and visible.

### 3.2 The coincidence that solves rather than complicates
- **Symptom** — "The ending felt convenient." Often reported as a tone problem.
- **Test** — At every point where fortune intervenes, ask which side it favours. Coincidence may *initiate* a story and may *complicate* one; if it resolves one, it is deus ex machina regardless of how well it is written. Rossio's version of the rule: fate should always favour the antagonist.
- **Cause** — The writer needed an outcome the protagonist could not plausibly produce.
- **Direction** — Convert the coincidence into a cost, or give the protagonist the capability earlier so the solution is theirs.
- **Precedent** — No Country puts its biggest coincidence at ~pp.94–96 (est.), where Carla Jean's mother tells a stranger at a bus station where they are going. It kills the protagonist. The plot turns on kindness rather than villainy, and the coincidence complicates absolutely — it solves nothing for anyone.

### 3.3 The protagonist does not cause the ending
- **Symptom** — "It just resolves." Or: the antagonist loses to something other than the hero.
- **Test** — Remove the protagonist from the last twenty pages and re-run the plot. If the outcome is materially unchanged, the ending is uncaused. Then check the sharper question, because it separates two very different faults: is the outcome *decoupled* from the hero deliberately (a force above them settles it), or did the writer simply not give them the decisive act?
- **Cause** — A climax that belongs to a system, an institution or a deity, with no agency bought back for the hero inside the same scene.
- **Direction** — When the outcome must belong to a larger force, buy the protagonist's agency back **inside the same scene** — presence plus one decisive piece of knowledge or action.
- **Precedent** — Raiders is the negative proof and the fix in one document. In this draft Indy is off-screen at p.94 and the bazooka standoff that should have been his decision resolves by a man grabbing him from behind (p.93). The map's verdict names the fault precisely: not a passive protagonist but a **decoupled climax** — and notes that the release cut fixed it with two beats (put him in the room; give him the one piece of knowledge that saves them) at about forty seconds of screen time.

### 3.4 The antagonist with no plan
- **Symptom** — Reported as a second-act sag, or as "the villain is thin." Almost never reported as an antagonist problem.
- **Test** — State the antagonist's plan in one sentence, using only what is on the page. If you must infer it, the audience must too, and the middle has no clock. Second check: does the antagonist attack the protagonist's *specific* weakness, or do they simply obstruct?
- **Cause** — The antagonist was written as opposition rather than as a person with their own campaign.
- **Direction** — Put the plan on the page early, in the antagonist's own mouth, and let the audience watch it run.
- **Precedent** — Dune states the Baron's plan as a proverb at pp.20–21 (18%) — "To break a virtuous man, give him a burden too heavy to bear" — and seals it at pp.42–44, roughly forty pages before it detonates. The second act runs on a countdown the audience can see and the characters cannot. The counter-case is Erin Brockovich, whose A-story has **no scene in which the antagonist states its own goal**: PG&E is a building, a fax recipient, an escalating grade of lawyer and a 1966 memo — legitimate, because the obstacle is institutional by design, but it forces the script to supply pressure from the domestic B-story instead.

---

## 4. Character-structure faults

### 4.1 The passive protagonist — with the worked case
- **Symptom** — "Things happen to them." Readers say the hero is likeable and the script is inert.
- **The critique, stated fairly** — A protagonist who reacts rather than pursues generates no story; every win is cancelled without their agency mattering; remove them and the plot proceeds. Passivity is permissible early and is conventionally fatal after the midpoint. Comedy tolerates it longer, but another character must push the hero back to agency before the resolution.
- **Test** — Three separate checks, and they give different answers, which is the point. (a) **Initiation**: count scenes the protagonist enters with an intention. (b) **Causality**: remove them and re-run the plot (§3.3). (c) **The dramatic question actually in force**: passivity measured against the wrong question produces a false positive.
- **Cause** — Genuine cases: the protagonist has a condition, not a want. False positives: the auditor measured agency against the plot's object rather than against the question the script is asking at that point.
- **Direction** — Confirmed cases: give the protagonist a want that requires action against opposition, early. Decoupled climaxes: §3.3.
- **Precedent — the worked case.** Raiders' map argues both sides and its verdict is the model for how to report this fault. **Stronger in one place:** Indy is absent from the climax (p.94) and does not witness, cause or suffer it. **Collapses in three:** (1) it measures the wrong question — after p.85 the operative question is *will Marion live*, and on that he is 100% causal, cutting four bindings with a bayonet a foot from burning oil (p.95); (2) he determines the time and place of the climax — burning the Flying Wing reroutes the Ark to the road, the truck to the sea, the sea to the island, so without him Belloq opens the Ark in Berlin in front of Hitler; (3) in this draft he is necessary for its recovery (p.96). Verdict: **"Partly true at the climax; false about the film."** The transferable form: name which of the three checks failed, and never let a failure on one imply the others.

### 4.2 Want and need not distinguished
- **Symptom** — The arc feels stated rather than dramatised; or the ending gives the protagonist everything and feels hollow.
- **Test** — Write the want (external, visible, achievable) and the need (internal, usually unconscious) as two separate sentences. If they are the same sentence, or if the need is a restatement of the want in nicer words, they are not distinguished. Then: does the climax force a choice between them?
- **Cause** — The theme was decided but never given a competing object.
- **Direction** — Make the want obtainable and the need only obtainable at the want's expense. The classic resolution is failing the want and winning the need.
- **Precedent** — E.T. runs the collision as its whole second half: Elliott's want is to keep, his need is to release, and from p.62 every act of help is an act of loss. Ted Lasso runs the extreme case — the hero **states no want in 39 pages**, not one line of "I want" — and substitutes dramatic irony: the audience learns at p.21 (54%) that Rebecca wants him to fail, seven pages before the BELIEVE sign at p.28 (72%). Reverse that order and the sign is a slogan.

### 4.3 The arc completes before the climax
- **Symptom** — The last act feels like a formality; the climax is exciting and weightless.
- **Test** — Find the page where the protagonist last changes internally. If it precedes the climax by more than a few pages, the climax has nothing to prove. Check the B-story too — if the relationship that carries the theme resolves early, the finale is unopposed.
- **Cause** — The writer resolved the emotional line at the collapse and left the plot to finish alone.
- **Direction** — Hold the final piece of self-knowledge until the moment it must be enacted under cost.
- **Precedent** — Erin Brockovich deliberately resolves its B-story *before* the climax — George at p.121 and Matthew at p.125 — precisely so that the win at p.130 is not the reward for family repair. That is the controlled version. Contrast The Matrix, which strips the credential instead: at PP II (p.95 / 75%) Neo flatly rejects the prophecy — "I'm not the One, Trinity" — and goes anyway, entering act three with the arc deliberately incomplete.

### 4.4 The protagonist whose absence would not change the outcome
- **Symptom** — Usually reported as "I don't know whose story this is."
- **Test** — For each candidate lead, delete them entirely and describe what still happens. The protagonist is the one whose deletion changes the outcome — not necessarily the one with the most pages.
- **Cause** — An ensemble in which the writer's favourite character is not the causal one; or a witness protagonist written as though they were an agent.
- **Direction** — Either give the character causal weight or accept the witness structure and build for it — which requires the witness to own the frame from page one.
- **Precedent** — No Country makes the witness structure work by declaring it: Bell **affects nothing** — its own map calls this "the point and also the most-argued weakness" — and the script licenses it by giving him pp.1–3 in voice-over before he owns a single scene, then delaying his physical entrance to p.28 (24%). Screen-presence totals: Moss ~52%, Chigurh ~39%, Bell ~34%. **Bell has the fewest pages and the most authority.** If the final POV has not spoken by the end of act one, it cannot inherit the ending.

---

## 5. Storyline faults

### 5.1 The thread that never converges
- **Symptom** — "The subplot goes nowhere," or an act three that has to stop and close things.
- **Test** — For every storyline, name the page where it touches the A-story in a way that *changes* the A-story. Proximity is not convergence; two threads in one scene that do not affect each other have not converged. Threads that never rejoin are a defect.
- **Cause** — A thread built for texture or theme and never given a plot job.
- **Direction** — Give the thread one moment where it supplies the A-story something it cannot get elsewhere — information, an object, an obstacle, or a person.
- **Precedent** — Legally Blonde converges everything physically in one room at pp.105–107 and uses each ally: David for Rule 3:03, Emmett for the supervision, Brooke for the firing, Sarah for the blessing. Desperate Housewives turns four independent stories into one Friday with a single overheard line in a Starbucks queue at p.44. The deliberate counter-example is Mare of Easttown, which re-arms the prowler thread at p.60A and leaves it armed — a limited series can bank a thread; a feature cannot.

### 5.2 The B story that carries no theme
- **Symptom** — "The subplot is fine but it feels like a break from the movie."
- **Test** — State the theme as a debatable proposition. Then ask what the B-story argues about it. If the B-story's answer is the same as the A-story's, it is decoration; if it has no answer, it is filler. The B-story character should be able to state the theme back to the protagonist at the crisis.
- **Cause** — A romance or friendship added for warmth rather than for argument.
- **Direction** — Make the B-story a second, incompatible answer to the same question, held by someone the protagonist cannot dismiss.
- **Precedent** — Legally Blonde's Emmett states the theme back at the dark night — "What if you're trying to be something you *are*?" (p.102) — and his throwaway line "have a little faith" (p.80) returns in the climax (p.109). Its C-story (Paulette) is a class mirror: the same wound without the money, and the first character to say the thesis aloud. Russian Doll installs its cure in a supporting character's mouth at p.8 — "Only our natural capacity for love can master sadistic destruction" — so the pilot can leave the change unpaid without leaving the theme unstated.

### 5.3 Subplot bloat
- **Symptom** — Page count high, forward pressure low; the reader loses track of who is where.
- **Test** — The cuttability test, applied honestly: remove each subplot entirely. If the A-story survives unharmed, the subplot is not earning its pages. Then a second pass — count how many *pages* each thread costs against how many *A-story changes* it produces.
- **Cause** — Every character was given a story because every character was interesting.
- **Direction** — Merge before you cut. Two thin threads that share a function usually want to be one thread with a person in it.
- **Precedent** — The Office pilot runs three interleaved runners at deliberately different speeds — Michael's induction of Ryan (which supplies the climax's motive), the Jim/Dwight war (which supplies the laughs), the downsizing threat (which supplies the stakes) — with no printed act architecture at all; momentum comes entirely from the speed differential. Nothing is cuttable because each runner does a different job.

### 5.4 The ensemble where one lead's story is an A-story in disguise
- **Symptom** — "It's an ensemble" — but readers report the script belongs to one character, or that one thread makes the others feel like interruptions.
- **Test** — For each lead, ask: does this storyline own a dedicated antagonist physically present in the world, and does it borrow its stakes from another thread? A thread that borrows its stakes is a B-story wearing an A-story's clothes. Genre is the second discriminator — four instances of one genre read as one story with three echoes.
- **Cause** — Equal page counts mistaken for equal weight.
- **Direction** — Either give the weak threads their own antagonist and their own genre, or stop calling it an ensemble and build the hierarchy deliberately.
- **Precedent** — Desperate Housewives keeps four A-stories genuinely parallel by giving each a different genre and a different antagonist physically present in the world: rom-com with a rival (Susan/Edie), domestic farce (Lynette/her children), marital drama (Bree/Rex), adultery caper (Gabrielle/Carlos). Mare of Easttown is the honest inverse — its map names the grief spine as the true A-story with the case as delivery mechanism, and calls Erin's thread "a second protagonist thread, not a subplot," meeting the A-story only once (p.56).

---

## 6. Contract faults

### 6.1 Missing obligatory scenes
- **Symptom** — "It's well written but unsatisfying." Genre readers report it more reliably than general ones.
- **Test** — Run the genre's obligatory-scene list from `../../story-structure/references/genre-contracts.md`. For each absent scene, ask the only question that matters: **is the absence argued for, or is it an oversight?** A withheld obligatory scene must be visibly refused, not merely missing.
- **Cause** — The writer wrote toward the story's interest and away from the genre's promise.
- **Direction** — Deliver the scene, or make the refusal itself the argument — which costs more setup, not less.
- **Precedent** — Parasite refuses the confrontation its premise promises: the Kims and the Parks never have a single scene of open conflict in 141 pages, and the collision is displaced onto the family one floor down. That is the film's controlling idea expressed as a structural refusal. No Country promises its obligatory scene *aloud* on the telephone at ~p.85 (est.) and never pays it — legitimate only because 85% of the pages built an immaculate archplot first, the substitute protagonist narrated pp.1–3, and elided violence was rehearsed three times before being applied to the climax.

### 6.2 Format violation — a feature with a series premise
- **Symptom** — The script ends and the situation is intact; or every act ends by opening something.
- **Test** — At the last page, ask whether the engine that generated the story is switched off. A feature answers its question; a pilot installs a machine that can ask it again. If the ending restores a repeatable condition, the material is a series.
- **Cause** — A premise with a renewable generator, written to feature length.
- **Direction** — Either close the engine, or accept the format and rebuild for episodes.
- **Precedent** — Compare the two ends. Russian Doll's pilot deliberately ends the circle at RETURN and withholds CHANGE, because a completed arc in episode one would close the engine; Nadia ends knowing *less* than she started. Legally Blonde does the opposite — its final image measures the institution's conversion, not the hero's, which is why the story is over.

### 6.3 Format violation — a pilot with no engine
- **Symptom** — "Great episode, no show." Readers cannot describe episode two.
- **Test** — Describe episode two using only what the pilot established. If you must invent a new generator, the engine is missing. Then check whether the engine is *felt* early even when it is *explained* late — those are different requirements and only the first is mandatory.
- **Cause** — A strong premise (a situation) mistaken for an engine (a repeatable story generator).
- **Direction** — Name the machine, the renewable friction and the permanently available cast positions. Install them, then decide how late to explain them.
- **Precedent** — Severance's draft explains its engine at pp.42–43 (79–81%) and makes it *felt* from p.1; its series engine has eight named components, including a locked exit with a stated key — "Both halves of you would need to request it" (p.48) — which is a finish line the audience can see and the characters cannot reach. The Rookie installs three permanently mismatched two-handers in twelve lines on p.10. Poker Face installs the constraint that makes weekly episodes possible at p.30 (46%) — "the trick is figuring out why someone's lying" — deliberately crippling the gift so it cannot solve the show. The negative case is in the corpus too: the Seinfeld pilot's signature architecture — the stand-up bracketing, the diner, the four-hander — is **not yet invented**, and the stand-up spine exists only as `(MONOLOGUE TO COME)` on p.44.

### 6.4 The act-out that does not survive a break
- **Symptom** — The act break lands, and the reader feels no pull to continue.
- **Test** — At each act-out, ask what unanswered thing the viewer is returning for. It does not have to be jeopardy. **Never flag an act-out for lacking a cliffhanger** — three of Breaking Bad's four act-outs are transgressions rather than danger (Walt pointing a gun at approaching sirens p.3, blackmailing Jesse p.31, assaulting a teenager p.43), and three of Severance's five are stillness (a door opening p.4, a silent room p.27, two jailers waiting p.52). The real test is whether the button reveals something about a character that the viewer wants resolved.
- **Cause** — The act-out was placed at the biggest event rather than at the most character-revealing one.
- **Direction** — Choose the button for what it exposes, not for what it withholds.
- **Precedent** — Abbott Elementary does the inverse of the obvious move: its biggest reversal (Ava's sign, p.22 / 65%) is deliberately *not* the act-out, because two further pages convert it into Janine's own mistake so the act buttons on self-inflicted humiliation. Its comedy act-outs run on embarrassment — p.24 promises a mandatory lunchtime "trust workshop… It's going to be FUN." Dread, not danger.

### 6.5 The pilot that never proves episode five exists
- **Symptom** — The pilot is complete and the series is not. Distinct from 6.3: the engine exists but has only been shown once.
- **Test** — Ask what the pilot *demonstrates* rather than *promises*. A promise is a line of dialogue about the future; a demonstration is the machine running and producing a result the audience can extrapolate. Check whether the pilot proves the format is not a treadmill.
- **Cause** — The writer spent the pilot installing and never ran the engine to a visible outcome.
- **Direction** — Run the machine once, to completion, and let it produce something the audience did not expect — ideally by disproving the obvious reading of the format.
- **Precedent** — Russian Doll proves the loop is bendable at p.26 (87%) by having John pull Nadia clear of the car that killed her, and disproves its own false quest on the same page it grants it (p.27, 90%) — the cat is found and she dies anyway. Both moves exist to show the series is not a puzzle to be solved. Only Murders defers the mystery machinery out loud at p.35 — "So tomorrow we lay out a timeline?" — and makes the private wounds the engine of the case, which is the thing that will still be true in episode five.

### 6.6 The stated genre is not the genre on the page
- **Symptom** — The pitch and the pages describe two different films. Readers say "it's good, I don't know what it is" or "I don't know who this is for"; a genre reader reports obligatory scenes missing that the writer never intended to write; coverage names a genre the writer would not have named.
- **Test** — Run the §6.1 obligatory-scene pass **twice**, side by side: once against the stated genre and once against the genre the pages actually deliver. Name the second one from the midpoint and the finale, never from the premise — the fast version is the premise-drift check in `../../story-structure/references/genre-contracts.md` §1 (name the genre from the logline, from the midpoint, from the finale; three different answers is the finding). **The genre whose scenes are present is the genre on the page**, and the count is the evidence: cite how many of each list land, with pages. Two discriminations before naming it. If neither list is more than half present, this is not mislabelling but a script running two spines — a hybrid still needs one. And if the mismatch is staged, dated and never revisited, it is a graft, not a fault (§8.4).
- **Cause** — Usually the label was fixed at the pitch and the draft went where the material was alive. The inverse also occurs and is worth separating: the genre was chosen for the market, the writer has no appetite for its obligatory scenes, and so those scenes were written thin or skipped — which reads as the same symptom and takes the opposite fix.
- **Direction** — **Change the label before you change the script.** Ask which list the script wants to complete; if the pages are delivering the unstated genre well, restate the genre and audit against that contract, and the note that follows is usually three missing scenes rather than a rewrite. Only when the stated genre is load-bearing — a commission, a package, a market position — is the fix on the page, and then it costs the obligatory scenes in full and the script must want them. Never split the difference.
- **Precedent** — Legally Blonde's map runs exactly this test and changes the label rather than the script: the first 25 pages are Rites of Passage (a heartbreak, a mourning montage, a grief-driven plan), and the map disqualifies that reading on one question — **the heroine does not change; the institution does** — which forces Fool Triumphant and explains why the back half inverts Snyder. The seam is visible and dated: the Boxster hits Harvard Yard at p.25 (21%), and it is never revisited. Mare of Easttown is the declared version: its own map names the grief spine as the true A-story with the case as delivery mechanism, and the body does not arrive until ~98% — audited as a murder mystery, episode one is missing nearly every scene it owes; audited as what it is, the missing scenes are the design.

---

## 7. Structure-shaped problems that are not structure problems

**This is the section that prevents the most damage.** Three faults present as structural sag and are made *worse* by structural notes. In each case the test is diagnostic, and the routing matters more than the naming.

### 7.1 Scenes where nobody wants anything
- **Symptom** — Identical to a second-act sag: "it drags," "nothing is happening," often with correct beat placement.
- **Test** — Take five consecutive scenes in the dragging stretch. For each, answer Mamet's three questions: **who wants what from whom, what happens if they don't get it, and why now?** If two or more scenes cannot answer all three, this is a want problem, not a structure problem. Confirm it: does the drag persist even in scenes that sit exactly on a load-bearing beat? If yes, moving beats will not fix it.
- **Cause** — Scenes written to convey information or mood rather than to be transactions.
- **Direction** — Do not move beats. Give each scene a character who wants something from another character now. **Route to `screenplay-dialogue`** for scene-level intention and obstacle work; where the scene is largely wordless, **route to `screenplay-action`**.
- **Precedent** — The Bear places two pages with no plot in them at pp.27–28 (73–76%), immediately after its loudest scene, and they are the strongest pages in the episode — because both characters want something specific from each other. Lady Bird runs 124 scenes averaging 0.91 pp with no goal-obstacle spine at all, and composes pressure with length instead: pp.40–50 run 24 scenes at 0.44 pp average, pp.70–80 run 6 at 2.08 pp. Neither script is sagging; both would be destroyed by a midpoint note.

### 7.2 Inert execution of correct beats
- **Symptom** — The audit measures clean. Every beat is present and within tolerance. The script is still dead.
- **Test** — This is the check the measurement pass cannot perform: **placement is the only property the corpus measures.** If the spine is intact, the tolerances are met, causality holds, and the reader is still bored, stop looking for a structural cause. Confirm by sampling: read three pages at the midpoint and three at the collapse. If the beats are doing the right work and the pages are flat, the fault is at line and image level. **Rule out §1.0 first** — an INERT beat also measures clean and also reads dead, and the two route in opposite directions. Run the functional tests: if the beats change nothing downstream the fault is structural and belongs in §§1.1–1.5; only when they pass is this entry the right one.
- **Cause** — The writer built correctly and wrote without pressure — dialogue that states, description that inventories.
- **Direction** — Say so explicitly in the finding, and do not prescribe more structure. **Route to `screenplay-dialogue`** for line-level work and **`screenplay-action`** for description, pacing on the page and visual storytelling.
- **Precedent** — Everything Everywhere All at Once lands eleven of fifteen Save the Cat beats within three points of Snyder and three exactly; its apparent formlessness is entirely in the *content* of the beats, not their placement. The corollary is the warning: **a script can be perfectly placed and dead.** Position is a diagnostic prompt, never a verdict.

### 7.3 A voice problem reading as a scene problem
- **Symptom** — "The scenes don't work." Often localised to scenes involving one or two characters, or to a whole act after a character joins it.
- **Test** — Strip the character cues from a page of dialogue and ask whether the speakers are still identifiable. If they are not, the scene is failing for want of differentiated speakers, not for want of shape. Second check: does the same *structural* beat work when a different character carries it? If yes, the fault travels with the person, not the position.
- **Cause** — Cast members sharing one register, or a character whose voice drifted across the draft.
- **Direction** — **Route to the `screenwriting-voices` plugin** — `character-voice` to build or extract the spec and run a workup, `voice-dialogue` to audit consistency across the draft. Do not restructure scenes to compensate for undifferentiated speakers.
- **Precedent** — The Office pilot delivers 100% of stated interiority through the talking-head interview: not one of the four principals ever tells another human being what they want. That works only because each interview voice is distinct enough to carry a whole want alone. Russian Doll runs the reverse experiment on purpose — the same seduction lines are moved from one man's mouth to another's (p.6 → p.23) and land as a joke *because* the voices differ.

---

## 8. False positives — deviations that look like faults and are not

Each of these appears in the measured corpus, in scripts that work. The entry gives the test for whether *this* instance is the earned version or the accidental one.

### 8.1 A first-act break at 33–38%
- **Looks like** — A long, indulgent first act.
- **Not a fault when** — The pre-break material runs a complete small story. Four canonical scripts sit here: Glass Onion 37–38%, When Harry Met Sally ~36%, Erin Brockovich 33–36%, Dune 29–30%.
- **Test** — §2.2's licence question. Also check the mirror case: an *early* break (The Father and No Country at 10–11%, Parasite ~11%, Lady Bird 13%) buys a long undirected second act in which the audience does not know what kind of story it is watching. Ask what the undirected stretch is *for*. If the answer is "the writer had nothing to withhold," warn.

### 8.2 The protagonist dies or exits before the end
- **Looks like** — A structural collapse; an abandoned premise.
- **Not a fault when** — The successor was planted before the audience knew there was one, and the handoff is staged rather than announced.
- **Test** — Locate the successor's first appearance. No Country gives Bell pp.1–3 in voice-over with no scene attached, delays his body to p.28 (24%), and at the handoff (~pp.101–103, 87%) cuts to *Bell's car* rather than from Moss alive to Moss dead — so the audience is already inside the successor's approach when the protagonist dies. Parasite hands off at p.89 and says so on the page: "No longer the man with the plan. He just does as he's told." Handoff at ~87% has precedent (n=2); it is a choice, not a fault.

### 8.3 A withheld climax
- **Looks like** — A missing third act.
- **Not a fault when** — Three conditions hold together, and all three are required. (1) The contract was honoured first — you can only withhold a climax you have actually built. (2) The substitute was planted early. (3) The grammar of the withholding was established as a local device before being applied globally.
- **Test** — No Country supplies the checklist: pp.1–101 are a conventional pursuit thriller at the highest level (working ticking device, hard midpoint at pp.57–59, competent proactive hero); Bell's voice opens the script; and elided violence is trained across three deaths — Wells (~p.83), Moss (~p.102), Carla Jean (p.112, conveyed by a man checking his boots) — before it is applied to the climax. **A structural choice that appears once looks like a gap; the same choice rhymed three times reads as a thesis.** If any one condition is missing, it is a fault.

### 8.4 A genre change mid-film
- **Looks like** — Two movies (§2.6).
- **Not a fault when** — The second genre is caused by the first, planted inside the first genre's furniture, and graded rather than switched.
- **Test** — Parasite's three conditions. **Causality:** the intruder at p.71 is the housekeeper the protagonists destroyed at p.51 — the thriller is the caper's bill. **Thematic priority:** the discovery is not a monster but a poorer family, which completes the satire's argument rather than betraying it. **Constant authorial signature:** same setups, same music-cue-driven sequences, same deadpan blocking. Register moves; voice does not. The distinguishing question remains §2.6's: name the page where the protagonist caused the second half.

### 8.5 A midpoint that is a want-reversal, not a plot reversal
- **Looks like** — A missing midpoint; nothing "happens" at centre.
- **Not a fault when** — The protagonist's relationship to the goal inverts, even if the plot's obstacle does not escalate.
- **Test** — Compare the pre- and post-centre dramatic questions (§1.3). E.T.'s p.62 (55%) is the model: no reversal of fortune, one line of dialogue, and the question flips from *can he keep him?* to *can he give him up?*. Parasite's p.71 goes further and **voids** the goal rather than escalating it, which is why a three-act pass mislabels it a midpoint and hides the protagonist handoff. If the question is unchanged, it is a fault regardless of how large the event is.

### 8.6 Repetition as structure
- **Looks like** — Padding; scenes the reader has already read.
- **Not a fault when** — What compresses is the repeated material *inside* the unit, not the unit; verbatim repetition is rationed; and the protagonist's knowledge is the one variable that never resets.
- **Test** — Russian Doll's counter-intuitive measurement: **the loops do not get shorter.** Loop A is ~12.6 pp, Loop B is ~14.2 pp — 1.6 pages *longer*. The fixed sequence inside falls 8.7 → 5.4 → 3.0 pp and the freed pages are respent on new material. Hold the runtime, change the contents. Check also for the five supporting mechanisms: the audience learns the rule before the protagonist (p.13 vs p.20); each repeated scene is re-entered at a different point in itself; verbatim text is rationed to about six short units; recycled dialogue is reassigned to a new mouth; and the script demonstrates it will elide by cutting a repeated line off mid-word (p.28).

### 8.7 Other deviations worth checking before flagging
- **No printed act breaks (TV).** Never infer a problem from their absence, nor sound structure from their presence. Severance prints four acts on a streaming show; This Is Us prints nothing on a network hour and its inferred act lengths (8.5 / 9 / 10 / 9 / 8.3 / 8.1 pp) are more regular than several scripts that do print them.
- **Wildly unequal acts (TV).** The Rookie's act one is 35% of the script; Severance's act two is 30%. Ask whether the long act is doing extra work, not whether it is long.
- **No locatable midpoint.** A real reading, not a gap. Oppenheimer's map names none, attaching centre language to three non-overlapping blocks — the honest answer for a film built on two interleaved timelines.
- **A script that disclaims act structure and still has one.** The Father opens "the script has no act structure in the conventional sense" and then names both turns (pp.9–10 / 10–11%; pp.44–46 / 51–53%). Aftersun declares both turns absent from the holiday body and relocates them to a 4.8-page memory frame (p.21 / 21%; p.48 / 48%). Even scripts that refuse the paradigm keep a middle — measure the frame, not just the body.
- **Printed acts that do not match dramatic acts.** Weird City's act one ends at p.13 but its point of no return is p.19; the printed breaks are *engine changes*, not turning points. Legitimate short-form structure that would read as broken against a standard four-act grid.

---

## 9. The common-mistakes linter

A fast pass. Each line is a yes/no check against the page; every hit routes to a numbered entry above. Run it after measurement, before writing findings.

| # | Check | Routes to |
|---|---|---|
| 1 | Cut the first 10–20 pages — does the story still work? | §2.2 |
| 2 | Is the disturbance located, and does it happen *to* the protagonist? | §1.1 |
| 3 | Does the second act repeat tactics without escalating? | §2.1(b) |
| 4 | Does "therefore" or "but" fit between every pair of beats? | §3.1 |
| 5 | Does any scene stop the story for a detachable character moment? | §7.1 |
| 6 | Is any tactic used twice? | §2.1(b) |
| 7 | Does any event out-scale the one that follows it? | §2.4 |
| 8 | Is the resolution caused by a protagonist choice? | §3.2, §3.3 |
| 9 | Is the protagonist reactive after the midpoint? | §4.1 |
| 10 | Is there a turn at the centre, and does the engine change? | §1.3 |
| 11 | Does the collapse cost something concrete? | §1.4 |
| 12 | Do all threads converge at or before the climax? | §5.1, §2.5 |
| 13 | Are there new plants in act three, or unpaid plants from act one? | §2.3 |
| 14 | Does the tone contract change after establishment? | §2.6, §8.4 |
| 15 | Are beats hit while nothing original happens in them? | §7.2 |
| 16 | Is this a situation rather than a story? | §1.1 |
| 17 | Can the antagonist's plan be stated from the page alone? | §3.4 |
| 18 | Do the want and need differ, and does the climax force a choice? | §4.2 |
| 19 | Are the genre's obligatory scenes present, or visibly refused? | §6.1 |
| 20 | (TV) Does the pilot demonstrate the engine, not just promise it? | §6.3, §6.5 |
| 21 | Does every located beat pass its *functional* test, not just its placement? | §1.0 |
| 22 | Does the genre named from the midpoint and the finale match the stated one? | §6.6 |

**Before reporting any hit:** ask what the deviation buys. The best scripts in the corpus deviate
most, and the corpus skews toward produced and acclaimed work — it can say what working scripts did,
never that a script doing otherwise will fail.
