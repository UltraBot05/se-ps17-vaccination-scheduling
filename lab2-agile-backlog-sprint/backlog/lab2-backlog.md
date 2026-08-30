# Lab 2 working sheet: backlog and sprint plan

Vaccination Cohort and Dose Scheduling System, Problem Statement 17
Abhigyan Dutta, PES2UG24CS019, 5A CSE

This is not a submission document. It is the sheet I typed into Jira, kept in the repo so the board
can be rebuilt if the Jira space is ever lost, and so it is clear where each story came from. The
five functional and two non-functional requirements from Lab 1 are the only input.

Five epics, seventeen user stories, 101 story points, two sprints.

### How to read a story entry

Each story below has three parts, and they are used differently:

- **Paste** — the description text. Copy it into the Description box in Jira exactly as written.
- **Fields** — values to set in the create dialog. Not typed into the description.
- **From** — which Lab 1 requirement or use case the story came from. **This goes nowhere in
  Jira.** It exists so that when someone in the viva asks why a story exists, the answer is on
  hand. It is also what the coverage table at the bottom of this file is built from.

Note that **Story Points cannot be set in the Jira create dialog** — the field only appears on the
view screen. Create each story with the other fields, then sweep down the backlog afterwards
clicking the points badge on each row.

---

## The epics

| Epic   | Title                                        | Stories | Points | Built from                          |
| ------ | -------------------------------------------- | ------- | ------ | ----------------------------------- |
| EPIC-1 | Citizen registration and cohort assignment   | 3       | 16     | FR-002, UC-01, UC-07                |
| EPIC-2 | Slot booking and dose interval enforcement   | 6       | 29     | FR-001, FR-003, UC-02, UC-03, UC-08 |
| EPIC-3 | Dose administration and recording            | 3       | 14     | FR-004, UC-04, UC-10                |
| EPIC-4 | Certificate issuance and verification        | 2       | 21     | FR-005, NFR-001, UC-05, UC-09       |
| EPIC-5 | Policy administration and platform readiness | 3       | 21     | NFR-002, UC-06                      |

I split the requirements this way because each epic is a stretch of the citizen's journey that
could be demoed on its own. The alternative was one epic per requirement, but FR-001 and FR-003
both happen inside the same booking screen, so keeping them apart would have meant two epics that
nobody could show separately.

Story points come from the Fibonacci series, the same one the handout describes. I used Story 1.2
as my anchor at 3 points, since it is a plain form with validation and nothing unknown about it,
and sized everything else against that.

---

## EPIC-1: Citizen registration and cohort assignment

**Epic description to paste:**

> A citizen makes an account, the government ID is checked, and the citizen lands in exactly one
> priority cohort so the rollout can be opened one cohort at a time.

### Story 1.1, Register with government ID

Paste:

```
As a citizen registrant,
I want to sign up using my government ID,
So that my identity is checked before I am allowed to book anything.
```

Fields: Parent `Citizen registration and cohort assignment` · Priority `High` · Points `5`
From: UC-01 and the National ID Service

### Story 1.2, Declare age, occupation and health condition

Paste:

```
As a citizen registrant,
I want to enter my age group, job category and any health condition when I sign up,
So that the system has what it needs to work out my priority.
```

Fields: Parent `Citizen registration and cohort assignment` · Priority `High` · Points `3`
From: FR-002

### Story 1.3, Get put into exactly one cohort

Paste:

```
As a citizen registrant,
I want the system to place me in exactly one cohort and show it on my dashboard,
So that I know which phase of the rollout I am in and when my turn opens.
```

Fields: Parent `Citizen registration and cohort assignment` · Priority `High` · Points `8`
From: FR-002 and UC-07

---

## EPIC-2: Slot booking and dose interval enforcement

**Epic description to paste:**

> A citizen finds a session at a centre and books it, while the system holds the two rules that
> cannot be held anywhere else, the dose gap and the session capacity.

### Story 2.1, Search sessions by centre and date

Paste:

```
As a citizen registrant,
I want to search sessions by district or centre and a date range,
So that I can find a slot I can actually reach.
```

Fields: Parent `Slot booking and dose interval enforcement` · Priority `High` · Points `5`
From: steps 3 to 5 of UC-02

### Story 2.2, Block a Dose 2 booking that is too early

Paste:

```
As a health administrator,
I want Dose 2 bookings refused until the configured gap has passed since Dose 1,
So that no citizen gets a second dose that does not work.
```

