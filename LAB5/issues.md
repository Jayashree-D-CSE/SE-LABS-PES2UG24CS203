# Lab 5: Static Code Analysis — Issues

## Overview

The original `pet_shelter.py` was analyzed using Pylint, Bandit, and Flake8 before any changes were made. The tools identified potential security weaknesses, a possible programming bug, exception-handling problems, naming and documentation issues, and style violations.

The issues below refer to the **original version** of `pet_shelter.py`. The cleaned version was then analyzed again to verify the fixes.

## Issue Table

| Issue | Type | Line(s) in original file | Description | Fix Approach |
|---|---|---:|---|---|
| Possible SQL injection (Bandit B608) | Security — Medium severity | 10 | The `INSERT` statement was built with string formatting. If values contain specially crafted input, the resulting SQL statement could be altered. | Replaced string formatting with a parameterized SQLite query using `?` placeholders and a tuple of values. |
| Mutable default argument (Pylint W0102) | Potential bug | 9 | `tags=[]` creates a list that can be reused across calls, so tags may unintentionally carry over between registrations. | Changed the default to `None` and created a new list inside the function when no tags are supplied. |
| Bare exception (Pylint W0702; Flake8 E722) | Error handling / style | 29 | A bare `except:` catches all exceptions, including exceptions that should not necessarily be suppressed. | Replaced the bare handler with handling for `sqlite3.Error`; also handled the case where the query returns no row. |
| Silently ignored exception (Bandit B110) | Error handling | 36–37 | `except Exception: pass` suppresses errors without providing information that the database operation failed. | Replaced broad, silent exception handling with `except sqlite3.Error as error` and an error message. |
| Random generator not intended for security-sensitive values (Bandit B311) | Security — Low severity | 22 | `random.randint()` is not designed for security-sensitive unpredictable values. | Replaced it with `secrets.randbelow()` for generating the adoption code. |
| Function names not in snake_case (Pylint C0103) | Code quality / naming | 9, 21, 25, 33, 40 | Names such as `registerPet`, `adoptionCode`, and `oldestAvailable` use camelCase instead of the conventional Python snake_case style. | Renamed functions to `register_pet`, `adoption_code`, `oldest_available`, `clear_unadopted`, and `shelter_status`, and updated their callers. |
| Missing module and function docstrings (Pylint C0114/C0116) | Documentation / maintainability | 1, 9, 15, 21, 25, 33, 40, 45 | The module and functions did not explain their purpose. | Added a module docstring and concise docstrings for the functions. |
| Long lines (Pylint C0301; Flake8 E501) | Style / readability | 5, 10, 27 | Some source lines exceeded the configured line-length limits. | Broke SQL statements and expressions across multiple lines for readability. |
| Multiple statements on one line (Pylint C0321; Flake8 E701) | Style / readability | 41 | The conditional and its return statement were written on the same line. | Placed the conditional body on separate lines. |
| Global statement (Pylint W0603) | Maintainability | 16 | `adopt()` modified `adoption_count` using a global variable, making state management less explicit. | Changed `adopt()` to accept the count as an argument and return the updated count; `main()` now owns the count. |
| String formatting that could use an f-string (Pylint C0209) | Readability / style | 10 | The original query used `%` string formatting. | Removed query string interpolation entirely by using parameterized SQL. |
| Missing or weak handling of an empty query result | Potential runtime bug | 27–30 | If there were no available pets, `fetchone()` could return `None`, and accessing `row[0]` would fail. | Added a check that returns `None` when no row is found. |

## Verification After Fixes

The cleaned program was run again and displayed output in the expected format, for example:

`Kiwi PET-2919 active`

The adoption code varies between runs.

The three analysis tools were rerun on the cleaned file, with these results:

- **Pylint:** 10.00/10 (original score: 3.95/10).
- **Bandit:** No issues identified.
- **Flake8:** No violations reported.

## Conclusion

The changes addressed the identified SQL construction risk, mutable default argument, exception-handling problems, random-code generation finding, naming issues, missing documentation, and style violations. The demonstration continued to run successfully after the changes. The final analysis results show that the cleaned file meets the lab's target Pylint score and has no findings reported by Bandit or Flake8 in this run.
