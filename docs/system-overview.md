# System overview

## Two-stage system

### Stage 1 — Habit and meaningful output

The learner conducts recurring English oral-diary conversations. The system encourages continued English communication, description of unknown concepts, and gradual topic awareness. The output is private raw material, not a polished performance.

### Stage 2 — Governed memory pipeline

The system transforms selected raw material into retrievable learning units and reconciles those units with Anki.

During Phase 2 Shadow Mode, ChatGPT is the diary and first-prediction runtime:
it captures the night/morning cycle, produces the Experimental Candidate, and
freezes RM-0 through RM-7 in a Pilot Bundle. Codex is the calibration and
control runtime: it preserves complete referenced source chats privately,
validates the independent manual notebook, materialises manual gold, runs RM-8
and RM-9, and converts only generalisable findings into repository changes.

## Target pipeline

| Stage | Purpose | Primary output |
|---|---|---|
| Intake | Establish session boundaries and source identity | Immutable source record |
| Segmentation | Reconstruct coherent topics from unstructured dialogue | Topic spans |
| Signal detection | Identify evidence of a real learning need | Learning-signal register |
| Candidate selection | Choose useful, reusable targets and reject noise | Candidate ledger |
| Notebook generation | Build source-grounded learning units | Structured notebook |
| Content validation | Check authority, meaning, coverage, and target boundaries | Gate results |
| Card design | Map content into appropriate retrieval tasks | Typed Anki-note records |
| Render/export validation | Check visible output and canonical exports | Validated artefacts |
| Import reconciliation | Confirm Anki types, fields, tags, decks, HTML, and counts | Reconciliation report |
| Post-cycle learning | Classify failures and propose reusable improvements | Protocol delta ledger |

## Learning-note roles

The current design uses four roles:

- **Context Cloze** tests expressions inside meaningful personal context.
- **Topic Retell** requires active reconstruction of a complete paired passage.
- **Vocabulary** supports expressions that are independently retrievable and useful outside one passage.
- **Guidance** preserves reusable reasoning, advice, conditions, and conclusions, with tightly aligned prompts and answers.

The protocol, not this overview, is the normative source for exact fields and gates.

## Authority and provenance

Every derived unit should identify the authoritative source span and the transformations applied to it. Generated text cannot validate itself or silently override a higher-authority source.

The intended machine-readable lineage is:

```text
source session
→ source span
→ topic
→ learning signal
→ selected target
→ notebook unit
→ Anki note
→ import reconciliation result
```

For Shadow Mode calibration, an additional private lineage applies:

```text
complete referenced ChatGPT chats
→ private source archive
→ independent manual notebook
→ source-fidelity report
→ Manual-Gold Ledger
→ RM-8 comparison
→ RM-9 calibration
→ privacy-safe protocol delta
```

## Human review as exception handling

The automation goal is not to eliminate acknowledgement of uncertainty. It is to classify work by confidence and risk:

- high-confidence units may advance through automatic gates;
- medium-confidence units may enter sampling or focused comparison;
- contradictory, ambiguous, or high-impact units require explicit review;
- validation failures block export.

Human effort should move from rewriting every result to resolving evidence the system cannot safely decide.

## Separation of concerns

The implementation should keep these components independent:

- extractors identify structure and evidence;
- selectors rank learning value;
- generators produce typed units;
- validators test invariants;
- exporters serialise validated data;
- adapters interact with external tools such as Anki;
- evaluators compare system output with approved standards.

This separation makes it possible to improve generation without weakening validation.
