# AI Tells in Dialogue

Scanner reference for the `voice-dialogue` judge: the catalog of machine-flavored dialogue patterns, plus the rules for firing on them without punishing designed voices.

## Contents

1. Why this exists
2. How to run the scan
3. The catalog — A. imported prose patterns; B. fiction-native patterns; C. dialogue-specific patterns
4. Severity and density rules
5. Exemptions and false positives
6. Uniformity metrics — distributional signals that outlive word-lists
7. Rewrite rules
8. Licenses and attribution

## 1. Why this exists

LLM-drafted dialogue survives a casual read and fails a professional one. Every character is fluent and every
answer cooperates; scenes arrive pre-shaped, sanded smooth. Human speech does none of this — people interrupt,
dodge, reuse a word because it is the right word, trail off mid-clause. This file maps the sanding marks.

## 2. How to run the scan

The whitelist exists before the first line of dialogue is read; the order below is the procedure.

1. **Load voice specs first.** Read every `<name>.voice.md` for the scene's speakers (format:
   `../../character-voice/references/voice-md-template.md`; specs usually sit in a `voices/` folder).
2. **Build the per-character whitelist** from each spec: Origin & Register Map features (L1
   interference, dialect grammar — each with its worked example), Idiolect Kit tics and signature
   move, Speech DNA markers (openers, tags, address), Under Pressure deltas. Whitelisted features
   are invisible to the scanner.
3. **Unspecced characters:** read their dialogue once before judging. A feature one character uses
   consistently reads as design — log it as a spec candidate; a cast-wide feature stays flaggable.
4. **Note the register contract** — the format/genre profile (section 4) that licenses certain
   symmetries script-wide. Then scan dialogue, parentheticals, and attribution in action lines.
5. **Fire by rule, not by sighting** (section 4): P0 on first confirmed instance, P1 on density, P2
   in full audits only. "Confirmed" means the hit survived the whitelist and the section 5 exemptions.
