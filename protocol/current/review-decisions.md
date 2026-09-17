# Protocol v3.5 review decisions

This document records the first complete section-level review of the migrated
v3.5 baseline. It explains how the migration distinguishes normative behaviour
from supporting explanation and repeated operational detail.

## Review policy

1. A normative requirement states an independently testable obligation,
   prohibition, permission boundary, authority rule, or release condition.
2. Headings, purposes, examples, enumerated field names, and workflow diagrams
   remain in the readable protocol but do not automatically become separate
   requirements.
3. A list item becomes a separate requirement only when it can fail
   independently and needs independent evidence.
4. Repeated summaries link back to the governing requirement instead of
   creating duplicate requirements.
5. Anki click-by-click instructions are operational profiles. Stable data,
   mapping, and reconciliation invariants are normative; interface navigation
   is not unless the operation itself changes system state or safety.
6. Existing v3.5 rules are baselined before new raw-material-generation rules
   are introduced.

## Section decisions

### 1. Core principles

Preservation of learner meaning, separation of learning stages, contextual
learning, and the Review Notebook's editing role are normative system
principles. Lists describing their purpose remain supporting context.

### 2. Night session

Free-speaking boundaries, correction limits, checkpoint source order,
immutability, topic-completeness auditing, zero-rewrite aggregation, reopening,
and scheduling truthfulness are normative. Literal trigger phrases are an
operational interface profile and should not be duplicated as product
principles.

### 3. Morning review

Answer non-disclosure, uninterrupted retelling, comparison boundaries, and use
of retrieval performance as selection evidence are normative. The fixed 08:30
time is a configurable operational default rather than an essential learning
principle.

### 4. Notebook sources and selection

Formatting semantics, evidence priority, prediction confidence, calibration
stage isolation, source authority, source fidelity, ledgers, coverage states,
build gates, error-class rescans, and protocol-change auditing are normative.
Examples of possible marks and candidate expressions are explanatory.

The ten end-to-end gates are normative workflow states. Their long checklists
must be decomposed into independently verifiable conditions and linked back to
the relevant underlying requirements.

### 5. Review Notebook v1

Editable-document delivery, topic organisation, semantic consolidation, stable
internal identity, late display numbering, Note Type choice, placement order,
and the authority of user edits are normative. Display field lists are schema
constraints rather than prose requirements.

### 6. Anki Note Types

Retrieval purpose, context requirements, target boundaries, cue leakage,
translation completeness, paired-source identity, Vocabulary answerability,
evidence, Guidance completeness, and bidirectional alignment are normative.
Illustrative Cloze strings remain examples and must not enter conformance data
as learner content.

### 7. Topic Retell selection

Selection must be based on discourse progression and complete reasoning rather
than sentence count, paragraph length, or broad topic alone. Lists of common
logical patterns explain the rule; each pattern does not require its own ID.

### 8. Paired Context Cloze and Topic Retell

One-to-one pairing, one canonical English source, permitted format differences,
prohibited content changes, duplicate prevention, and exact pre-export identity
are normative.

### 9. Tags and decks

The four stable destinations, first-level Topic constraint, non-redundancy,
Type admission, controlled expansion, and set audit are normative. Current tag
names and deck names are configuration profiles. Example dates and candidate
Type names are non-normative examples.

### 10. Review and finalisation

Edited-source authority, independent audit families, global error-class scans,
Guidance linked invalidation, stop conditions, preservation of unaffected
content, stage isolation, and confirmation before master archiving are
normative.

### 11. Anki export and import

Canonical Note Type contracts, field order, UTF-8 no-header exports, HTML
preservation, canonical-versus-temporary-copy boundaries, destination mapping,
and database reconciliation are normative. Click sequences are operational
instructions and should become adapter documentation rather than core protocol
requirements.

### 12. First import validation

Rendered behaviour, field mapping, counts, duplicate behaviour, and
content-versus-implementation fault isolation are normative. One-time setup
steps are operational profiles.

### 13–15. Summary, automation, and triggers

These sections restate earlier rules for execution. They should link to stable
requirement IDs rather than create duplicates. Scheduling defaults and literal
trigger phrases belong to configuration. The rule not to claim success before
an external action succeeds remains normative.

## Decisions deferred to product configuration

The following are not blockers for requirement migration and should become
configuration rather than hard-coded universal rules:

- morning review time;
- literal conversational trigger phrases;
- filesystem locations;
- deck and Note Type display names;
- approved Topic vocabulary;
- UI-specific Anki navigation steps.

## Current completion criterion

The migration is complete only when every clause has one recorded disposition:

- mapped to one or more stable requirements;
- retained as non-normative context;
- retained as an operational profile;
- superseded with a reason; or
- escalated as a material product ambiguity.

The requirement coverage matrix measures this condition and prevents silent
omission.
