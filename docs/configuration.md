# Configuration boundaries

The core protocol defines learning and quality invariants. Environment-specific
choices belong to configuration and must not be mistaken for universal learning
principles.

Configurable values include:

- morning review time and time zone;
- accepted conversational trigger phrases;
- external private-data root;
- canonical archive location outside the repository;
- parent and subdeck display names;
- Anki Note Type display names;
- approved first-level Topic vocabulary;
- rendering profile and supported display modes;
- confidence thresholds for automatic, sampled, and mandatory review.

Configuration may specialise a protocol requirement but may not weaken source
authority, semantic fidelity, privacy, build-blocking gates, or reconciliation.

Real configuration files that contain local paths or account details must remain
untracked. A future public configuration template may contain placeholders only.
