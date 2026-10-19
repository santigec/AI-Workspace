## ADDED Requirements

### Requirement: CG-001 Reproducible local installation
AI-Workspace SHALL pin CodeGraph and its lockfile as a local development tool and SHALL provide reproducible setup instructions.

#### Scenario: Install on the current machine
- **WHEN** the tool is installed
- **THEN** its CLI reports the pinned version and can initialize and query a local project index

### Requirement: CG-002 Project scoped navigation
CodeGraph queries MUST identify the intended project and SHALL use bounded context for structural exploration. Generated indexes MUST remain local and excluded from version control.

#### Scenario: Explore a software project
- **WHEN** an indexed software project is queried
- **THEN** the result is scoped to that project and includes source references appropriate to the task

#### Scenario: Missing or stale index
- **WHEN** the index is absent, outdated or unsupported for the task
- **THEN** the agent identifies the limitation and uses targeted file tools or a justified index update rather than inventing graph coverage

### Requirement: CG-003 Verified integration
The setup SHALL preserve existing Codex configuration, expose only the intended navigation tools and distinguish configured MCP from a tool available in the current chat.

#### Scenario: Register MCP
- **WHEN** CodeGraph is registered for Codex
- **THEN** existing unrelated server entries remain intact and a protocol handshake and query verify the server independently of a config-only claim

### Requirement: CG-004 Honest efficiency and evidence
Guidance MUST avoid redundant whole-file reads while retaining necessary verification of edited code, runtime behavior and graph freshness. It MUST NOT claim measured token savings without a comparable measurement.

#### Scenario: Inspect a result
- **WHEN** a graph result already includes sufficient current source context
- **THEN** the agent reuses that context and reads only missing or conflicting code, while executing relevant tests separately

#### Scenario: Fresh machine
- **WHEN** another machine clones AI-Workspace
- **THEN** the user installs the pinned tools and configures that local Codex instance and rebuilds per-project indexes instead of assuming MCP or SQLite state synced through Git
