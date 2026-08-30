# Lab 2: Agile Backlog Creation and Sprint Simulation in Jira

Abhigyan Dutta, PES2UG24CS019, 5A CSE
Problem Statement 17, Vaccination Cohort and Dose Scheduling System

The five functional and two non functional requirements written in Lab 1 were turned into a Jira
backlog and run through two sprints. Everything here is built on that lab, so the requirement IDs
below refer back to `../lab1-requirements-usecase/`.

## What was built

A company style Scrum space in Jira with the key `VCDSS`, holding:

- 5 epics
- 17 user stories in the As a, I want, So that form
- 101 story points, estimated on the Fibonacci scale
- 2 sprints of one week each, 40 points per sprint, both started and completed
- 3 stories worth 21 points deliberately left in the backlog

| Epic | Stories | Points | Built from |
|---|---|---|---|
| Citizen registration and cohort assignment | 3 | 16 | FR-002, UC-01, UC-07 |
| Slot booking and dose interval enforcement | 6 | 29 | FR-001, FR-003, UC-02, UC-03, UC-08 |
| Dose administration and recording | 3 | 14 | FR-004, UC-04, UC-10 |
| Certificate issuance and verification | 2 | 21 | FR-005, NFR-001, UC-05, UC-09 |
| Policy administration and platform readiness | 3 | 21 | NFR-002, UC-06 |

Every requirement from Lab 1 is covered by at least one story. The mapping is at the bottom of
`backlog/lab2-backlog.md`.

## Folder contents

```
docs/
  PES2UG24CS019_SE_Lab2.docx   the submitted deliverable
  lab2-reflection.md           the reflection text before it went into Word
backlog/
  lab2-backlog.md              working sheet the Jira board was built from
screenshots/
  01 to 08                     evidence, in reading order
```

`backlog/lab2-backlog.md` is kept so the board can be rebuilt if the Jira space is ever lost. Each
story in it carries the requirement or use case it came from.

## Screenshots

| File | Shows |
|---|---|
| `01-backlog-epics-stories.png` | Backlog with the epic panel open, stories tagged to epics |
| `02-story-points.png` | Story point values, 101 total |
| `03-sprint1-board.png` | Sprint 1 active board across To Do, In Progress and Done |
| `04-sprint2-board.png` | Sprint 2 active board |
| `05-burndown-sprint1.png` | Sprint 1 burndown |
| `06-burndown-sprint2.png` | Sprint 2 burndown |
| `07-sprint-report-sprint1.png` | Sprint 1 report, 40 of 40 completed |
| `08-sprint-report-sprint2.png` | Sprint 2 report, 40 of 40 completed |

The first four are the ones the handout asks for. The rest cover the second sprint and support the
reflection answers.

## Note on the burndown

Both burndown charts show a flat line that spikes to 40 and drops back, rather than a slope. The
sprints were given backdated start dates so the chart would have more than one day on its axis, but
the stories were only added afterwards, so Jira recorded each sprint as starting with zero points
and then receiving all 40 as scope change. The reflection document covers what that shape means and
why it was left as it is.
