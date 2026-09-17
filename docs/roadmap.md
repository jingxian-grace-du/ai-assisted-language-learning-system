# Roadmap

## Phase 0 — Foundation

Goal: define the system before automating it.

- establish product philosophy and learner boundaries;
- document the two-stage learning model;
- lock privacy and repository boundaries;
- inventory current protocol strengths;
- identify raw-material generation gaps;
- define evaluation dimensions;
- select a licence and publication model before release.

Exit condition: the repository describes one coherent system without relying on private examples.

## Phase 1 — Protocol as an executable specification

Goal: convert mature audit rules into versioned, testable requirements.

- freeze and import a privacy-reviewed protocol baseline;
- assign stable IDs to normative requirements;
- define gate inputs, outputs, failures, and invalidation rules;
- create schemas for source spans, topics, signals, targets, notebook units, and audit results;
- build deterministic validators for structural invariants;
- create a synthetic conformance suite.

Exit condition: an artefact cannot claim a gate pass without machine-readable evidence.

## Phase 2 — First-draft generation

Goal: specify and implement raw material to structured notebook.

- session parsing and speaker attribution;
- topic reconstruction;
- learning-signal detection;
- candidate ranking and rejection reasons;
- source-grounded canonical content;
- Note Type assignment;
- confidence and exception routing.

Exit condition: the pipeline produces traceable notebook candidates whose every unit links to evidence and a selection decision.

## Phase 3 — Private calibration

Goal: measure quality against separately stored, human-approved standards.

- evaluate segmentation, selection, fidelity, and card design independently;
- establish precision, recall, review-cost, and false-pass baselines;
- build regression tests from abstracted error classes, not copied diary text;
- calibrate automatic, sampled, and mandatory-review thresholds;
- record protocol deltas through post-cycle classification.

Exit condition: quality and human-review requirements are measured rather than asserted.

## Phase 4 — Anki integration

Goal: produce and reconcile safe canonical Anki records.

- typed exporters;
- render validation;
- bounded import configuration;
- read-only collection reconciliation;
- duplicate and linked-update handling;
- operational recovery and idempotency.

Exit condition: validated notebook units map to expected Anki objects without silent mutation or count drift.

## Phase 5 — Review by exception

Goal: minimise routine human intervention while preserving uncertainty.

- high-confidence automatic passage;
- focused review queues with evidence and reasons;
- privacy-preserving observability;
- user-specific preferences with explicit controls;
- continuous error-class and protocol-delta audits.

Exit condition: most routine material advances automatically, while ambiguous or risky decisions remain visible and blocked.

## Explicit non-goals for early releases

- public storage of learner diaries;
- therapeutic or life-advice claims;
- guaranteed learning outcomes;
- fully autonomous publication of low-confidence content;
- optimising card volume as a substitute for learning value;
- supporting every proficiency level or examination workflow.
