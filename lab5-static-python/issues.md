# Lab 5: Issues found and fixed

File: `code/society_dues.py`. Line numbers refer to the **original** file, as given in the
`*_before.txt` reports. Security and bug issues come first, then quality, then style.

| # | Issue | Type | Tool and code | Line(s) | Description | Fix Approach |
|---|-------|------|---------------|---------|-------------|--------------|
| 1 | SQL injection | Security (Medium) | Bandit B608 | 9 | `addDue` built the INSERT with an f-string, so a flat name like `X'); DROP TABLE dues; --` becomes part of the SQL. | Use `?` placeholders and pass the values as a tuple, the same way `collect` already did. |
| 2 | Use of `eval` | Security (Medium) | Bandit B307, Pylint W0123 | 21 | `penalty` ran `eval(rule)`, so any Python in the rule string would run, for example `__import__("os").system(...)`. | Parse the rule with `ast.parse` and work it out in a small `calc` function that only allows numbers and `+ - * /`. Anything else raises `ValueError` and the fee is 0. Bandit's own hint, `ast.literal_eval`, does not accept `50 * 2`, so it would have broken the feature. |
| 3 | Hardcoded password | Security (Low) | Bandit B105 | 5 | `TREASURER_PASSWORD = "flat#101"` sits in plain text in the source and in git history. | Read it from the `TREASURER_PASSWORD` environment variable with `os.environ.get`. |
| 4 | Mutable default argument | Bug | Pylint W0102 | 8 | `history=[]` is created once and shared by every call, so each `addDue` kept adding to the same list. | Default to `None` and create a new list inside the function. |
| 5 | Too broad exception | Bug | Pylint W0718 | 22 | `except Exception` hid every error in `penalty`, including real bugs. | Catch only `SyntaxError`, `ValueError` and `ZeroDivisionError`, the errors a bad rule can actually cause. |
| 6 | Inconsistent return | Bug | Pylint R1710 | 12 to 16 | `collect` returned the amount on success and fell off the end (an implicit `None`) otherwise. | Return `None` explicitly. While fixing it I added `AND paid = 0` to the SELECT, because the same due could be collected twice (see row 12). |
| 7 | Comparison to None | Bug / Style | Pylint C0121, Flake8 E711 | 29 | `rows != None` is always true because `fetchall()` returns a list, never `None`. So the check did nothing. | Removed the check and return the list directly. One change cleared both tools. |
| 8 | Function name not snake_case | Convention | Pylint C0103 | 8 | `addDue` uses camelCase. | Renamed to `add_due` and updated both calls in `main`. |
| 9 | Missing docstrings | Convention | Pylint C0114, C0116 | 1, 8, 12, 19, 27, 34 | No module docstring and no function docstrings. | Added a module docstring and a one line docstring to every function. |
| 10 | Line too long | Style | Flake8 E501, Pylint C0301 | 4, 13, 15 | Lines of 87, 104 and 92 characters. Flake8's limit is 79, Pylint's is 100, so only line 13 failed both. | Split the long `execute` calls over several lines inside their brackets. |
| 11 | Missing blank lines | Style | Flake8 E302 | 12 | `def collect` came straight after `addDue` with no blank lines. | Added two blank lines between the functions. |
| 12 | Same due collected twice | Bug (no tool found this) | None | 12 to 16 | Calling `collect("A-101", "Oct")` twice returned 2500 both times, as if the flat paid twice. | Only select rows where `paid = 0`, so a second call returns `None`. |

Also changed, not reported by any tool: `main()` used to run at import time. It now sits under
`if __name__ == "__main__":`, so the module can be imported without running the demo.

## Results

| Tool | Before | After |
|------|--------|-------|
| Pylint | 5.81/10, 13 messages | 10.00/10 |
| Bandit | 3 issues (2 Medium, 1 Low) | No issues identified |
| Flake8 | 5 issues | 0 issues (empty report) |

The program still prints `2500`, `100` and `['A-102']`, the same as before the changes.
