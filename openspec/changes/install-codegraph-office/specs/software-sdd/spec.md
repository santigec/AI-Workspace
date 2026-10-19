## MODIFIED Requirements

### Requirement: SDD-001 Specification precedes implementation
All software development governed by AI-Workspace SHALL define the intended behavior, scope and verifiable scenarios in a repository-local OpenSpec change before implementation. Existing behavior MUST be inspected before it is documented as current behavior. Structural exploration SHALL use CodeGraph when available and useful, with explicit project scope and current source references; targeted file tools remain appropriate for unsupported, stale or missing graph context.

#### Scenario: Start a feature
- **WHEN** a developer starts an authorized feature or bug fix
- **THEN** the change records a proposal, requirement scenarios, proportional design and tasks before changing implementation
- **AND** unresolved business decisions remain explicit rather than being invented

#### Scenario: Pure documentation change
- **WHEN** a change has no product behavior impact
- **THEN** its proposal identifies that scope and records applicable checks without inventing product requirements or unnecessary UML

#### Scenario: Explore indexed code
- **WHEN** a developer needs symbol relationships or call flow in an indexed project
- **THEN** a scoped CodeGraph query supplies bounded context before additional file reads, without replacing tests or treating unresolved links as proof of absence
