# Generator Handoff Contract

Use this file when the downstream output is meant for AI coding tools, AI UI tools, or AI image/audio generators.

## Goal

Translate design chapters into machine-friendly generation steps with minimal ambiguity.

## Generator input order

Do not give every tool the whole project at once.

Preferred order:

1. canonical registries
2. system or page scope
3. style anchor
4. pipeline stage
5. acceptance checks
6. export and naming rules

## Per-tool handoff requirements

### AI coding tool

Must receive:

- scene list
- UI page list
- object list
- state machine
- variables and formulas
- success and failure conditions
- acceptance criteria

### AI UI tool

Must receive:

- page purpose
- component list
- state list
- layout zones
- style anchor
- target resolution
- acceptance checks

### AI image generator

Must receive:

- asset family name
- anchor reference
- camera and composition
- export size
- transparency requirement
- forbidden drift terms
- naming rule

### AI audio generator

Must receive:

- event or scene
- emotion
- duration
- loop rule
- timbre preferences
- forbidden sound directions
- format and naming rule

## Required return fields

When a generator step finishes, require it to return:

- generated asset or output name
- pipeline stage completed
- anchor used
- known quality risks
- export format
- files or layers produced

## Rejection conditions

Send the generation step back for revision if:

- it cannot state which anchor it followed
- it cannot state which pipeline stage it completed
- it returns files that do not match the naming contract
- it produces assets that cannot be evaluated by the acceptance checklist
