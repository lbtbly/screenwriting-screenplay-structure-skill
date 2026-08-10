# Screenwriting Structure

A plot-structure system for screenplays. One idea runs through it: a story's structure is a
**contract** — written down as a `structure.md` file — that a writer can build against, revise
against, and be measured against.

Sibling to `screenwriting-voices`, and built the same way. That plugin makes a character's voice a
spec; this one does it for the shape of the story.

## What makes it different

Most structure tools recite Blake Snyder's page numbers. This one measures. The
`structure-library/` holds 42 page-referenced structural analyses of produced screenplays — every
beat located on the page, every percentage computed against that script's own length — and the
plugin's page targets come from what those scripts do, not from what the craft books prescribe.

The headline finding, and the one that changes how the skills behave: **the midpoint is the
reliable beat, the first-act break is not.** Of 17 locatable feature midpoints, 14 land between 47%
and 55%. First-act breaks range from 10% to 38%, and only 10 of 18 sit in the conventional 19–25%
zone. So the audit skill flags an off-centre midpoint loudly and treats an unconventional first-act
break as a question — what does the placement buy? — rather than a fault. Four canonical scripts in
the corpus run first acts past 29%, and each pays for it the same way.

## What's inside

**Skill: story-structure** — designs the contracts. Five workflows: build a structure from a
premise, answer the framework question ("Save the Cat or the Hero's Journey?"), extract a spec from
pages that already exist, reshape a structure between frameworks or formats, and unstick a story
that has no shape. Ships the catalogue of 20 frameworks with use-when/avoid-when and named
criticism, the format layer (11 formats with measured page counts, act architecture, pilot audit,
series-engine tests), genre contracts and obligatory scenes, the measured-evidence tolerances, and
the annotated `structure.md` template with two complete worked examples.

**Skill: structure-audit** — consumes the contracts. Diagnoses the structure actually present in a
draft, audits a draft against its spec, judges with prioritized page-cited findings, and compares a
writer's measured figures against produced screenplays that faced the same pressure. Ships the full
measurement procedure (how to locate an unlabelled beat, how to establish a denominator, the
five-beat sweep with its ABSENT discipline) and a 39-entry fault catalogue built as a differential
diagnosis — symptom, test, cause, fix direction, library precedent.

**Structure library** (`structure-library/`) — 42 beat maps of produced screenplays: 18 features and
24 TV episodes, indexed by framework, format, genre, and — most usefully — by structural problem.
"My first act runs long" routes to the three scripts that afford one and shows how.

## The workflow

1. Design a structure — "break my story", "which framework fits?", "outline my pilot".
2. Keep the spec as `structure/<project>.structure.md` beside your screenplay.
3. Write the pages (that's `screenplay-write`, given the spec as context).
4. Audit — "does my draft do what the plan said?", "why does page 60 die?", "how does my act one
   compare to a real script?"

## A standing caveat

Every map in the library is of the draft that circulated, which is frequently not the release cut —
Severance's is a pre-production spec with a different protagonist, Raiders' 1979 draft has the hero
absent from his own climax, Succession's has Kendall winning the deal. Each file logs its
divergences. This is a feature: reading a draft against its film is the cheapest lesson in what
rewriting is for.

## Provenance

Built from a structural knowledge base synthesized from 17 craft guides, ~150 web sources covering
the canon and how the major film schools teach it, and original analysis of 42 screenplays from the
author's script library. The beat maps are original structural analysis — they describe and cite
page positions in copyrighted screenplays for study and do not reproduce them. Framework
descriptions summarize published craft systems and attribute them to their authors.
