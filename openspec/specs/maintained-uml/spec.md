# maintained-uml Specification

## Purpose
Maintain editable UML and supported documentation diagrams with reproducible local rendering, explicit code traceability, freshness checks and semantic/visual review as part of each relevant software change.

## Requirements

### Requirement: UML-001 Editable community tooling
Software offices SHALL use editable diagram sources with reproducible local PlantUML or Mermaid tooling appropriate to the diagram type. A rendered image alone MUST NOT substitute the maintained source.

#### Scenario: Formal UML
- **WHEN** a change needs use cases, activities, classes, sequence, states, components or deployment UML
- **THEN** the model preserves its intended semantics and PlantUML source with traceable requirements and proposed or observed scope

#### Scenario: Documentation diagram
- **WHEN** Mermaid is selected
- **THEN** the selected diagram type is supported and a generic flowchart is not falsely labeled as formal UML

### Requirement: UML-002 Verified rendering
The workflow SHALL render and inspect diagram artifacts locally and MUST distinguish syntax validation, visual review and semantic correctness.

#### Scenario: Syntax error
- **WHEN** the source cannot be rendered
- **THEN** the tool exits unsuccessfully and does not record a successful current render

### Requirement: UML-003 Maintained traceability
Each maintained diagram SHALL identify its editable source and relevant local code references. The freshness check MUST detect changes to the source, referenced code, tool versions or generated artifacts.

#### Scenario: Referenced code changes
- **WHEN** referenced code changes after a verified render
- **THEN** the check reports stale status until the diagram is updated or the unchanged model is explicitly reviewed with a reason and re-rendered

#### Scenario: Incomplete manifest
- **WHEN** diagram paths escape the project or required references are invalid
- **THEN** validation rejects the manifest rather than reading arbitrary files or reporting it current

### Requirement: UML-004 Update as part of delivery
Every software change SHALL assess affected UML and update relevant diagrams before completion, or record why no model is affected. Tool upgrades MUST be intentional and validated rather than silently installing latest versions.

#### Scenario: Complete a feature
- **WHEN** a feature affects an existing modeled flow or structure
- **THEN** its tasks include updating model source, rendering, checking freshness and semantic/visual review against the changed code and scenarios

#### Scenario: New machine
- **WHEN** a project is resumed elsewhere
- **THEN** local renderers and artifacts are restored from pinned instructions while editable sources and lightweight traceability remain versioned
