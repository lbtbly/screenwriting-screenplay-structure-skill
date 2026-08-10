# The voice.md Format — Annotated Template

A voice.md is a **self-contained rendering contract**: any writer (human, Claude, another skill) must be able to produce this character's dialogue from this file alone, without the axes taxonomy, the designer, or this skill. Everything a line needs must be *in* the file — that's why values are written as full phrases with rendering notes, never bare numbers.

Rules of the format:
1. **Self-contained.** No references out except an optional background.md link. Spell out what "sideways directness" means *for this character*.
2. **Calibration lines are the anchor.** The 6–10 sample lines matter more than any single field — they are the few-shot examples a renderer imitates. Write them at final-draft quality, in varied emotional states, labeled.
3. **Deltas, not just baseline.** The Under Pressure section is mandatory. A spec without state modulation produces a monotone character.
4. **Tic cap: 2.** The Idiolect Kit may list at most two catchphrases/tics.
5. **Origin renders as grammar, idiom, and rhythm — not respelled pronunciation** (exception policy in `dialect-and-l1.md`). Every origin feature listed must include a worked example *in this character's mouth*.
6. **Only spec what's load-bearing.** Axes at unremarkable middle values can be omitted — a spec is a fingerprint, not a census. 8–12 committed values beat 16 shrugs.

File naming: `<character-name>.voice.md`, kept next to the screenplay (suggested: `voices/` folder per project).

---

## The template (annotations in [brackets])

```markdown
# VOICE: <Character Name>
<One-line essence — the logline of the mouth. e.g. "Customer-service warmth wrapped
around mob violence, delivered in earnest second-language enthusiasm.">

## Identity
[2–5 sentences: who/where/when. Age, world, occupation, era of the story. What their
speech has to survive (boardrooms? lockup? a 19th-century parlor?). Optional:
`Background: see <name>.background.md` — if absent, a renderer may infer background
from the surrounding screenplay, but voice.md wins every conflict.]

## Speech DNA
[The load-bearing axes only, as "axis: value — rendering note for THIS character".
Group headers optional. Values are phrases, not numbers.]

**Stance**
- Directness: <e.g. "coded — makes his point through parables and questions; states
  a thing plainly only when the listener has failed the parable">
- Candor: ...
- Emotional display: ...
- Tact: ...
- Humor: <style(s) + target + off-switch. "Sardonic, aimed at the world, never at
  his mother; jokes stop entirely when money is discussed.">

**Syntax**
- Sentence length / completeness / certainty / momentum: <only the committed ones>

**Lexicon**
- Register (home + range): <e.g. "street at home, professional in court — shifts by
  listener; never fully standard anywhere">
- Word texture & jargon fields: ...
- Profanity (style, not just rate): ...
- Markers: openers <...>, tags <...>, concession style <...>, address <...>

**Sound**
- Tempo & pauses: ...
- Turn-taking & listening behavior: <how they signal receipt of others' lines>
- Repetition habits: ...

## Origin & Register Map
[Only if marked. Each active layer: variety/L1 + intensity (light/medium/heavy) +
the 3–5 SIGNATURE FEATURES this character actually uses, each with an example line.
Feature salad is a spec bug — real speakers run a personal subset.]
- <e.g. "L1 French, fluent-marked, intensity MEDIUM. Features: (1) no do-support in
  questions — 'You want to leave now?' (2) present-for-perfect with 'since' — 'We
  are married since ten years.' (3) false friend under stress — 'You have deceived
  me' meaning disappointed. (4) tag 'no?' — 'It's better, no?'">
- Code-switch triggers: <when L1 surfaces; when register jumps>
- Education imprint / era / class markers: <as needed>

## Idiolect Kit
- Signature move: <THE mechanism — one sentence, mandatory>
- Obsessions & metaphor domains: ...
- Taboos & deflection maneuver: ...
- Catchphrases/tics (MAX 2): ...
- Never says: <words, registers, speech acts alien to this mouth>

## Under Pressure  [mandatory — deltas from baseline]
- Anger: <which axes move, which direction, what leaks. e.g. "goes QUIETER and more
  ornate; sentence length UP, profanity from never to detonation">
- Fear/stress: <e.g. "L1 interference thickens one notch; hedges vanish">
- Grief/hurt: ...
- Deceit (their tells): ...
- Tenderness (who unlocks it, what drops away): ...
- <optional states the story will visit: drunk, exhausted, in public...>

## Calibration Lines  [6–10, final-draft quality, varied states, labeled]
1. [neutral, to a stranger] "..."
2. [neutral, floor-holding] "..."
3. [angry] "..."
4. [afraid] "..."
5. [lying] "..."
6. [tender] "..."
7. [their joke] "..."
8. [under maximum pressure — the breaking point] "..."

## Evolution Notes  [optional]
[If the voice moves across the story: stages, triggers, which features shift.
e.g. Bella Baxter: telegraphic → literal-precise → baroque; each stage gated by
experience milestones.]

## Provenance  [optional]
[If extracted from existing pages: source script/scenes sampled, date, and any
features deliberately changed from the source.]
```

---

## Worked micro-example (compressed, to show the register of a good spec)

```markdown
# VOICE: NOHO HANK
Customer-service warmth wrapped around mob violence — a Chechen gangster who
sounds like your most supportive barista.

## Identity
30s Chechen mafia lieutenant in Los Angeles; L1 Russian/Chechen, near-native
English absorbed from American service culture and wellness podcasts. Speech must
survive: crime logistics, hostage etiquette, male friendship.

## Speech DNA
- Directness: plain — says terrible things simply, as helpful information.
- Tact: polished-to-ceremonious — hospitality rules apply mid-felony ("I'll walk
  you out. — I want to. It's polite.")
- Certainty: assertive but eager — states opinions as friendly facts.
- Markers: openers "Look," "Okay so"; enthusiastic receipt ("That sounds good.",
  "Great great."); address by first name, warmly, including targets.
- Tempo: quick, upbeat; no menacing pauses — menace arrives at conversational pace.

## Origin & Register Map
- L1 Russian, near-native, intensity LIGHT: (1) article slips under excitement —
  "Is very good plan."; (2) idiom near-misses — "taking up in a Holiday Inn";
  (3) formal completeness where natives contract — "That does not sound like it
  is true." Zero respelling.
- Code-switch: Chechen/Russian only with compatriots or prayer-level fear.

## Idiolect Kit
- Signature move: the gap — sunny service-register × violent content, played
  straight.
- Obsessions: wellness trends, etiquette, friendship.
- Tics (2): "Great great."; upbeat sign-offs ("Good day.")
- Never says: threats phrased as threats; vulgarity beyond mild.

## Under Pressure
- Fear: courtesy INCREASES, articles drop one notch more, sentences shorten but
  stay polite ("Please do not make me to do this.")
- Anger: almost never hot; disappointment register instead — a manager handling
  a bad review.

## Calibration Lines
1. [neutral, business] "We contacted Fuches because we have a confidential
   situation. Can you see this okay?"
2. [helpful, re: murder] "And Goran would like him to suffer. We want him to
   suffer, yes?"
3. [wounded, polite] "That doesn't sound like it's true."
4. [maximum pressure] "NOW."
```

[Note what the micro-example demonstrates: only load-bearing axes are present; every
origin feature has a worked line; the calibration lines are quotable; the whole
thing fits in a renderer's head. A full spec runs 80–140 lines; past ~180 lines a
spec stops being a fingerprint and starts being a costume trunk.]
