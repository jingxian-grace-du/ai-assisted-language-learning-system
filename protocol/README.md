# Protocol workspace

This directory holds the versioned, privacy-reviewed protocol specification and
its emerging machine-readable requirement catalogue.

The v3.5 Word source has been migrated as a legacy baseline after review for:

- references to private notebook titles, source paths, or session content;
- normative requirements that need stable identifiers;
- duplicated rules introduced through iterative patches;
- rules that describe implementation rather than required behaviour;
- gates that lack machine-readable inputs, outputs, and failure conditions;
- inconsistencies between prose, schemas, validators, and Anki behaviour.

Current structure:

```text
protocol/
├── current/
│   ├── protocol.md
│   ├── requirements.json
│   └── migration-trace.json
├── requirements.schema.json
└── README.md
```

The protocol is normative. Overview documents explain the system but do not override it.

`protocol.md` contains stable `legacy-pNNNN` anchors corresponding to the source
Word paragraphs. `requirements.json` currently contains the first baselined
cross-process requirements. It is not yet a complete atomic representation of
all v3.5 normative clauses.

Migration changes are limited to privacy and portability transformations and
are recorded in `migration-trace.json`.