Fields: Parent `Slot booking and dose interval enforcement` · Priority `High` · Points `8`
From: FR-001 and UC-08

### Story 2.3, Show the earliest date instead of just refusing

Paste:

```
As a citizen registrant,
I want to be told the exact date my Dose 2 booking opens when I am too early,
So that I can plan for it instead of trying again and again.
```

Fields: Parent `Slot booking and dose interval enforcement` · Priority `Medium` · Points `3`
From: alternate flow 2a of UC-02

### Story 2.4, Refuse bookings once a session is full

Paste:

```
As a vaccination officer,
I want the system to stop taking bookings once a session hits its capacity,
So that my centre does not get more people than it can handle in that session.
```

Fields: Parent `Slot booking and dose interval enforcement` · Priority `High` · Points `5`
From: FR-003

### Story 2.5, Confirm a booking and get a reference

Paste:

```
As a citizen registrant,
I want a booking reference and a confirmation message once I confirm a slot,
So that I have something to show at the centre.
```

Fields: Parent `Slot booking and dose interval enforcement` · Priority `High` · Points `3`
From: steps 8 and 9 of UC-02

### Story 2.6, Move an appointment to another session

Paste:

```
As a citizen registrant,
I want to reschedule my appointment,
So that a change of plans does not cost me my place in the rollout.
```

Fields: Parent `Slot booking and dose interval enforcement` · Priority `Medium` · Points `5`
From: UC-03

---

## EPIC-3: Dose administration and recording

**Epic description to paste:**

> The officer at the centre records what was actually injected, with enough detail that a recalled
> batch can be traced back to the people who got it.

### Story 3.1, Record a dose against a confirmed appointment

Paste:

```
As a vaccination officer,
I want to save the dose number, batch number, date and time, and my officer ID,
So that every dose given can be traced if that batch is recalled later.
```

Fields: Parent `Dose administration and recording` · Priority `High` · Points `8`
From: FR-004 and UC-04

### Story 3.2, Refuse a duplicate dose record

Paste:

```
As a vaccination officer,
I want a second save against the same appointment to be refused,
So that a citizen's record is not spoiled by a double entry.
```

Fields: Parent `Dose administration and recording` · Priority `High` · Points `3`
From: FR-004

### Story 3.3, Log an adverse event

Paste:

```
As a vaccination officer,
I want to record a reaction against a dose that was already given, if there is one,
So that a problem with a batch becomes visible to the administration.
```

Fields: Parent `Dose administration and recording` · Priority `Low` · Points `3`
From: UC-10, which only extends UC-04, so it is optional by design

---

## EPIC-4: Certificate issuance and verification

**Epic description to paste:**

> Turn a saved dose record into a certificate a stranger can trust, and make checking it fast
> enough to use at a gate with a queue behind it.

### Story 4.1, Issue a signed QR certificate

Paste:

```
As a citizen registrant,
I want a signed QR certificate ready within two minutes of my dose being recorded,
So that I have proof of vaccination that other people can check.
```

Fields: Parent `Certificate issuance and verification` · Priority `Medium` · Points `8`
From: FR-005, UC-09 and the Certificate Authority

### Story 4.2, Verify a certificate QR at the gate

Paste:

```
As a vaccination officer,
I want to scan and check a QR in under 150 ms whether or not I have internet,
So that the queue keeps moving and a fake certificate gets caught.
```

Fields: Parent `Certificate issuance and verification` · Priority `High` · Points `13`
From: NFR-001 and UC-05

---

## EPIC-5: Policy administration and platform readiness

**Epic description to paste:**

> Give the administration the controls that the enforcement rules read from, and make the platform
> survive the moment every day when booking opens.

### Story 5.1, Set the cohort rules and the dose gap

Paste:

```
As a health administrator,
I want to define the cohorts and set the minimum gap between doses,
So that the rules can be changed without waiting for a new release.
```

Fields: Parent `Policy administration and platform readiness` · Priority `High` · Points `5`
From: UC-06, feeding FR-001 and FR-002

### Story 5.2, Set the session capacity of each centre

Paste:

```
As a health administrator,
I want to set how many appointments each session at a centre can take,
So that bookings never go past what the centre can actually deliver.
```

Fields: Parent `Policy administration and platform readiness` · Priority `High` · Points `3`
From: FR-003 and UC-06

### Story 5.3, Survive the rush when booking opens

