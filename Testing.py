"""
Python Testing Tools:
- unittest / pyUnit (built-in)
- doctest (built-in)
- pytest (popular 3rd-party)
- nose (legacy)
- tox (test automation/envs)

This script includes example tests and how to run them.
"""

# ------------------------------------------
# 1. CODE TO BE TESTED
# ------------------------------------------

def add(a: int, b: int) -> int:
    """
    Adds two integers.

    >>> add(2, 3)
    5

    >>> add(-1, 1)
    0
    """
    return a + b

def divide(a: float, b: float) -> float:
    """
    Divides a by b.

    Raises:
        ZeroDivisionError: if b is 0
    """
    return a / b


# ------------------------------------------
# 2. UNITTEST (pyUnit) — Built-in
# ------------------------------------------

import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

"""
Run with:
    python -m unittest test_script.py
    # OR discover all tests
    python -m unittest discover
"""

# ------------------------------------------
# 3. DOCTEST — Built-in
# ------------------------------------------

import doctest

def run_doctests():
    """
    Will test all >>> examples inside function docstrings.
    """
    doctest.testmod()

"""
Run with:
    python -m doctest -v test_script.py
Or call run_doctests() in __main__
"""

# ------------------------------------------
# 4. PYTEST — Most popular 3rd-party framework
# ------------------------------------------

"""
Install:
    pip install pytest

Pytest automatically discovers tests that start with "test_"

Features:
- Better output
- Simple syntax (no classes needed)
- Fixtures
- Parametrization
"""

# Example pytest function (place in test_something.py)

def test_add_pytest():
    assert add(2, 3) == 5

def test_divide_pytest():
    assert divide(10, 5) == 2

def test_divide_zero_pytest():
    import pytest
    with pytest.raises(ZeroDivisionError):
        divide(3, 0)

"""
Run with:
    pytest
    pytest -v           # verbose
    pytest --maxfail=1  # stop on first failure
"""

# ------------------------------------------
# 5. NOSE (Legacy)
# ------------------------------------------

"""
Install:
    pip install nose

Run:
    nosetests

Nose is similar to unittest, and was used widely before pytest took over.
Note: Nose is no longer actively maintained.
"""

# ------------------------------------------
# 6. TOX — Environment & Test Automation
# ------------------------------------------

"""
Install:
    pip install tox

tox runs your tests in isolated virtualenvs.
Useful for:
- Testing against multiple Python versions
- Linting, type checking, etc.

Steps:
1. Create tox.ini file in your project root:

[tox]
envlist = py38, py39

[testenv]
deps = pytest
commands = pytest

2. Run tox:
    tox

3. It will:
- Create venvs
- Install deps
- Run commands

Great for CI (GitHub Actions, GitLab, etc.)
"""

# ------------------------------------------
# 7. SUMMARY
# ------------------------------------------

"""
✅ unittest   -> Built-in, xUnit style, class-based
✅ doctest    -> Test in docstrings (great for docs & quick tests)
✅ pytest     -> Modern, powerful, popular
✅ nose       -> Legacy, not recommended for new projects
✅ tox        -> Automate tests in multiple envs, great for CI

Best practice:
- Use `pytest` for writing tests
- Use `tox` for running tests across Python versions
- Use `doctest` for simple function-level examples in docs
"""

# ------------------------------------------
# 8. OPTIONAL: RUN DOCTESTS ON FILE EXECUTION
# ------------------------------------------

if __name__ == "__main__":
    run_doctests()
    unittest.main()  # comment this out if running with pytest/tox
