# Phase 2 Interchange Contract v0.1

- Status: Experimental technical contract
- Contract version: `0.1.0`
- Stable semantic authority: English Oral Diary Protocol v3.5
- Experimental semantic authority: Raw Material Processing Specification v0.1
- Execution authority: Protocol v3.6-draft — Phase 2 Shadow Mode Profile
- Automatic Anki export or import: Prohibited

## 1. Purpose and authority boundary

This document is the self-contained machine-interchange contract for moving
structural Phase 2 Shadow Mode results from a private ChatGPT Project into the
local English Oral Diary pilot runtime.

It defines two outputs:

1. the Phase 2 Pilot Bundle, exported by the ChatGPT Project before the manual
   notebook is disclosed;
2. the Phase 2 Manual-Gold Ledger, materialised by the private Codex runtime
   only after manual-gold source-fidelity verification.

This contract controls field names, required values, identifiers, linkage,
privacy metadata, and export failure behaviour. It does not change which
material should be learned, how source meaning is judged, or how Protocol v3.5
operates. If this contract conflicts with a semantic rule, the governing
Protocol or Specification controls and the export must record or report the
conflict rather than silently changing meaning.

## 2. Global rules

### 2.1 JSON output

Each trigger produces exactly one valid JSON object. Do not include comments,
trailing commas, Markdown headings, or explanatory prose inside the JSON.
Prefer a downloadable `.json` file. If file creation is unavailable, return one
JSON code block and nothing else in that response.

Do not claim that an export succeeded unless the complete JSON object was
actually produced.

### 2.2 Stable identifiers

Every identifier must match:

```text
^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+$
```

Identifiers must remain stable across the Pilot Bundle, Manual-Gold Ledger,
later comparison, and any resumed export. Never recycle one ID for a different
entity.

Recommended forms include:

```text
EOD-YYYY-MM-DD-S01
SPAN-YYYY-MM-DD-001
TOPIC-YYYY-MM-DD-001
PACKET-YYYY-MM-DD-001
CHECKPOINT-YYYY-MM-DD-001
SIGNAL-YYYY-MM-DD-001
CAND-YYYY-MM-DD-001
TARGET-YYYY-MM-DD-001
LEDGER-YYYY-MM-DD-PRED-001
LEDGER-YYYY-MM-DD-REJ-001
LEDGER-YYYY-MM-DD-GOLD-001
RESULT-YYYY-MM-DD-RM-0
BUNDLE-YYYY-MM-DD-001
```

### 2.3 Privacy object

Every object that requires `privacy` must use exactly:

```json
{
  "classification": "private-learning-data",
  "repository_allowed": false,
  "retention_policy": "learner-controlled"
}
```

The Pilot Bundle and Manual-Gold Ledger are private even when the source-span
index contains no raw text. Never recommend adding either export to GitHub.

### 2.4 Source-content boundary

The source-span index must never contain raw diary wording, quotations,
transcripts, summaries of private events, names, locations, or other diary
content. It contains only structural metadata and stable references back to the
private Project conversation.

Other private bundle objects may contain concise evidence or decision reasons
when required, but they must not reproduce the full diary transcript. Prefer
stable reason codes or minimal descriptions sufficient for audit.

### 2.5 Arrays and additional fields

All arrays identified as unique must contain no duplicate values. Do not add
fields that are not defined in this contract. Use an empty array for an allowed
field with no values; do not invent placeholder evidence.

## 3. Export A — Phase 2 Pilot Bundle

### 3.1 Trigger and timing

Trigger:

```text
Export the Phase 2 pilot bundle.
```

Use it only after the Experimental Notebook Candidate and gates RM-0 through
RM-7 exist, and before the learner supplies the manual notebook. This freezes
the independent AI prediction and prevents gold-answer leakage.

### 3.2 Top-level object

The Pilot Bundle must contain exactly these fields:

```json
{
  "bundle_version": "0.1.0",
  "bundle_id": "BUNDLE-YYYY-MM-DD-001",
  "session_manifest": {},
  "source_span_index": {},
  "topic_evidence_packets": [],
  "checkpoint_register": {},
  "learning_signals": [],
  "candidate_ledgers": [],
  "experimental_notebook_manifest": {},
  "gate_results": [],
  "privacy": {
    "classification": "private-learning-data",
    "repository_allowed": false,
    "retention_policy": "learner-controlled"
  }
}
```

`candidate_ledgers` must contain exactly one prediction ledger and one rejected
ledger. `gate_results` must contain exactly one result for every gate from
`RM-0` through `RM-7`.

### 3.3 Session Manifest

Required fields:

```json
{
  "manifest_version": "0.1.0",
  "session_id": "EOD-YYYY-MM-DD-S01",
  "mode": "phase-2-shadow",
  "protocol": {
    "stable": "3.5",
    "experimental": "raw-material-processing-v0.1",
    "profile": "3.6-draft-shadow-mode"
  },
  "status": "candidate-generated",
  "artefacts": {
    "source_archive": "source",
    "topic_evidence_packets": "evidence-packets",
    "checkpoints": "checkpoints",
    "learning_signals": "signals",
    "candidate_ledgers": "ledgers",
    "pilot_bundles": "bundles",
    "comparison_reports": "comparisons",
    "calibration_reports": "calibration",
    "state_transitions": "transitions"
  },
  "privacy": {
    "classification": "private-learning-data",
    "repository_allowed": false,
    "retention_policy": "learner-controlled"
  }
}
```

For a completed, structurally valid RM-0 through RM-7 run, `status` must be
`candidate-generated`. If a required source, link, conflict, or gate is
blocked, use `blocked`. Do not use `comparison-complete` in the Pilot Bundle.

### 3.4 Content-free Source-Span Index

Required object:

```json
{
  "index_id": "INDEX-YYYY-MM-DD-001",
  "session_id": "EOD-YYYY-MM-DD-S01",
  "spans": [],
  "privacy": {
    "classification": "private-learning-data",
    "repository_allowed": false,
    "retention_policy": "learner-controlled"
  }
}
```

Every span must contain:

- `span_id`: stable ID;
- `order`: unique integer starting at 1 or greater;
- `speaker`: `learner`, `assistant`, or `system-event`;
- `substantive`: Boolean;
- exactly one of `topic_id` or `non_topic_disposition`.

Allowed span object shapes:

```json
{
  "span_id": "SPAN-YYYY-MM-DD-001",
  "order": 1,
  "speaker": "learner",
  "substantive": true,
  "topic_id": "TOPIC-YYYY-MM-DD-001"
}
```

```json
{
  "span_id": "SPAN-YYYY-MM-DD-002",
  "order": 2,
  "speaker": "system-event",
  "substantive": false,
  "non_topic_disposition": "OPERATIONAL-EVENT"
}
```

No span object may contain `content`, raw wording, or a private diary summary.

### 3.5 Topic Evidence Packets

Each current packet must contain:

```json
{
  "packet_id": "PACKET-YYYY-MM-DD-001",
  "version": 1,
  "session_id": "EOD-YYYY-MM-DD-S01",
  "topic_id": "TOPIC-YYYY-MM-DD-001",
  "source_span_ids": ["SPAN-YYYY-MM-DD-001"],
  "excluded_adjacent_span_ids": [],
  "signal_ids": [],
  "reasoning_candidate_ids": [],
  "guidance_candidate_ids": [],
  "checkpoint_id": "CHECKPOINT-YYYY-MM-DD-001",
  "unresolved_conflict_ids": [],
  "confidence": "high",
  "status": "complete",
  "privacy": {
    "classification": "private-learning-data",
    "repository_allowed": false,
    "retention_policy": "learner-controlled"
  }
}
```

Required fields are `packet_id`, `version`, `session_id`, `topic_id`,
`source_span_ids`, `signal_ids`, `checkpoint_id`, `status`, and `privacy`.