Paste:

```
As a health administrator,
I want 5000 booking requests at once served at p95 of 2 seconds with no slot given to two people,
So that the daily rush does not bring the platform down or oversell a session.
```

Fields: Parent `Policy administration and platform readiness` · Priority `Medium` · Points `13`
From: NFR-002 and alternate flow 7a of UC-02

---

## Points sweep reference

For the pass down the backlog after all stories exist.

| Story | Points |  | Story           | Points        |
| ----- | ------ | - | --------------- | ------------- |
| 1.1   | 5      |  | 3.1             | 8             |
| 1.2   | 3      |  | 3.2             | 3             |
| 1.3   | 8      |  | 3.3             | 3             |
| 2.1   | 5      |  | 4.1             | 8             |
| 2.2   | 8      |  | 4.2             | 13            |
| 2.3   | 3      |  | 5.1             | 5             |
| 2.4   | 5      |  | 5.2             | 3             |
| 2.5   | 3      |  | 5.3             | 13            |
| 2.6   | 5      |  | **Total** | **101** |

---

## Sprint plan

Two sprints of one week each. Not everything is sprinted. Three stories are left in the backlog on
purpose, which is closer to how a real sprint ends than a backlog that empties perfectly.

### Sprint 1, eight stories, 40 points

Goal: a citizen can register, land in a cohort, and confirm a first booking, with the dose gap
already being enforced.

| Story | Title                                        | Priority | Points |
| ----- | -------------------------------------------- | -------- | ------ |
| 5.1   | Set the cohort rules and the dose gap        | High     | 5      |
| 5.2   | Set the session capacity of each centre      | High     | 3      |
| 1.1   | Register with government ID                  | High     | 5      |
| 1.2   | Declare age, occupation and health condition | High     | 3      |
| 1.3   | Get put into exactly one cohort              | High     | 8      |
| 2.1   | Search sessions by centre and date           | High     | 5      |
| 2.2   | Block a Dose 2 booking that is too early     | High     | 8      |
| 2.5   | Confirm a booking and get a reference        | High     | 3      |

The two administrator stories sit at the very top on purpose. The system cannot enforce a gap that
nobody has configured yet, so 5.1 has to be done before 2.2 and 5.2 before 2.4. They look like
boring settings screens but they are really dependencies.

### Sprint 2, six stories, 40 points

Goal: a booked citizen can be dosed at a centre and walk out with a certificate that the officer at
the next gate can check.

| Story | Title                                           | Priority | Points |
| ----- | ----------------------------------------------- | -------- | ------ |
| 2.3   | Show the earliest date instead of just refusing | Medium   | 3      |
| 2.4   | Refuse bookings once a session is full          | High     | 5      |
| 3.1   | Record a dose against a confirmed appointment   | High     | 8      |
| 3.2   | Refuse a duplicate dose record                  | High     | 3      |
| 4.1   | Issue a signed QR certificate                   | Medium   | 8      |
| 4.2   | Verify a certificate QR at the gate             | High     | 13     |

### Left in the backlog, three stories, 21 points

| Story | Title                                  | Why it is still sitting there                                                 |
| ----- | -------------------------------------- | ----------------------------------------------------------------------------- |
| 2.6   | Move an appointment to another session | A citizen can cancel and book again, so this can wait                         |
| 3.3   | Log an adverse event                   | UC-10 only extends UC-04, so the main flow is complete without it             |
| 5.3   | Survive the rush when booking opens    | Needs load testing infrastructure that does not exist until booking is stable |

---

## Checking nothing from Lab 1 got dropped

| Requirement                       | Stories that cover it | Sprint               |
| --------------------------------- | --------------------- | -------------------- |
| FR-001 dose interval              | 2.2, 2.3, 5.1         | 1 and 2              |
| FR-002 exactly one cohort         | 1.2, 1.3, 5.1         | 1                    |
| FR-003 session capacity           | 2.4, 5.2              | 1 and 2              |
| FR-004 dose record                | 3.1, 3.2              | 2                    |
| FR-005 certificate in two minutes | 4.1                   | 2                    |
| NFR-001 verify under 150 ms       | 4.2                   | 2                    |
| NFR-002 5000 bookings at once     | 5.3                   | still in the backlog |

Same idea as the traceability matrix I added at the end of Lab 1. It is not asked for, but it is a
quick way to be sure no requirement ended up without a story behind it.