6. **Report as craft notes** — scene and page, tell name, quoted line, direction ("p. 34, DEREK:
   template phrase, tell 4, second this scene — P1 fires; cut the armature"). Never an authorship
   accusation, never an "AI score": these patterns are signals, and signals only. Human writers produce
   every one of them, and an edited machine draft comes out scrubbed; confidence would take several scripts.

## 3. The catalog

Severity: **P0** = scene-killer, first confirmed instance; **P1** = strong tell, fires on density (2+ per scene or 3+
per 10 pages); **P2** = polish-level, audit-only. Sources: [AAW] conorbronsdon/avoid-ai-writing (MIT, section 8);
[WP] Wikipedia "Signs of AI writing"; [RC] recordcrash; [DRV] original to this suite. All BAD examples are project-written.

### A. Imported prose patterns (they transfer straight into mouths)

#### 1. Negative-parallelism reveal — P0 [AAW#12][WP][RC]
The "It's not X — it's Y" frame with its split ("This isn't anger. This is grief.") and countdown ("It's not the
money. It's not the house. It's us.") variants. The most universal tell across models; every character becomes an essayist.
> MARA: This isn't about the affair, Tom. It's about trust.
> TOM: And trust isn't something you rebuild. It's something you excavate.
- Fix: keep the Y, cut the scaffold — or let her say the wrong thing. Budget: one per script, earned.
#### 2. Rule-of-three compulsion — P1 [AAW#17][WP][RC]
Triadic lists in speech after speech. Humans mostly list in twos or ramble past the third item.
> DEV: You were cold, distant, and cruel.
> LIA: And you were absent, evasive, and drunk.
- Fix: vary group size — stop a list at two, or let it collapse mid-delivery.
#### 3. Synonym cycling — P1 [AAW#19][WP]
Rotating synonyms to dodge repetition; real speakers reuse the clearest word, and the reuse IS voice. Also fires
on attribution epithets in action lines ("the older man," "the detective" for one named character).
> COP: Drop the weapon! Slide the firearm over here!
> COP (CONT'D): I said lose the piece!
- Fix: pick the character's word and let them hammer it; in action lines, use the name.
#### 4. Template phrases — P1 [AAW#21]
Slot-fill armatures with nouns swapped in: "Whether you're [X] or [Y]...", "At the end of the day, [platitude]."
> CHIEF: Whether you're a rookie or a twenty-year vet, this city changes you.
> ROOKIE: A sobering reminder that no one is immune.
- Fix: replace the armature with a sentence only this speaker could build.
#### 5. Hedge stacking — P1 [AAW#15,#43]
Hedges piled into one clause (modal + hedge adverb + softener). One hedge is character; three is filler.
> ANA: I think maybe we could perhaps try to possibly reach out to him?
> BEN: That could potentially be worth considering, I suppose.
- Fix: keep the strongest hedge, delete the rest. A written-as-timid character gets ONE, used consistently.
#### 6. Aphorism formula — P1 [AAW#35][WP]
Greeting-card abstraction where a concrete stake should be: "X is the language of Y," "a testament to it all."
> EVE: Grief is just love with nowhere to go.
> SAM: Then this house is a testament to everything we never said.
- Fix: trade the abstraction for the specific thing at risk in this scene.
#### 7. False ranges — P2 [AAW#28]
"From X to Y" spanning unrelated extremes for fake sweep.
> RIO: I've seen it all in this job — everything from jaywalking to cartel hits.
> KIM: From the mailroom to the boardroom, nothing surprises me either.
- Fix: name the actual middle instead of the span.
#### 8. Manufactured staccato — P1 [AAW#36]
Three-plus same-shape clipped fragments for unearned punch.
> VOSS: No warning. No mercy. No survivors.
> HALE: No plan. No backup. No choice.
- Fix: keep one fragment, fold the rest into a sentence. Budget: one staccato run per script.
#### 9. Infomercial hooks — P1 [AAW#27]
Self-teasing setups: "The catch?" "Here's the thing." Real people say these — flag only when several characters
share the tic or it opens beats mechanically.
> JAY: The catch? He never left the building.
> MO: And the kicker? Neither did she.
- Fix: license the hook to one character as a tic, or let the information land unannounced.
#### 10. Chatbot register leakage — P0 [AAW#55,#57,#30][WP]
Assistant-speak in a character's mouth: "Great question." "I hear you, and that's valid." "Let me break down what
happened." Instant kill unless the character IS an AI (section 5, in-world carve-out).
> DET. CRUZ: Walk me through that night.
> WITNESS: Absolutely, great question. Let me break down the timeline for you.
- Fix: delete the service framing; answer or deflect in the character's own register.
#### 11. AI-frequency vocabulary — P1 [AAW Tier 1A][WP]
Markers running 5–20x above human baseline: delve, tapestry, realm, seamless, pivotal, "rich cultural heritage,"
landscape and navigate as metaphors. Ordinary characters suddenly talk like brand copy.
> NINA: We need to navigate this ever-evolving landscape of our marriage.
> PAUL: It's a testament to our resilience that we're still delving into it.
- Fix: swap each marker for the word this character would actually reach for.
#### 12. Brochure verbs — P2 [AAW#24][WP]
"Serves as," "boasts," "features," "stands as" where a person says "is" or "has." Nobody speaks real estate.
> AGENT: The den serves as a sanctuary and boasts a wood-burning fireplace.
> BUYER: And the garden? Does it also serve as something?
- Fix: restore the plain copula.

### B. Fiction-native patterns

#### 13. Self-poisoning repetition — P1 [RC#1]
The model locks onto a syntactic frame and keeps feeding it; humans give a frame a rest once they hear it, while
models double down on whatever matched the previous paragraph.
> ROSS: Knowing what I know now, I'd never have signed.
> BETH: Seeing what I've seen tonight, neither would I.
- Fix: rebuild openings until consecutive speeches stop sharing a shape.
#### 14. Verbose/curt oscillation — P2 [RC#4]
Ornate simile-heavy flights slamming into tiny cliché sentences, with no middle register between them.
> OWEN: My doubt was a cathedral, vast and echoing, every pillar a year of our silence.
> OWEN (CONT'D): It had to end. Simple as that.
- Fix: find the character's true register and grade the transitions through it.
#### 15. Metaphor stacking — P1 [RC#3,#5]
Two or more metaphors for one referent inside a single speech.
> IRIS: Her absence was a wound, a hollow bell, a winter with no thaw.
> NOA: For me it was more of a locked door. A sealed vault. A closed fist.
- Fix: keep the strongest image, cut its understudies. One image per idea; let it land.
#### 16. Blocky dialogue/action segmentation — P2 [RC#6]
Speech, one action beat, speech, alternating like gears — dialogue never interrupted BY action, action never
arriving mid-thought. The scene reads compartmentalized rather than lived-in.
> LEV: The books are clean. [He straightens a pen.] You have my word.
> ORA: Then you won't mind an audit. [She closes the ledger.] Tomorrow.
- Fix: let action cut a line off mid-clause; let a look replace a reply.
#### 17. Eyeball-kick imagery — P2 [RC#7]
Sensory language (in speech or parentheticals) tuned for evocative over coherent: tastes that glow, synesthesia
with no POV logic behind it.
> WREN: His voice tasted like static. Like the color of a bruise turned inside out.
> KIP: (a smile like wet copper) I know exactly what you mean.
- Fix: keep only the images this speaker's senses could plausibly deliver.
#### 18. Punctuation fashion — P2, time-decaying [RC#8][AAW#1]
Em-dash density was a strong 2024–25 tell; newer models moved to semicolons and commas on the same frames.
Corroboration only, never primary — the frames (tells 1 and 8) outlive the punctuation.
> TESS: I wanted to stay — I did — but staying — real staying — takes a kind of nerve I lost.
> GIL: And nerve — once it goes — it goes.
- Fix: repair the frame the punctuation decorates; the dashes follow.

### C. Dialogue-specific patterns (original to this suite)

#### 19. On-the-nose emotion naming — P0 [DRV]
Characters announce interiority instead of leaking it through behavior and deflection. Screen dialogue's cardinal
sin; models commit it constantly because naming the feeling maximizes coherence.
> JUNE: I'm angry, but under the anger I'm really just afraid of losing you.
> CAL: I understand. Your fear makes me feel guilty about my betrayal.
- Fix: bury the feeling in what the character does to the other person.
#### 20. Everyone over-articulate — P1 [DRV]
No fragments, no self-repair, no trailing off, no false starts — complete, well-formed sentences even mid-crisis.
> DEREK: The reason I came tonight is that I want to explain my behavior at the dinner.
> LISA: I appreciate that, and I would like to hear your explanation in its entirety.
- Fix: break the syntax where the pressure is; let one thought die unfinished.
#### 21. Echoing the question — P0 [DRV]
Restating the prompt before answering: interview-transcript disease. Exception: a stalling beat the scene marks as stalling.
> KANE: Where were you on the night of the fourteenth?
> TED: Where was I on the night of the fourteenth? At home, watching the game.
- Fix: cut the echo; a character who needs time gets business or a counter-question instead.
#### 22. Perfect turn-taking — P1 [DRV]
No interruptions, no overlaps, nobody talked past or ignored, no silence used as a reply — ping-pong with a net
judge. Fires at scene level: zero cut-offs across a whole conflict scene is the tell.
> ANA: I have something difficult to tell you.
> BEN: Then say it, and I will listen carefully until you are finished.
- Fix: let someone cut in early, or leave a line hanging unanswered.
#### 23. Everyone answers what was asked — P0 [DRV]
Total cooperativity: direct questions get truthful, complete answers. Real characters evade, attack, joke, lie,
go quiet, or answer a different question. Subtext dies here; the biggest drama-killer in the catalog.
> MOM: Are you using again?
> KYLE: Yes. I relapsed three weeks ago because of stress at work, and I'm sorry.
- Fix: decide what the character wants from the exchange and route the reply through that.
#### 24. Vocative overuse — P1 [DRV]
Names dropped line after line. A vocative is a rare, loaded event; more than one or two per ten turns, two
people alone in a room, is machine courtesy.
> SARA: I can't keep doing this, David.
> DAVID: Don't say that, Sara. We can fix this, Sara. We always do, Sara.
- Fix: strip every name the line doesn't need as an event.
#### 25. Therapy-speak anachronism — P0 in period settings, P1 contemporary [DRV]
Clinical-wellness idiom ("hold space," "boundaries," "do the work," "toxic") in mouths that predate it or wouldn't
own it. Contemporary use can be characterization: who talks like this, who rolls their eyes.
> MARTHA (1874, homestead): You crossed a boundary, Elias. I need you to hold space for my anger.
> ELIAS: I hear you, Martha. I am ready to do the work.
- Fix: translate the feeling into the character's own era and class.
#### 26. Uniform turn-length rhythm — P1 [DRV]
Every speech the same size and shape (commonly one or two sentences, 12–25 words) — metronomic pages. Humans
produce one-word turns and page-long rants in the same scene.
> NED: We should leave before the storm reaches the valley floor.
> MAY: You always say that when the barometer starts to drop.
- Fix: redistribute — give one character the floor, cut another to grunts.
#### 27. Tidy button endings — P2 [DRV]
Every scene exits on a bow — a summary line or mini-aphorism. Real scenes get cut off mid-energy; some just stop.
> JO: Maybe getting lost was the only way we could ever find each other.
> CUT TO: (the next scene also ends on an aphorism)
- Fix: end two beats earlier, on the unresolved line.
#### 28. Homogeneous register across characters — P1 per scene, P0 at script scale [DRV]
Strip the names: can you still attribute the lines? When a dockworker and a surgeon share the same syntax and
the same lexicon, there is one voice in the room — the model's.
> DOCKWORKER: The logistics of tonight have become untenable.
> SURGEON: Indeed. Our options have narrowed considerably.
- Fix: re-render each speaker from their voice.md; where none exists, write the spec first.
#### 29. Explaining the metaphor — P1 [DRV]
A character lands an image, then unpacks it for the cheap seats. The unpacking un-writes the image.
> RUTH: This house is a museum. Everything preserved, nothing alive.
> RUTH (CONT'D): Like us — we stopped living and started curating our marriage.
- Fix: cut everything after the image lands.
#### 30. Nobody boring, nobody repetitive — P2 [DRV]
Everyone witty and economical: no hobbyhorses, no re-told stories, no filler person, no one who talks too much
about soup. Controlled boringness is characterization; its total absence is generation.
> GRAMPS: Time is the one currency you can't counterfeit.
> TEEN (15): Then I guess we're all born broke and die rich.
- Fix: assign someone a hobbyhorse and let them ride it one beat too long.

## 4. Severity and density rules

- **P0** fires on first confirmed instance: tells 1, 10, 19, 21, 23 — plus 25 in period settings and 28 at script scale.
- **P1** fires at 2+ per scene or 3+ per 10 pages; sub-threshold hits go on a watch list and still count toward clusters.
- **P2** is reported only in full audits, or when clustered.

**Cluster escalation.** Three or more distinct P1 patterns confirmed in one scene escalate the scene
to P0. A P2 pattern recurring across consecutive scenes reports at P1 weight.

**Budgets for licensed devices.** Per script: one negative-parallelism reveal (tell 1), placed where
the scene earns it; one staccato run (tell 8). Per character: the two tics licensed by their voice.md,
and no more. A device that migrates to a second character loses its license and feeds tells 13 and 28.

**Format/genre profiles** (naturalist drama is the default and the strictest — every rule as written):
- **Heightened comedy and patter** (screwball, Sorkin, Mamet): symmetry tells 2, 8, 13, 22, 26 fire at
  doubled thresholds; tell 30 stops firing. Cooperation tells (19, 21, 23) and register tells (10, 11,
  25) keep full strength — people dodge questions even in patter.
- **Verse and stylized drama:** judge rhythm (26) and frame repetition (13) against the form's own
  meter; suspend them where the verse contract explains the symmetry.
- **Period formality:** over-articulateness (20) and formal address (24) fire at doubled thresholds;
  therapy-speak (25) hardens to P0.

**Stricter-of-two composition.** When two profiles apply at once (a period screwball, say), each tell takes the
stricter of the applicable thresholds. The whitelist sits outside this arithmetic — a specced feature is skipped
under every profile.

## 5. Exemptions and false positives

**Rule zero: a designed voice feature is never a tell.** L2-English interference and dialect grammar are
character voice. AI-detection heuristics false-positive on non-native English writers at rates above 60%
[AAW]; in this suite that failure mode is doctrine. A French character's calques ("I am cooking since this
morning," "It's me who is right"), a Russian character's article drops, Indian English "isn't it?" and
clause-final "only," AAVE habitual "be," Scots "cannae": designed features, specced in each voice.md's Origin
& Register Map. Never "correct" a specced feature. Flagging or fixing one is a judge failure, logged as one.

- **Dialect grammar generally.** Negative concord, was-leveling, "done told you," invariant tags:
  rule-governed grammar. Calling it error or repetition is a false positive with a disrespect problem on top.
- **Character-intentional flatness.** Androids, the dissociating, the depressed, cult members, a cop
  reading a statement: uniformity can be design. The test — is the flatness LOCAL (one character,
  contrasted by the ensemble) or GLOBAL (everyone)? Local flat = choice; global flat = generation.
- **Stylized registers.** Patter, loops, verse, screwball symmetry, period formality, ensemble deadpan:
  heightened uniformity is the genre contract. Judge against the script's own baseline (section 4).
- **Deliberate repetition as motif.** A line echoed across acts, a catchphrase, a running joke, a tic
  assigned to ONE character: craft. The flags target unchosen repetition spread across the cast.
- **Strategic on-the-nose.** Therapy scenes, depositions, a manipulator naming feelings AT someone,
  small children: single instances can be earned. Fire on density and distribution, never on lone sightings.
- **Stock phrases exist.** "Here's the thing," "at the end of the day," "it is what it is," "look, all
  I'm saying is": real speech. One character owning one is voice; the whole cast sharing one is the tell.
- **In-world generated text.** A chatbot character, an on-screen assistant, boilerplate read aloud
  SHOULD trip the detector — that is the point. Exempt quoted in-world material from every flag; check
  instead that it contrasts with the humans around it.

## 6. Uniformity metrics

Word-lists decay and false-positive on designed voices; distributional signals age better. Compute these by
reading, pencil in hand. One odd value can be innocent; several low-variance readings at once are the fingerprint.

- **Words-per-turn variance.** Eyeball each character's longest and shortest turns per scene.
  Suspicious: everything lands between 12 and 25 words — no grunts, no rants, no one-word exits.
- **Type-token ratio per character.** Track the content words each character reuses; healthy voices recycle
  a personal core vocabulary. Suspicious: nobody ever repeats a content word, or every voice's rate feels identical.
- **Vocatives per ten turns.** Count names in direct address. Suspicious: more than one or two per
  ten turns between two people alone in a room.
- **Interruptions and trail-offs per page.** Count cut-offs, overlaps, and lines answered with
  silence or business. Suspicious: zero across a conflict scene.
- **Question-to-direct-answer adjacency.** For each question, mark whether the very next line answers
  it fully and truthfully. Suspicious: a rate near 100% — evasion is where subtext lives.
- **Scenes ending on aphorism.** Read only the final line of every scene. Suspicious: a quarter or
  more are thesis lines or bows.
- **Syntactic-frame repetition.** Read only the first three or four words of every speech in a scene.
  Suspicious: recurring shapes (participial openers, name-plus-comma openers) shared across characters.
- **Strip-the-names register distance.** Cover the names on a full page and try to re-attribute every
  line. Suspicious: you can't. (Tell 28, run as a measurement.)

## 7. Rewrite rules

- **Subtract and sharpen.** Almost every fix is a deletion. Cut the scaffold, keep the load-bearing
  clause; anything added must be specificity in the speaker's own idiom.
- **Never inject.** No added wit, stakes, candor, or lyricism the draft didn't contain. A flat line
  made falsely sparkling stacks a second tell on top of the first.
- **Never standardize a designed voice.** A fix sitting next to an L2 or dialect feature leaves the
  feature verbatim; rewrite around it, then check against the character's calibration lines.
- **Second-pass audit.** Rescan any rewrite from scratch — fixes routinely reintroduce rhythm
  uniformity and template phrasing. If the second pass changes anything, ship the second pass, and say so.

## 8. Licenses and attribution

The section A catalog is adapted from **conorbronsdon/avoid-ai-writing** (SKILL.md), used under the MIT
License. This file redistributes substantial portions of that catalog, so the license ships with it, verbatim:

```
MIT License

Copyright (c) 2026 Conor Bronsdon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**Wikipedia.** Items tagged [WP] derive from the English Wikipedia essay "Wikipedia:Signs of AI
writing" (accessed 2026-08-08 via r.jina.ai mirror), text available under Creative Commons
Attribution-ShareAlike 4.0 (CC BY-SA 4.0). Derivative text reusing its wording must attribute
Wikipedia and share alike.

**recordcrash (Substack).** Items tagged [RC] use ideas and brief quotations under fair use/commentary;
cite the post ("How to Identify AI-Written Web Fiction") when its framing is reused; do not reproduce it at length.

**Section C** ([DRV]) is original to this project, as are all BAD examples in every section: no
upstream license obligations.