Allowed `confidence` values are `high`, `medium`, and `low`. Allowed `status`
values are `open`, `complete`, `blocked`, and `superseded`. Export only current
packet versions as active; preserve supersession identities when relevant.

### 3.6 Checkpoint Linkage Register

Required object:

```json
{
  "register_id": "CHECKREG-YYYY-MM-DD-001",
  "session_id": "EOD-YYYY-MM-DD-S01",
  "links": [],
  "privacy": {
    "classification": "private-learning-data",
    "repository_allowed": false,
    "retention_policy": "learner-controlled"
  }
}
```

Each link must contain:

```json
{
  "checkpoint_id": "CHECKPOINT-YYYY-MM-DD-001",
  "topic_id": "TOPIC-YYYY-MM-DD-001",
  "packet_id": "PACKET-YYYY-MM-DD-001",
  "source_span_ids": ["SPAN-YYYY-MM-DD-001"],
  "status": "locked"
}
```

Allowed status values are `locked`, `blocked`, and `superseded`.

### 3.7 Learning Signals

Each signal must contain:

```json
{
  "signal_id": "SIGNAL-YYYY-MM-DD-001",
  "topic_id": "TOPIC-YYYY-MM-DD-001",
  "source_span_ids": ["SPAN-YYYY-MM-DD-001"],
  "signal_type": "explicit-wording-question",
  "confidence": 0.9,
  "evidence_note": "DIRECT-LEARNER-SIGNAL",
  "privacy": {
    "classification": "private-learning-data",
    "repository_allowed": false,
    "retention_policy": "learner-controlled"
  }
}
```

Required fields are `signal_id`, `topic_id`, `source_span_ids`, `signal_type`,
`confidence`, and `privacy`. `confidence` is a number from 0 through 1.
`evidence_note` is optional.

Allowed `signal_type` values are:

- `unknown-concept-description`;
- `explicit-wording-question`;
- `hesitation`;
- `self-correction`;
- `inaccurate-substitution`;
- `unnatural-production`;
- `morning-recall-failure`;
- `accepted-expression`;
- `reused-expression`;
- `explicit-retention-request`;
- `manual-mark`;
- `other`.

### 3.8 Candidate Ledgers

Every ledger must contain:

```json
{
  "ledger_id": "LEDGER-YYYY-MM-DD-PRED-001",
  "session_id": "EOD-YYYY-MM-DD-S01",
  "ledger_kind": "prediction",
  "specification": "raw-material-processing-v0.1",
  "candidates": [],
  "privacy": {
    "classification": "private-learning-data",
    "repository_allowed": false,
    "retention_policy": "learner-controlled"
  }
}
```

Allowed `ledger_kind` values are `prediction`, `rejected`, and `manual-gold`.
The Pilot Bundle permits only `prediction` and `rejected` and requires one of
each.

Every candidate must contain:

```json
{
  "candidate_id": "CAND-YYYY-MM-DD-001",
  "target_key": "TARGET-YYYY-MM-DD-001",
  "topic_id": "TOPIC-YYYY-MM-DD-001",
  "signal_ids": ["SIGNAL-YYYY-MM-DD-001"],
  "learning_function": "lexical",
  "note_type": "vocabulary",
  "decision": "selected",
  "decision_reasons": ["DIRECT-LEARNER-SIGNAL"],
  "confidence": "high",
  "source_span_ids": ["SPAN-YYYY-MM-DD-001"],
  "boundary_key": "BOUNDARY-YYYY-MM-DD-001",
  "semantic_fidelity": "pass"
}
```

Required candidate fields are `candidate_id`, `target_key`, `topic_id`,
`signal_ids`, `learning_function`, `note_type`, `decision`, `decision_reasons`,
`confidence`, and `source_span_ids`. `boundary_key` and `semantic_fidelity` are
optional fields but should be present when evaluated.

