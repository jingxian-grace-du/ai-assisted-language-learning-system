# Pipeline

This directory contains the Phase 2 structural pilot CLI. It intentionally does
not generate diary language or decide learning value.

Pipeline components must accept private data from explicit external locations and must not write source content into the repository, logs, or test snapshots.

## Current commands

Initialize a private Shadow Mode session outside the repository:

```text
python pipeline/eod.py init-session \
  --private-root /external/private/root \
  --session-id EOD-YYYY-MM-DD-S01
```

Validate the resulting private workspace and structural ledgers:

```text
python pipeline/eod.py validate-session \
  --session-root /external/private/root/sessions/EOD-YYYY-MM-DD-S01
```

Import the private JSON produced by the ChatGPT trigger
`Export the Phase 2 pilot bundle.`:

```text
python pipeline/eod.py import-bundle \
  --bundle /external/private/pilot-bundle.json \
  --session-root /external/private/root/sessions/EOD-YYYY-MM-DD-S01
```

Read a content-free status summary:

```text
python pipeline/eod.py status \
  --session-root /external/private/root/sessions/EOD-YYYY-MM-DD-S01 \
  --json
```

Record a normal session-state transition:

```text
python pipeline/eod.py transition \
  --session-root /external/private/root/sessions/EOD-YYYY-MM-DD-S01 \
  --to night-open
```

Import the complete private source archive handed off from referenced ChatGPT
chats:

```text
python pipeline/eod.py import-source-archive \
  --archive /external/private/source-archive.json \
  --session-root /external/private/root/sessions/EOD-YYYY-MM-DD-S01
```

After the learner independently freezes the manual notebook, Codex performs the
source-fidelity review and materialises the Manual-Gold Ledger. Import both
private artefacts, then run RM-8:

```text
python pipeline/eod.py import-gold \
  --gold /external/private/gold-ledger.json \
  --fidelity-report /external/private/source-fidelity-report.json \
  --session-root /external/private/root/sessions/EOD-YYYY-MM-DD-S01

python pipeline/eod.py compare-session \
  --session-root /external/private/root/sessions/EOD-YYYY-MM-DD-S01 \
  --comparison-id CMP-YYYY-MM-DD-001
```

Create the post-comparison calibration summary:

```text
python pipeline/eod.py calibration-report \
  --comparison /external/private/comparison.json \
  --output /external/private/calibration-report.json \
  --report-id CAL-YYYY-MM-DD-001 \
  --session-root /external/private/root/sessions/EOD-YYYY-MM-DD-S01
```

The comparison engine currently aligns opaque `target_key` values and detects
selection, boundary, learning-function, and Note Type differences. Semantic
fidelity and topic-boundary adjudication remain explicit review stages.

See `docs/phase-2-pilot-runtime.md` for the complete private workflow.
