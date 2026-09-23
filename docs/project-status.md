# Project status

## Foundation draft

The repository currently contains:

- a concise public project definition;
- the two-stage learning model;
- intended-learner and non-goal boundaries;
- a target end-to-end system architecture;
- strict separation between public code and private learning data;
- an inventory of relatively mature protocol areas;
- a gap analysis for raw-material processing and first-draft generation;
- an evaluation framework;
- a phased engineering roadmap;
- reserved component directories for protocol, schemas, pipeline, validators, exporters, and tests.

## Phase 1 — Complete

Completed in Phase 1:

- migrated the complete Protocol v3.5 text to a traceable Markdown baseline;
- assigned a source anchor to every non-empty legacy paragraph;
- recorded the source document hash and every migration transformation;
- replaced the machine-specific private archive path with an external data-root variable;
- removed non-portable internal citation tokens without changing normative meaning;
- created 60 stable cross-process requirement IDs;
- linked each requirement to its legacy source paragraphs;
- assigned requirement level, pipeline stage, verification method, and required evidence;
- added deterministic requirement and repository-privacy validators;
- added a standard-library conformance test suite.
- created a complete 954-clause legacy inventory with explicit unreviewed status;
- added heuristic candidate classification without presenting it as confirmed judgement;
- defined 13 draft schemas covering private sources, transformations, topics, learning signals, candidates, notebook units, gate results, Anki records, reconciliation, authority conflicts, and protocol deltas;
- required explicit privacy metadata for every runtime schema that may carry learner content.

The final coverage matrix maps 500 legacy clauses to baselined requirements,
retains 360 clauses as original non-normative context, confirms 6 additional
clauses as non-normative, and moves 88 clauses into reviewed operational
profiles. Normative and operational backlogs are both zero.

## Current limitations

- semantic target generation and topic-boundary adjudication are not yet
  deterministic production automation;
- automatic target selection and direct Experimental Candidate import into Anki
  remain blocked;
- two private full-cycle pilots are calibration evidence only and do not
  justify reduced human review;
- further independent Shadow Mode cycles are required before any production
  threshold or autonomy claim is considered.

## Phase 2 entry work

1. specify session parsing and topic reconstruction;
2. specify learning-signal detection and candidate scoring;
3. implement traceable first-draft notebook generation;
4. add confidence-based exception routing;
5. build content-free and wholly synthetic conformance tests;
6. select repository visibility and a licence before publication.

## Phase 2 — Experimental draft started

Raw Material Processing Specification v0.1 now defines:

- separate source archive, Topic Evidence Packet, Topic Reference Checkpoint,
  and Night Reference Record roles;
- long-conversation capture and recovery without relying on model memory;
- experimental gates RM-0 through RM-9;
- source-linked gold-standard comparison;
- calibration error classes and metrics;
- qualitative confidence and Shadow Mode routing;
- evidence requirements for promoting a draft rule.

The next English Oral Diary cycle can privately test this draft. It remains
blocked from automatic Anki export until the existing final-review gates pass.

The ChatGPT execution layer is now available as Protocol v3.6-draft — Phase 2
Shadow Mode Profile, together with a short Project Instructions dispatcher.

The first Phase 2 engineering slice is also available:

- 25 JSON Schemas;
- 22 stable experimental error codes;
- external private-session workspace initialization;
- repository-boundary rejection for private runtime data;
- a versioned ChatGPT-to-local pilot-bundle contract;
- a Codex-only complete private source-archive and source-fidelity handoff;
- validated Manual-Gold Ledger import and explicit `gold-ready` state;
- structural session, source-index, packet, checkpoint, signal, ledger, and
  RM-0 through RM-7 linkage validation;
- content-free status reporting and explicit state transitions;
- opaque-target gold comparison for selection, boundary, function, and Note Type;
- structural calibration-report generation;
- content-free synthetic conformance fixtures;
- 20 passing standard-library tests.

Semantic target generation and topic-boundary adjudication remain governed
Codex review steps rather than deterministic automation. The runtime now
validates the artefacts and cross-links produced by that review.

## Private full-cycle evidence

Two private Shadow Mode cycles have now completed the frozen-prediction handoff,
manual-gold comparison, RM-8/RM-9 calibration, stable Protocol v3.5
finalisation, Anki reconciliation, and learner review of the rendered cards.
The private source and all learning content remain outside this repository.

The cycle exposed substantial first-draft selection and boundary differences,
so it does not justify production automation or reduced review. It also exposed
a reusable Topic Retell Front enforcement gap: cues must omit redundant task
labels and represent the complete logical skeleton, using explicit progression,
causality, and parallel-relationship markers where applicable. The
experimental specification, Shadow Mode profile, and Project Instructions now
state this rule consistently. Further independent cycles are required before
any review threshold may be relaxed.

The second cycle established three additional reusable controls: Manual Gold is
a 100% coverage floor rather than an exclusive whitelist; standalone
Vocabulary answers use context-independent citation forms; and accepted
near-synonyms with meaningful usage differences require explicit
`Type::SynonymContrast` routing. It also added a single-card Context Cloze
invariant: related blanks use `c1`, and generated card counts must match the
approved note design before import.
