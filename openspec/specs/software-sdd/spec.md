# software-sdd Specification

## Purpose
Define a shared specification-driven workflow for software governed by AI-Workspace, preserving institutional controls for SITOP V2 and lighter documentation for Tribe Sport while maintaining traceable implementation and honest verification.

## Requirements

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

### Requirement: SDD-002 Preserve project documentation profiles
The workflow SHALL preserve SITOP V2 institutional controls and SHALL use lighter documentation for Tribe Sport without removing test traceability.

#### Scenario: Institutional project
- **WHEN** the target is SITOP V2
- **THEN** proposal, specs, design, tasks and verification reference the applicable F0 through F5 records without fabricating approval

#### Scenario: Tribe Sport project
- **WHEN** the target is Tribe Sport
- **THEN** the Django and Railway change maintains specification, design, tasks, test evidence and release notes without mandating F0 through F5

### Requirement: SDD-003 Verify before completion
The workflow MUST distinguish structural OpenSpec validation from executed application tests, acceptance and deployment authorization. Tasks SHALL be completed only with real corresponding evidence.

#### Scenario: Structurally valid but untested
- **WHEN** OpenSpec validates successfully and application tests were not run
- **THEN** verification states the tests are NOT_RUN and does not claim acceptance or production readiness

#### Scenario: Failed or skipped tests
- **WHEN** a relevant test fails or is skipped
- **THEN** verification records its actual status and the unresolved requirement instead of reporting the change as fully verified

### Requirement: SDD-004 Keep product knowledge at its source
Each software repository SHALL keep its own OpenSpec specifications and change artifacts under version control. AI-Workspace SHALL keep reusable policies and Engram SHALL retain decisions with project separation.

#### Scenario: Resume on another machine
- **WHEN** work resumes after repositories are synchronized
- **THEN** the developer reads the product change, AI-Workspace revision and relevant project memory without relying on chat history or an automatic sync assumption

### Requirement: SDD-005 Reproducible tooling
AI-Workspace SHALL pin and lock the tested OpenSpec development dependency and provide project configuration templates without silently overwriting existing project configuration.

#### Scenario: Existing application setup
- **WHEN** a target repository already has OpenSpec or agent instructions
- **THEN** adoption compares and merges applicable guidance while retaining existing work and recording the selected tool version
