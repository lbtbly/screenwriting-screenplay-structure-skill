# Screenwriting Voices

A voice-spec system for screenplay dialogue. One idea runs through it: a character's voice is a
**contract** — written down as a `voice.md` file — that any writer, human or AI, can render from
and be judged against.

## What's inside

**Skill: character-voice** — designs the contracts. Five workflows: interview a new voice into
existence, extract one from existing script pages, refine/critique specs (including
cast-distinctness checks), generate an audition scene to test-drive a voice, and the Voice
Designer. Ships the 16-axis taxonomy, the annotated voice.md template, dialect & L1-interference
kits (French in depth; Spanish, Russian, German, Mandarin, Arabic, Indian English; AAVE, Southern,
NYC, London, Irish, Scottish — grammar-first, never eye-dialect), and a study map of exemplar
voices from produced scripts.

**Skill: voice-dialogue** — consumes the contracts. Writes ensemble scenes and solo dialogue from
voice.md files (orchestrator-ready input contract: characters + specs, scene goal, length,
mentions, context), revises dialogue while preserving voice, judges dialogue against specs with a
five-dimension rubric, scans for machine-flavored writing (with designed voice features
whitelisted so a French character's calques never get "fixed"), and audits full drafts for voice
drift.

**Voice Designer** (`skills/character-voice/assets/voice-designer.html`) — a standalone page:
open it in any browser. Per-axis morph previews (the same beat hand-written at every notch),
origin grammar samples, eight preset voice stacks, a rough live composite, and voice.md
export/import.

**Voice library** (`voice-library/`) — ten ready specs reverse-engineered from produced
screenplays (Logan Roy, Paul Hunham, NoHo Hank, Sandra Voyter, Benoit Blanc, Mercedes, Colm
Doherty, Elektra, Beth Harmon, Eleanor Shellstrop). Use them as templates, calibration references,
or sparring partners.

## The workflow

1. Design a voice — in conversation ("create a voice for my detective, she's from Marseille"), or
   in the Designer page, or by extraction ("build a voice.md for SARAH from my draft").
2. Keep specs as `voices/<character>.voice.md` beside your screenplay.
3. Write from them: "2-page scene, MARION and TOMMY, she fires him, mention the September menu."
4. Judge and audit: "does this scene sound like them?" — "sweep the draft for voice drift."

## Provenance

Built from a 250-screenplay corpus analysis, craft sources (Scriptnotes, writingwithcolor, Yale
Grammatical Diversity Project, and others — cited inside the reference files), and original
synthesis. AI-tell catalog partially adapted from conorbronsdon/avoid-ai-writing under MIT — see
NOTICE.md.
