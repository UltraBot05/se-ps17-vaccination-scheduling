# Lab 5: Static Code Analysis

Individual lab, not tied to the vaccination system. I was given a small Python program with
quality, style and security problems and had to find and fix them using Pylint, Bandit and Flake8.

- Assigned repo: [SETAPESU26/L5_17_society_dues](https://github.com/SETAPESU26/L5_17_society_dues)
- Program: an apartment society maintenance dues ledger. It bills flats, collects payments, works
  out late fees and lists flats that still owe money.
- Deliverable document: [docs/PES2UG24CS019_SE_Lab5.docx](docs/PES2UG24CS019_SE_Lab5.docx)

## Results

| Tool | Before | After |
|------|--------|-------|
| Pylint | 5.81/10 | 10.00/10 |
| Bandit | 3 issues (2 Medium, 1 Low) | No issues identified |
| Flake8 | 5 issues | 0 issues |

The program prints the same output as before: `2500`, `100`, `['A-102']`.

## What was fixed

The main ones. The full table with line numbers is in [issues.md](issues.md).

- **SQL injection.** The INSERT was built with an f-string. It now uses `?` placeholders.
- **`eval` on the late fee rule.** Replaced with a small `ast` based calculator that only allows
  numbers and `+ - * /`.
- **Hardcoded password.** Now read from the `TREASURER_PASSWORD` environment variable.
- **Mutable default `history=[]`.** Now `None`, with a fresh list made inside the function.
- **Broad `except Exception`.** Now catches only the three errors a bad rule can cause.
- **Same due collected twice.** No tool reported this. Found while fixing `collect`.

## Reflection

Full answers to the four reflection questions are in [reflection.md](reflection.md). In short:

- **Easiest and hardest.** The style and naming fixes were mechanical. `eval` was the hardest,
  because Bandit's suggested fix, `ast.literal_eval`, cannot work out `50 * 2` and would have
  broken the late fee feature.
- **False positives.** B105 flagged a password that nothing in the program reads. Flake8 and Pylint
  also disagree on line length (79 vs 100). And none of the tools noticed that the same due could be
  collected twice.
- **Workflow.** Flake8 and Bandit in a pre-commit hook, all three in CI on every pull request, with
  `pylint --fail-under=9.5` and Bandit failing on Medium or higher.
- **Improvements.** Pylint went from 5.81 to 10.00 with the same program output. Injection, code
  execution and double collection were all checked by hand. A 10.00 score still does not mean the
  code is correct.

## Commits

One commit per tool, as the handout asks:

1. Bandit fixes, with all three `before` reports and `bandit_report_after.txt`
2. Pylint fixes, with `pylint_report_after.txt`
3. Flake8 fixes, with the final `after` reports for all three tools, the issue table, the
   reflection and the document

## Running it

```
cd code
python society_dues.py
pylint society_dues.py
bandit -r society_dues.py
flake8 society_dues.py
```

## Layout

```
lab5-static-python/
  code/          cleaned society_dues.py
  reports/       pylint, bandit and flake8 reports, before and after
  docs/          deliverable docx and pdf
  issues.md      issue table
  reflection.md  answers to the four reflection questions
```
