# Lab 2: Sprint reflection

Vaccination Cohort and Dose Scheduling System, Problem Statement 17
Abhigyan Dutta, PES2UG24CS019, 5A CSE

The backlog was built from the five functional and two non-functional requirements written in Lab 1.
Five epics, seventeen user stories, 101 story points in total.

| | Sprint 1 - Reg & Booking | Sprint 2 - Doses & Certificates |
|---|---|---|
| Ran | 27 Aug 12:00 AM to 30 Aug 11:11 PM | 29 Aug 11:21 PM to 30 Aug 11:23 PM |
| Stories | 8 | 6 |
| Points committed | 40 | 40 |
| Points completed | 40 | 40 |

Three stories worth 21 points were left in the backlog at the end and never sprinted.

---

## 1. Did the estimates match the actual effort?

The honest answer is that this exercise cannot tell me. Nothing was built, so there is no actual
effort to compare against. Both sprints closed at 40 of 40 points because I moved the cards, not
because the work went as planned. Any claim that my estimates were accurate would be made up.

What I can do is say which estimates I would change now, on reflection.

I used Story 1.2 as the anchor at 3 points, because it is a plain form with validation and there is
nothing unknown about it, and sized everything else against that.

Story 4.2, checking a QR in under 150 ms both online and offline, got 13 points. Looking at it
again, that number was carrying my uncertainty rather than the amount of work. Verifying offline
means the Certificate Authority public key has to reach every device at every centre and be rotated
when it changes, and that is a distribution problem more than a coding one. If I had split it into
an online check and a separate key distribution story, I would have had two honest estimates
instead of one 13 that hides a question I never answered. A 13 in a two week sprint is usually a
sign the story has not been broken down enough.

Story 1.3, cohort assignment at 8 points, is probably too high. The rule itself is a lookup over
age band, occupation and declared condition. The hard part is agreeing what the cohorts are, and
that decision actually sits in Story 5.1, which was in the same sprint anyway.

## 2. Was the backlog prioritised well?

Mostly, though one ordering decision needs explaining.

I set priority by user impact, and in a vaccination rollout impact means medical safety before
convenience. So the dose gap story, the capacity story and the duplicate record story are all High
even though none of them is something a citizen would ask for. They are the rules that stop the
system doing harm. The comfort features, showing the earliest eligible date and rescheduling, sit
at Medium.

The decision I had to think about was putting the two administrator stories, 5.1 and 5.2, at the
very top of Sprint 1. Configuration screens feel like low value work and would normally get pushed
back. But the system cannot enforce a gap that has never been configured, so Story 2.2 depends on
5.1 and Story 2.4 depends on 5.2. Here it was right to order by dependency rather than by what the
user can see. I kept that ordering when working the board as well, clearing both configuration
stories to Done before starting on registration.

The part I am less happy with is Story 3.3, logging an adverse event, which I marked Low and then
dropped from both sprints. That follows from the use case model, since UC-10 only extends UC-04 and
the main flow is complete without it, but in a real rollout a reaction that never gets logged is a
patient safety gap. It is Low because it is optional to the flow, not because it does not matter.

## 3. How did the simulated sprint match the plan?

On paper it matched exactly. Both sprints were planned at 40 points and both closed at 40 of 40,
with nothing carried over. That match is not evidence of good planning. It is what happens when one
person drags every card across in a single sitting and nothing can slip.

Two things did go wrong, and they are more interesting than the clean numbers.

**I changed statuses before starting the sprint.** I moved the first five stories from To Do to
Done using the dropdowns on the backlog rows, assuming that dragging stories into the sprint
container had started the sprint. It had not. The Active Sprint board was still empty and the
button still said Start sprint. Jira records nothing in a burndown before the sprint is actually
started, so all that work was invisible. I had to set the five stories back to To Do, start the
sprint properly, and redo the transitions on the board. Planning a sprint and starting one are two
separate actions, which is obvious in hindsight but was not while doing it.

**The sprint dates and the work did not line up.** I set Sprint 1 to start on 27 August so the
burndown would have more than one day on its horizontal axis. But the stories were only created and
added on 30 August, so Jira correctly recorded the sprint as starting with zero points and then
receiving all 40 as scope change three days later. Backdating only helps if the stories are already
in the sprint at that timestamp. It made the chart harder to read, not easier.

What the plan did get right is the sprint goals. Sprint 1 delivers one connected slice, register,
get a cohort, book a first dose with the gap enforced, instead of a scatter of half finished
features. Sprint 2 finishes the journey up to a certificate somebody else can verify, and its
internal ordering follows the same dependency logic, since the dose record is what triggers the
certificate. Either sprint could have been demoed on its own, which is the real test of whether it
was planned properly.

## 4. What did the burndown chart show about capacity?

Both charts have the same shape: the red remaining line sits flat at zero for most of the sprint,
spikes vertically to 40, and drops back to zero almost immediately. The grey guideline runs
underneath it. The event table below each chart explains why, and every row says the same thing:
`Scope change, issue added to sprint`. The Status Report marks every single story with an asterisk
meaning *issue added to sprint after start time*.

So the chart is not really showing work being burned down. It is showing 40 points of scope
arriving in a sprint that started empty, and then being completed at once.

That shape is worth reading properly rather than apologising for, because real teams produce it and
when they do it means something specific. The handout's own notes on burndowns say a sharp drop
during a sprint suggests work has not been estimated accurately or broken down properly, and that
burndowns are useful for spotting scope creep. Both readings apply here. A team whose chart looked
like this would be committing to work after the sprint had already begun, which is the definition
of scope creep, and would be finishing everything in a lump at the end rather than letting it flow
through. Story 4.2 at 13 points is exactly the kind of item that causes the second problem for real.

On capacity, two sprints is nowhere near enough to claim a velocity, and these two are worth even
less than usual because the completions are simulated. Forty points a sprint is a starting
assumption, not a measured number. It would take three or four sprints of real completion data
before it could be used to forecast anything, and the first few of those would probably show that
40 was wrong.

The one honest capacity signal in the whole exercise is that 21 points were consciously left in the
backlog rather than pulled forward to make the numbers look complete. Rescheduling, adverse event
logging and the load test are all real work that a real team would carry into Sprint 3. Deciding
not to commit to them is a better decision than overcommitting and then carrying spillover.
