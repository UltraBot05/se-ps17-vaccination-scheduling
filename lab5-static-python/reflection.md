# Lab 5: Reflection

## Which issues were the easiest to fix, and which were the hardest? Why?

The easiest were the Flake8 style issues and the Pylint naming and docstring messages. The blank
lines, the long lines and renaming `addDue` to `add_due` are mechanical. The tool tells you the
line and what it wants, and there is only one sensible way to do it. The rename touched just two
calls in `main`, so nothing else could break.

The hardest was `eval` in `penalty`. Bandit's hint was to use `ast.literal_eval`, so I tried that
first. It does not accept `50 * 2`, because it only reads literal values and does not do
multiplication. Following the tool's advice as written would have removed the security hole and
the feature with it. I ended up parsing the rule with `ast.parse` and walking the tree in a small
`calc` function that only allows numbers and `+ - * /`. Then I had to decide which exceptions to
catch in place of `except Exception`. A bad rule can raise `SyntaxError` (`1 +`), `ValueError`
(anything that is not plain arithmetic) or `ZeroDivisionError` (`10/0`), so those three are the
only ones caught now.

The mutable default was easy to fix but took a minute to see why it matters. In the original,
`history` was one list shared by every call. Nothing in the demo prints it, so the bug never shows
up when you run the program, only when you read the code.

## Did the static analysis tools report any false positives? If so, describe one example.

B105, the hardcoded password, is the closest to a false positive. Bandit only flagged it because
the variable name has `PASSWORD` in it. Nothing in the program ever reads `TREASURER_PASSWORD`, so
it cannot be used against anything in this file. I still moved it to an environment variable,
because a password in source code ends up in git history forever, and that is a real problem once
the code is pushed.

Pylint and Flake8 also disagree on line length. Flake8 stops at 79 characters and Pylint allows
100. Lines 4 and 15 were "too long" for one tool and fine for the other, so neither report is wrong.
They are just set up differently. I followed the stricter limit so both are clean.

The more interesting point is what the tools missed. `collect` let the same due be collected twice,
which in a real society means a flat could be shown as paying twice. None of the three tools
reported this. Pylint only pointed at that function because of the inconsistent return, and I
found the double collection while fixing that. Also, `rows != None` was flagged by both Pylint
(C0121) and Flake8 (E711) as a style problem, but the real issue was that the check could never be
false. The tools saw how it was written and not that it was pointless.

## How would you integrate static analysis tools into your actual software development workflow?

I would run them at two points. Locally, a pre-commit hook would run Flake8 and Bandit on the
changed files, since both are fast and their messages are easy to act on. A commit with a Medium or
High Bandit issue would be blocked before it ever reaches the repo.

In CI, for example a GitHub Actions workflow on every pull request, all three tools would run.
Pylint would use `--fail-under=9.5` to match this lab's target, Bandit would fail the build on
Medium or higher severity, and Flake8 would fail on any error. Teams would also need a shared
config file (`setup.cfg` or `pyproject.toml`) so that everyone uses the same line length and
nobody fights the 79 vs 100 difference from question 2.

Doing it in this lab also showed me the order matters. I fixed the Bandit issues first. The new
`calc` function then got checked by Pylint in the next round, so the security fix did not add new
quality problems. Running only one tool and stopping would have missed that.

## What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The numbers changed a lot. Pylint went from 5.81 to 10.00, Bandit from 3 issues to none, and
Flake8 from 5 issues to none. The program still prints exactly the same output, `2500`, `100` and
`['A-102']`, so nothing it did before was lost.

Robustness improved in ways the demo does not show but I checked separately:

- A flat name with a quote in it is now stored as text instead of being run as SQL.
- A late fee rule like `__import__("os")` now gives a fee of 0 instead of running code.
- Collecting the same due a second time now returns `None` instead of 2500 again.
- Two calls to `add_due` now return separate history lists instead of sharing one.

For readability, every function now has a docstring that says what it returns, including the
`None` case for `collect`. The long SQL lines are split so they can be read without scrolling.

What it did not fix: the database connection is still one global at the top of the file, and
there are no tests. The tools were happy with both. A 10.00 score means the code follows the rules
the tools know about, not that it is correct, and the double collection bug is the proof of that.
