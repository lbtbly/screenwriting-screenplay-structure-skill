# Rendering Craft — Writing FROM a voice.md

How to turn a spec into living lines. The spec is a rendering contract: it decides HOW everything
is said; the scene decides WHAT happens. This file is the order of operations between the two.

## Ingesting a spec (read in this order)

1. **Essence line + Signature move** — the mechanism. Hold it while writing every line; when a
   line feels dead, it's usually because the mechanism stopped driving.
2. **Calibration lines — read twice.** They are the few-shot anchor: absorb their rhythm, then put
   them away. Imitate the mechanism, never reuse the lines themselves — a calibration line
   appearing verbatim in output is a rendering failure (it will also go stale on the second use).
3. **Under Pressure** — know the deltas before writing, because most scenes worth writing are
   pressure scenes.
4. **Axes + Markers** — the dials. Note which are committed (off-middle) — those are load-bearing.
5. **Origin kit** — the 3–5 features and the intensity dial; the dosage algorithm below.
6. **Never says** — post it mentally above the keyboard.
If a background.md is linked, read it after the voice.md; where they conflict on speech, voice.md
wins. With no background file, infer background from the surrounding screenplay — and say you did.

## The line loop

For each speech: know the character's **want in this beat** and their **state** → pick the **mode**
(neutral / emotional / declarative / manipulative) → compose in-voice → check: does it break a
never-says? does it overspend the tic budget? did the last line change their brain (see Listening)?

Mode rules that outrank everything:
- **Emotional is rarely well-articulated.** Under real feeling, subtract: vocabulary shrinks,
  sentences break, repetition rises. "Less coherent and more emotionally clear."
- **Never emotional and declarative in the same breath.** Wisdom delivered mid-breakdown reads as
  the writer talking. Break the speech: collapse first, insight later (or never).
- **Manipulative mode is voice-true too.** A manipulator manipulates IN their voice — Logan hunts
  with questions, Hank soothes with logistics, a hedger weaponizes helplessness.

## State modulation in practice

The spec's baseline is the character at rest; apply Under Pressure deltas the moment stakes rise.
- **The general law: stress subtracts complexity and amplifies signature** — the ornate get more
  ornate, the clipped get shorter — **until the breaking point**, where even the signature
  collapses into plain short true words. Every voice's breaking point sounds weirdly similar;
  that's the point. What differs is how long they hold out and what finally breaks them.
- **The gun changing hands changes the voice mid-scene.** Track who holds the power; at the
  handoff beat, both voices shift — the winner's features relax, the loser's compress or spike.
  If a scene's power never moves, ask the scene why it exists.
- **L1/dialect intensity moves one notch heavier under stress, fatigue, drink, or fury** — and one
  notch lighter inside rehearsed professional domains. Code-switching fires only at the spec's
  triggers (compatriots, counting, prayer, rage) — never as seasoning.
- **Deceit uses the spec's tells.** Every good spec says how this character lies (over-precision,
  charm spike, tempo change, one detail too many). Render the tell; don't announce the lie.

## Listening is half the voice

Between any two speeches, the second speaker heard the first — render the receipt:
- Use the character's **listening behavior** from the spec (minimal power-token, silence-as-reply,
  echo-then-attack, enthusiastic agreement, challenge-by-question).
- **Discourse markers are state-change evidence** ("Well—", "Okay. Okay." "No, you're right"):
  they say the last line changed the speaker's brain. Give each character their own palette from
  the spec's Markers block; palette collision across characters is a differentiation bug.
- Characters may **refuse** to have heard — evasion, subject change, answering a different
  question — but refusal must be visible, i.e., motivated by want or taboo, not by the writer
  needing a segue.

## Origin dosage (the algorithm)

1. **Establish hard in the character's first 2–3 speeches**: two grammar features + one lexical
   item, so the reader's inner ear locks the accent.
2. **Taper to maintenance**: roughly one marked element per 3–4 lines; rhythm carries the rest.
   Lines with zero markers are correct — the reader continues the voice unaided.
3. **Re-spike at pressure and code-switch boundaries** — the spike IS characterization.
4. Grammar and idiom only; the one licensed respelling family at most (see `dialect-and-l1.md`,
   which also governs the auteur exception). Never add features the spec doesn't list — a French
   character does not drop articles Russian-style because it "sounds foreign".

## When the scene demands what the voice can't say

The most common rendering crisis: the beat requires an apology, a confession, an "I love you" —
and the spec says the character can't produce it. Never break the spec; **route the content
through the mechanism**:
- Logan can't apologize → he offers a job, unexplained.
- Hunham can't say "I'm proud of you" → he presses a book into a hand, with a citation.
- Hank can't threaten → he shares regrettable logistics, cheerfully.
- A sealed character can't grieve aloud → the grief goes into what they do to the kettle.
The audience receives the beat BECAUSE it arrived in-voice; the translation is the drama. If the
content truly cannot arrive in-voice, that's a story note, not a license to break voice — flag it.

## Solo rendering (monologues, single-character passes)

Same loop, plus: compose in **movements of thought** — chunks with mini-reversals and built-in
pauses, each chunk anchored on an emphasis word ("the point, the reveal, or a strange word").
Monologues still need a want, a listener (even absent), and at least one turn where the speaker
surprises themself. Check memorizability by reading aloud: buried anchors and consonant pileups
are rewrites.

## Revision that preserves voice

When revising existing dialogue (yours or the writer's):
- **Minimal diff.** Keep the writer's beats, structure, and every line that already works; touch
  only voice-breaking spans. Mark what changed and name the axis/rule that motivated each change.
- Rewrite in **subtract-and-sharpen** mode: never inject wit, stakes, or performed candor the
  original didn't have (full rule in `ai-tells-dialogue.md`); never standardize an L2/dialect
  feature while fixing an adjacent problem.
- After the pass, re-run the self-checks (cover test on the revised scene; tells scan on the
  rewrite itself — fixes love to reintroduce uniformity).

## Output hygiene

Screenplay format rules belong to the screenplay-write skill — cues, wrylies, dual dialogue,
interruption punctuation (em-dash cut-off, ellipsis trail-off) follow it. From this file, only two
formatting stances: script interruptions and overlaps where the specs license them (dual dialogue
is a heavy spice), and keep wrylies rare — voice on the page should not need stage-managing.
