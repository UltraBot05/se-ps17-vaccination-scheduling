# Lab 3: Component Modelling and Architectural Pattern Selection

Abhigyan Dutta, PES2UG24CS019, 5A CSE
Problem Statement 17, Vaccination Cohort and Dose Scheduling System

The requirements and use cases from Lab 1, and the epics from Lab 2, are used here to choose an
architectural style and lay out the system as a UML component diagram.

## Architecture chosen

**Microservices.** The system already splits into the five functional areas that were run as
separate epics in Lab 2, each with its own sprint. Microservices keeps that separation at the
architecture level instead of folding five independent concerns back into one shared application.
The full reasoning, including the security and performance points the handout asks for, is in
`docs/PES2UG24CS019_SE_Lab3.docx`.

## Components

Seven components plus the two external systems already established in Lab 1.

| Component | Role |
|---|---|
| Citizen Portal | client used by the citizen registrant |
| Officer Console | client used by the vaccination officer, including QR verification |
| Registration & Cohort Service | signs a citizen up and assigns exactly one cohort |
| Booking & Scheduling Service | books a slot, enforces the dose gap and session capacity |
| Dose Recording Service | records a dose against a confirmed booking |
| Certificate Service | issues and verifies the signed QR certificate |
| Policy Configuration Service | holds the cohort rules, dose gap and capacity settings |
| National ID Service *(external)* | verifies a citizen's government ID |
| Certificate Authority *(external)* | signs the certificate |

Only Citizen Registrant and Vaccination Officer are named as actors in the official problem
statement. Health Administrator, National ID Service and Certificate Authority were added with
justification back in Lab 1, and are carried forward here for consistency across the submission.

## Folder contents

```
diagrams/
  component-diagram.png         the deliverable diagram
  component-diagram.pdf         same diagram, as PDF
  component-diagram.drawio.xml  editable source, open at app.diagrams.net
docs/
  PES2UG24CS019_SE_Lab3.docx    the one page justification
```

## Notation used

Solid line ending in a ball (filled circle) and a socket (open arc) is an assembly connector: the
ball sits on the component that provides the interface, the socket on the component that requires
it. The one dashed arrow, Dose Recording Service to Certificate Service, is a `<<use>>` dependency,
since recording a dose triggers issuing a certificate without either component needing to expose an
interface for it.
