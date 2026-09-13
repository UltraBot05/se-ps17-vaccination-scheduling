
# Software Engineering Lab Work

Abhigyan Dutta, PES2UG24CS019, 5A CSE
PES University, Department of CSE, Semester 5

Lab work for Problem Statement 17, **Vaccination Cohort and Dose Scheduling System**, under the
Healthcare and Telemedicine domain.

## The system

A public health platform for running a district wide vaccination drive. Citizens register and are
sorted into a single priority cohort, book a slot at a centre, and an officer records the dose
against that booking. A signed QR certificate is issued afterwards that anyone can verify.

Two rules do the real work, because software is the only place they can be enforced:

- a minimum interval between doses, so nobody gets a second dose too early for it to work
- a capacity limit per session, so a centre is never booked past what it can deliver

Certificate trust is the third pillar. A certificate that cannot be checked offline is not much use
at a gate with a queue behind it.

## Labs

| Lab                                          | Topic                                                   | Deliverable                                                            |
| -------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------- |
| [Lab 1](lab1-requirements-usecase/)           | Requirements engineering and UML use case modelling     | Requirements table, use case diagram, use case flow                    |
| [Lab 2](lab2-agile-backlog-sprint/)           | Agile backlog creation and sprint simulation in Jira    | Backlog of epics and stories, two sprints, burndown charts, reflection |
| [Lab 3](lab3-architecture-component-diagram/) | Component modelling and architectural pattern selection | Architecture choice, UML component diagram, one page justification     |

Each lab folder has its own README with the detail.

### Lab 1

Five functional and two non functional requirements, each with acceptance criteria and a rationale.
Five actors and ten use cases, with `include` and `extend` relationships. A full flow for the slot
booking use case, covering the dose gap alternate flow and the case where a session fills up
between listing and confirming.

### Lab 2

The same requirements turned into a Jira backlog: 5 epics, 17 user stories, 101 story points on the
Fibonacci scale. Two one week sprints of 40 points each, both completed, with 21 points deliberately
left in the backlog. Every story traces back to a requirement or use case from Lab 1.

### Lab 3

The five epics from Lab 2 mapped onto a Microservices architecture, with a UML component diagram
covering seven components and the two external systems from Lab 1. A one page justification covers
the architectural choice, two scenario specific reasons, a security advantage and a performance
benefit.

## Layout

```
lab1-requirements-usecase/
  docs/        deliverable docx and pdf
  diagrams/    drawio source and exported png
lab2-agile-backlog-sprint/
  docs/        deliverable docx and pdf
  backlog/     working sheet the Jira board was built from
  screenshots/ evidence for the submission
lab3-architecture-component-diagram/
  docs/        deliverable docx
  diagrams/    drawio source and exported png and pdf
```

Deliverables are named `PES2UG24CS019_SE_LabN`.

## Licence

MIT, see [LICENSE](LICENSE).
