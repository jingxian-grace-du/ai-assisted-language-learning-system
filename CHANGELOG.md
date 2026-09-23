# Changelog

All notable public changes to this project are documented here.

The project uses pre-release version labels while the Phase 2 generation and
calibration design remains experimental.

## Unreleased

### Calibrated

- treated independent Manual Gold as a mandatory coverage floor rather than an
  exclusive whitelist and added a separate AI Supplementary review route;
- added a reciprocal omission scan for useful source-supported targets missed
  by both Manual Gold and the frozen prediction, with learner approval required
  before promotion;
- added Manual-Gold Review Alerts for possible human errors without silently
  rewriting the gold record;
- normalised standalone Vocabulary verbs and phrasal verbs to
  context-independent citation forms;
- introduced explicit `Type::SynonymContrast` routing for accepted expressions
  whose use differs by register, setting, institution, relationship, or
  pragmatic effect;
- enforced one-card Context Cloze indexing with shared `c1` blanks unless a
  separate card is intentionally approved;
- required the Chinese Prompt in bilingual Context Cloze to remain fully
  visible while only the English targets are clozed;
- added chronology, causality, and event-identity validation for Topic Retell
  Front and Back content;
- recognised Topic Retell as a strong Feynman-style retrieval task and blocked
  automatic paired-card creation unless another Note Type serves a distinct
  learning function;
- recorded learner visual confirmation and formal completion of the second
  private Shadow Mode cycle;
- added a privacy-safe aggregate report from the second completed private
  Shadow Mode cycle.

### Safety boundaries

- preserved the frozen historical prediction and pre-clarification comparison;
- kept all source-bearing cycle artefacts, notebook content, Anki records, and
  collection backups outside the public repository;
- retained mandatory human review and explicit approval before Anki import.

## v0.1.0-alpha — 2026-09-17

### Added

- the two-stage English Oral Diary learning model and intended-learner boundary;
- the privacy-reviewed Protocol v3.5 Markdown baseline and traceability data;
- 60 machine-readable cross-process requirements and 25 JSON Schemas;
- deterministic requirement, schema, coverage, error-code, and repository
  privacy validators;
- a Phase 2 structural runtime for private Pilot Bundle import, complete source
  archive validation, Manual-Gold handoff, RM-8 comparison, and RM-9 reporting;
- Raw Material Processing Specification v0.1 and the Protocol v3.6-draft Shadow
  Mode Profile;
- content-free synthetic conformance fixtures and 16 standard-library tests;
- a privacy-safe aggregate report from the first complete private pilot cycle.

### Calibrated

- strengthened Topic Retell Front construction so the cue omits redundant task
  labels and represents the complete logical skeleton without answer leakage;
- separated frozen-prediction evaluation from later stable-path card correction,
  Anki reconciliation, and rendered-card confirmation.

### Safety boundaries

- real diaries, chats, notebooks, screenshots, recordings, Anki content, and
  source-bearing calibration artefacts are prohibited from the repository;
- Experimental Candidates are not approved for direct Anki import;
- production automation and reduced human review are not claimed.

### Known limitations

- semantic topic reconstruction and learning-target selection still require
  governed human review;
- evidence comes from one private full-cycle pilot and is insufficient for
  production thresholds.

### Licence

- released under the Apache License 2.0;
- copyright 2026 Jingxian (Grace) Du.
