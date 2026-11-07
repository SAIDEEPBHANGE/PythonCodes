# Python Development Tools

These examples and reference notes cover development environments, package management, typing, documentation, and testing. Python 3 is sufficient for the standard-library examples; third-party tools mentioned in the notes must be installed separately before using them.

- [Environments](Environments.py)
- [Package managers](package_managers.py)
- [Python concepts and context managers](common_packages_examples.py)
- [Typing and code quality notes](StaticTyping.py)
- [Sphinx documentation notes](Sphinx.py)
- [Testing examples](Testing.py)

From the repository root, run the built-in unit tests and doctests with:

```bash
python -m unittest development_tools.Testing
python -m doctest development_tools/Testing.py
```

The context-manager example writes `example.txt` in the current working directory. Several files are primarily reference notes, so read them before running them or installing optional tools.

[Back to the learning path](../README.md#learning-path)