Allowed `learning_function` values:

- `lexical`;
- `complete-expression`;
- `reasoning-unit`;
- `guidance`.

Allowed `note_type` values:

- `context-cloze`;
- `topic-retell`;
- `vocabulary`;
- `guidance`;
- `none`.

Allowed `decision` values:

- `selected`;
- `suggested-for-review`;
- `rejected`;
- `unresolved-conflict`.

Allowed `confidence` values are `high`, `medium`, `low`, and `manual`. Pilot
prediction or rejected candidates must not use `manual`.

Allowed `semantic_fidelity` values are `pass`, `fail`, and `not-evaluated`.

The prediction ledger contains AI-selected, review-routed, or unresolved
candidates. The rejected ledger contains rejected or unresolved candidates.
Every candidate, including a rejection, requires at least one source span and
at least one decision reason.

### 3.9 Experimental Notebook Manifest

Required object:

```json
{
  "manifest_id": "NOTEBOOK-YYYY-MM-DD-001",
  "session_id": "EOD-YYYY-MM-DD-S01",
  "label": "EXPERIMENTAL CANDIDATE — NOT APPROVED FOR ANKI",
  "specification": "raw-material-processing-v0.1",
  "unit_ids": [],
  "ledger_ids": [
    "LEDGER-YYYY-MM-DD-PRED-001",
    "LEDGER-YYYY-MM-DD-REJ-001"
  ],
  "gate_result_ids": [],
  "unresolved_conflict_ids": [],
  "anki_ready": false,
  "privacy": {
    "classification": "private-learning-data",
    "repository_allowed": false,
    "retention_policy": "learner-controlled"
  }
}
```

The label and `anki_ready: false` are immutable in Shadow Mode. `ledger_ids`
must exactly identify the two ledgers in the bundle. `gate_result_ids` must
exactly identify all eight RM-0 through RM-7 results.

### 3.10 RM-0 through RM-7 Gate Results

Each result must contain:

```json
{
  "result_id": "RESULT-YYYY-MM-DD-RM-0",
  "gate_id": "RM-0",
  "subject_ids": ["EOD-YYYY-MM-DD-S01"],
  "status": "pass",
  "checks": [
    {
      "requirement_id": "EOD-RM-000",
      "status": "pass",
      "evidence_reference": "INDEX-YYYY-MM-DD-001"
    }
  ],
  "invalidates_result_ids": [],
  "evaluated_at": "2026-01-01T00:00:00Z"
}
```

Allowed result `status` values are `pass`, `fail`, `blocked`, `not-run`, and
`invalidated`. Each result requires at least one check.

Each check requires:

- `requirement_id` matching `EOD-<UPPERCASE-STAGE>-<THREE DIGITS>`;
- `status`: `pass`, `fail`, `blocked`, or `not-applicable`;
- non-empty `evidence_reference`;
- optional `failure_code`.

`evaluated_at` must be a real ISO 8601 date-time. Do not fabricate a passing
check when evidence is missing.

## 4. Pilot Bundle cross-object invariants

Before export, verify all of the following:

1. Every object uses the same `session_id`.
2. Every source-span ID is unique and every order number is unique.
3. Every substantive span has exactly one topic assignment or an explicit
   non-topic disposition.
4. The set of topic IDs assigned in the source index equals the set of current
   Topic Evidence Packet topic IDs.
5. Every packet source span resolves in the source index.
6. Every packet signal ID resolves in `learning_signals`.
7. Every packet checkpoint ID resolves in the checkpoint register.
8. Every checkpoint link resolves to the same packet, topic, and source spans.
9. Every signal topic and source span resolves.
10. Every candidate topic, signal, and source span resolves.
11. Candidate IDs and `target_key` values are unique inside each ledger.
12. The bundle contains exactly the `prediction` and `rejected` ledgers.
13. The bundle contains exactly RM-0, RM-1, RM-2, RM-3, RM-4, RM-5, RM-6, and
    RM-7 once each.
