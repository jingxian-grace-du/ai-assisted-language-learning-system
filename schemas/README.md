# Schemas

The first draft machine-readable contracts are now available. They describe
runtime records and validation evidence without containing real learning data.

Current schemas include:

- common identifiers, provenance, source ranges, and privacy metadata;
- source sessions and private source spans;
- reconstructed topics;
- observed learning signals;
- candidates, scores, and selection decisions;
- structured notebook units and Guidance mappings;
- gate results linked to stable requirement IDs;
- validated Anki note records.

Dedicated contracts for transformations, authority conflicts, import
reconciliation, and post-cycle protocol deltas are also included.

Phase 2 adds contracts for session manifests, Topic Evidence Packets, candidate
ledgers, experimental notebook manifests, gold comparisons, and calibration
reports. The Codex handoff additionally defines a complete private source
archive and a source-fidelity report. Experimental notebook manifests hard-code
`anki_ready` to false.

Schemas must contain structural examples only or wholly synthetic values. They must not embed private diary content.
