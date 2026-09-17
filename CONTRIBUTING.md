# Contributing

Contributions must preserve the project's learning philosophy, source fidelity, and privacy boundary.

## Never commit private learning content

Do not add real or lightly anonymised:

- oral diaries or transcripts;
- AI conversation exports;
- personal notebooks or manual annotations;
- Anki notes, collections, or import files;
- screenshots, recordings, logs, prompts, or error traces containing session content;
- names, relationships, events, locations, dates, or combinations of details derived from a learner's life.

Removing names is not sufficient. Context can remain identifying. When a technical test eventually needs content, write a wholly synthetic fixture from scratch and label it as synthetic.

## Documentation changes

Keep these distinctions clear:

- product philosophy describes why the system exists;
- the protocol specifies required behaviour and gates;
- schemas define machine-readable contracts;
- implementation code performs transformations;
- validators determine whether an artefact may advance;
- evaluation measures system quality against approved standards.

Do not present an implementation shortcut as a protocol principle, or add a new rule merely to conceal a failure to execute an existing rule.

## Change requirements

Every material change should state:

1. the problem being addressed;
2. the authority or evidence supporting the change;
3. the affected pipeline stage and gates;
4. new failure modes introduced by the change;
5. tests or validation needed;
6. whether the change affects privacy or data retention.

## Protocol changes

Protocol revisions require a changelog entry. A revision should distinguish:

- existing rule — execution failure;
- existing rule — ambiguous or insufficiently enforced;
- missing generalisable rule;
- one-off preference;
- technical or operational issue.

Only reusable missing or insufficient rules belong in the protocol.