14. Notebook ledger IDs and gate result IDs exactly match the bundled objects.
15. The notebook label is unchanged and `anki_ready` is `false`.
16. Every required private object uses `repository_allowed: false`.
If all eight gates pass, session status is `candidate-generated`. If any gate
fails, is blocked, has not run, or is invalidated, session status is `blocked`.

## 5. Codex artefact B — Phase 2 Manual-Gold Ledger

### 5.1 Timing and execution boundary

This is not a ChatGPT Project trigger. Codex may materialise the ledger only
after:

1. the Pilot Bundle prediction has already been frozen;
2. every authoritative source chat has been preserved in a complete private
   source archive;
3. the learner has independently supplied the manual notebook;
4. Codex has completed the source-fidelity review;
5. source-fidelity conflicts have been resolved or explicitly preserved as
   unresolved and excluded from approved gold selections.

Before the ledger is accepted, the Codex runtime validates two additional
private artefacts:

- a `private-source-archive.schema.json` object containing every authoritative
  night and morning source-chat segment and a complete/partial/unavailable
  completeness decision;
- a `source-fidelity-report.schema.json` object linking the manual notebook and
  approved gold candidates back to frozen source-span IDs.

Neither artefact may be stored in the public repository. A partial or
unavailable source archive blocks the gold handoff.

### 5.2 Top-level object

The output must contain exactly:

```json
{
  "ledger_id": "LEDGER-YYYY-MM-DD-GOLD-001",
  "session_id": "EOD-YYYY-MM-DD-S01",
  "ledger_kind": "manual-gold",
  "specification": "raw-material-processing-v0.1",
  "candidates": [],
  "privacy": {
    "classification": "private-learning-data",
    "repository_allowed": false,
    "retention_policy": "learner-controlled"
  }
}
```

Each approved gold candidate uses the Candidate object contract in section
3.8, with these additional rules:

- `decision` is `selected` for an approved target;
- `confidence` is `manual`;
- `decision_reasons` contains at least one manual-selection reason;
- `semantic_fidelity` is `pass` only after source verification;
- `source_span_ids` is non-empty;
- `signal_ids` may be empty for a true manual-only target when no earlier
  signal exists;
- unresolved source conflict is not exported as an approved selection.

### 5.3 Target identity

Reuse the prediction ledger's `target_key` only when the prediction and gold
candidate represent the same semantic learning target. Similar wording alone
is insufficient.

Assign a new stable `target_key` when the gold candidate is a genuine
manual-only target omitted by the prediction. Do not change an already frozen
prediction `target_key` to improve the apparent comparison result.

## 6. Blocking and recovery

Do not export a superficially valid object by inventing missing IDs, evidence,
checks, topics, signals, or decisions.

If the full object cannot be produced:

- identify the exact missing or inconsistent IDs outside the JSON;
- keep the session status `blocked` when applicable;
- preserve completed artefacts and stable IDs;
- resume the same export after recovery;
- do not substitute a prose summary for the required JSON object.

If response length interrupts the JSON, the partial output is not a successful
export. Regenerate one complete object or produce a downloadable file.

## 7. Final pre-export checklist

For the Pilot Bundle:

- manual notebook not yet disclosed;
- complete JSON object;
- bundle version `0.1.0`;
- exactly two ledgers: prediction and rejected;
- exactly eight gate results: RM-0 through RM-7;
- all cross-object IDs resolve;
- no raw diary wording in source-span index;
- private metadata on every required object;
- experimental label exact;
- `anki_ready: false`;
- stored outside GitHub.

For the Manual-Gold Ledger:

- prediction already frozen;
- complete private source archive imported by Codex;
- manual notebook source-verified;
- ledger kind `manual-gold`;
- source-linked manual selection reasons;
- semantic target keys aligned without answer leakage;
- unresolved conflicts not mislabelled as approved;
- no raw diary transcript;
- private metadata present;
- stored outside GitHub.
