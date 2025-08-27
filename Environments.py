"""
Python Environments & Dependency Management:
- virtualenv
- pipenv
- pyenv
- environments overview

These tools are primarily used in the terminal, but here’s a Pythonic explanation with CLI commands shown as comments.
"""

# ------------------------------------------
# 1. PYTHON ENVIRONMENTS OVERVIEW
# ------------------------------------------

"""
A Python environment is an isolated workspace where you can install dependencies 
without affecting the global Python installation.

Why use environments?
- Different projects need different packages or versions.
- Avoid version conflicts.
- Keep your system Python clean.
"""

# ------------------------------------------
# 2. VIRTUALENV
# ------------------------------------------

"""
virtualenv creates isolated Python environments.

Install it globally:
    pip install virtualenv

Create a new environment:
    virtualenv venv

Activate environment:
    On Windows: .\venv\Scripts\activate
    On Mac/Linux: source venv/bin/activate

Install packages:
    pip install requests

Freeze dependencies to a file:
    pip freeze > requirements.txt

Reinstall from requirements:
    pip install -r requirements.txt

Deactivate environment:
    deactivate
"""

# Example (non-executable in script, run in terminal):
# virtualenv myenv
# source myenv/bin/activate
# pip install numpy
# deactivate

# ------------------------------------------
# 3. PIPENV
# ------------------------------------------

"""
Pipenv combines pip and virtualenv in one tool.
It creates a virtual environment and manages dependencies using Pipfile & Pipfile.lock.

Install pipenv:
    pip install pipenv

Create env and install package:
    pipenv install requests

Activate shell in env:
    pipenv shell

Run script in env without activating:
    pipenv run python script.py

Uninstall a package:
    pipenv uninstall requests

Pipenv automatically creates:
    - Pipfile: lists your packages
    - Pipfile.lock: locks specific versions for reproducibility
"""

# Example (CLI, not Python code):
# pipenv install flask
# pipenv shell
# pipenv run python app.py

# ------------------------------------------
# 4. PYENV
# ------------------------------------------

"""
pyenv manages multiple Python versions on your system.

Why use it?
- Different projects may need Python 3.6, 3.10, etc.
- Your OS might not allow changing the system Python.

Install pyenv (Unix/macOS example using curl):
    curl https://pyenv.run | bash

Install a Python version:
    pyenv install 3.10.5

Set Python version globally:
    pyenv global 3.10.5

Set Python version for a folder/project:
    pyenv local 3.9.7

Check Python version in use:
    pyenv which python

pyenv is often used with virtualenv:
    pyenv virtualenv 3.10.5 myproject-env
    pyenv activate myproject-env
"""

# Example usage in terminal:
# pyenv install 3.8.12
# pyenv virtualenv 3.8.12 project-env
# pyenv local project-env

# ------------------------------------------
# SUMMARY
# ------------------------------------------

"""
virtualenv  -> Create isolated envs manually.
pipenv      -> Modern tool combining pip + virtualenv + Pipfile.
pyenv       -> Manage multiple Python versions on your system.

Best practice:
- Use pyenv to manage Python versions.
- Use virtualenv or pipenv for project isolation.
- Always keep dependencies tracked (requirements.txt or Pipfile).
"""
