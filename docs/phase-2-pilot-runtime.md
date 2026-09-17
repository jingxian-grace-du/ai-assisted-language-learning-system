# Phase 2 pilot runtime

The pilot runtime is the private bridge between a ChatGPT Phase 2 Shadow Mode
cycle and this repository's structural validation tools. It can run before the
first real Shadow Mode cycle. The cycle supplies calibration evidence; it does
not unlock the ability to keep engineering the repository.

## Boundary of the current implementation

The runtime can:

- initialise an external private session workspace;
- import a versioned Shadow Mode pilot bundle;
- verify source-span, topic, packet, checkpoint, signal, candidate, and gate
  linkage;
- enforce the experimental-notebook Anki boundary;
- expose a content-free session status;
- enforce explicit session-state transitions;
- import a complete private multi-chat source archive;
- import a source-verified Manual-Gold Ledger and Source-Fidelity Report;
- compare an opaque prediction ledger with the validated gold ledger in RM-8;
- generate a structural calibration report.

It cannot yet infer reliable topics or learning targets from diary language,
adjudicate semantic fidelity, or decide that the system is production-ready.
Those abilities require evidence from repeated private Shadow Mode cycles.

## ChatGPT Project source set

The private ChatGPT Project requires four sources:

1. English Oral Diary Protocol v3.5;
2. Raw Material Processing Specification v0.1;
3. Protocol v3.6-draft — Phase 2 Shadow Mode Profile;
4. Phase 2 Interchange Contract v0.1.

Place the replacement Project Instructions in the Project's Instructions field,
not in its source list. This Pilot Runtime guide is for local operation and does
not need to be uploaded to the ChatGPT Project.

## Private interchange contract

After RM-0 through RM-7, the ChatGPT Project trigger is:

```text
Export the Phase 2 pilot bundle.
```

The response must follow Phase 2 Interchange Contract v0.1; the repository
validator implements `schemas/pilot-bundle.schema.json`. Its source-span
index is deliberately content-free: it records IDs, order, speaker, and topic
or non-topic disposition, but not raw diary wording. Before manual-gold
comparison, Codex materialises every referenced authoritative chat as a
paginated private source archive outside the repository. Project memory and
summaries are not source substitutes.

The bundle itself is still private learning data because its evidence and
candidate decisions can reveal personal learning activity. Store it outside
the repository.

## Local cycle

Create a private runtime root outside this Git checkout:

```text
python pipeline/eod.py init-session \
  --private-root /external/private/eod-runtime \
  --session-id EOD-YYYY-MM-DD-S01
```

Save the ChatGPT export in another private external location, then import it:

```text
python pipeline/eod.py import-bundle \
  --bundle /external/private/exports/EOD-YYYY-MM-DD-S01-pilot-bundle.json \
  --session-root /external/private/eod-runtime/sessions/EOD-YYYY-MM-DD-S01
```

Inspect content-free state and run structural validation:

```text
python pipeline/eod.py status \
  --session-root /external/private/eod-runtime/sessions/EOD-YYYY-MM-DD-S01

python pipeline/eod.py validate-session \
  --session-root /external/private/eod-runtime/sessions/EOD-YYYY-MM-DD-S01
```

After the Pilot Bundle is imported, hand every night continuation and morning
review chat to Codex. Codex writes a private archive conforming to
`private-source-archive.schema.json`; then import it:

```text
python pipeline/eod.py import-source-archive \
  --archive /external/private/source/conversation-source-archive.json \
  --session-root /external/private/eod-runtime/sessions/EOD-YYYY-MM-DD-S01
```

The learner prepares the manual notebook independently. Codex performs
source-fidelity review and materialises two private artefacts conforming to
`candidate-ledger.schema.json` and `source-fidelity-report.schema.json`. Import
them together; this advances the session to `gold-ready` only when the complete
source, gold selections and source links validate:

```text
python pipeline/eod.py import-gold \
  --gold /external/private/gold/manual-gold-ledger.json \
  --fidelity-report /external/private/gold/source-fidelity-report.json \
  --session-root /external/private/eod-runtime/sessions/EOD-YYYY-MM-DD-S01

python pipeline/eod.py compare-session \
  --comparison-id CMP-YYYY-MM-DD-001 \
  --session-root /external/private/eod-runtime/sessions/EOD-YYYY-MM-DD-S01

python pipeline/eod.py calibration-report \
  --comparison /external/private/eod-runtime/sessions/EOD-YYYY-MM-DD-S01/comparisons/gold-comparison.json \
  --output /external/private/eod-runtime/sessions/EOD-YYYY-MM-DD-S01/calibration/calibration-report.json \
  --report-id CAL-YYYY-MM-DD-001 \
  --session-root /external/private/eod-runtime/sessions/EOD-YYYY-MM-DD-S01
```

The comparison currently relies on opaque `target_key` identity. Codex creates
and source-verifies that identity through governed review; the deterministic
runtime validates the resulting linkage but does not claim to infer semantics.

## Promotion rule

An imported bundle can reach `candidate-generated`; a completed gold comparison
can reach `comparison-complete`. Neither state means Anki-ready. The
experimental manifest must always retain:

```text
EXPERIMENTAL CANDIDATE — NOT APPROVED FOR ANKI
```

The calibration report always requires another pilot at this stage. Stable
Protocol v3.5 finalisation and all existing Anki gates remain independent and
mandatory.

## Stable-path completion after RM-9

If the learner accepts a corrected notebook after RM-9, continue through the
stable Protocol v3.5 card-design, render, export, import, reconciliation, and
post-cycle gates. Record later card corrections separately from RM-8 so that a
good final card cannot retroactively improve the frozen prediction score.

The private cycle is complete only after the learner-approved master is bound
to the canonical export, import reconciliation passes, and the learner confirms
the rendered cards. Do not change the experimental manifest to
`anki_ready: true`; the stable output is separately approved and does not alter
the frozen experimental candidate's prohibition.
