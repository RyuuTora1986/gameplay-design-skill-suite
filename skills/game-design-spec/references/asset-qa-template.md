# Asset QA Template

Use this file to add acceptance gates for chapter 4, chapter 8, chapter 9, and chapter 10.

## Goal

Do not accept an asset because it looks roughly correct in isolation.

Judge it against:

- consistency
- readability
- implementation fit
- export readiness

## UI acceptance table

| Check area | Pass condition |
|---|---|
| target resolution | Main information remains readable at the declared target resolution |
| visual hierarchy | Player sees the primary action and primary status first |
| state coverage | Default, disabled, error, success, and onboarding states are visually distinguishable |
| interaction clarity | Click, drag, confirm, cancel, and close targets are obvious |
| style consistency | Page uses the locked style anchor without drift |
| coding fit | Naming and component structure can map to implementation files |

## Art acceptance table

| Check area | Pass condition |
|---|---|
| silhouette clarity | Main shape reads correctly before details are inspected |
| gameplay readability | Asset does not hide clickable or time-critical information |
| family consistency | Assets in the same family share palette, line, and shape language |
| export readiness | Resolution, transparent background, slices, and naming are correct |
| forbidden drift | Asset does not slide into banned styles |
| production fit | Asset complexity matches the project scale |

## Audio acceptance table

| Check area | Pass condition |
|---|---|
| emotional match | Music or sound matches the scene promise |
| trigger readability | The player can understand what action or state caused the sound |
| repetition control | Short sounds do not become irritating under frequent repetition |
| mix priority | Warnings, actions, and results remain distinguishable |
| integration fit | File naming, duration, and format match implementation requirements |

## Batch rejection rules

Reject the whole batch for correction if:

- more than 20 percent of assets in the batch drift from the style anchor
- more than 10 percent of assets cannot be integrated without manual renaming or re-export
- UI readability fails on the target resolution
- important audio triggers are confused with each other

## Recommended chapter usage

- chapter 4: include UI acceptance items
- chapter 8: include art acceptance items
- chapter 9: include audio acceptance items
- chapter 10: convert the chosen acceptance items into explicit QA cases
