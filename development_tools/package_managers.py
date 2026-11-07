"""
==============================================
Package Managers in Python: PyPI, pip, conda, Poetry, and uvicorn
==============================================

Package managers help you install, manage, and maintain third-party packages or dependencies for your Python projects.

"""

# ----------------------------------------------
# 1. PyPI (Python Package Index)
# ----------------------------------------------
# PyPI is the official repository of Python packages.
# It hosts thousands of packages that you can install using pip or other tools.
#
# Website: https://pypi.org/
#
# Example: You can search for packages here, e.g., 'requests', 'numpy', 'flask'.

# ----------------------------------------------
# 2. pip (Python Package Installer)
# ----------------------------------------------
# pip is the default package manager for Python.
# It installs packages from PyPI.
#
# Common commands:
#
# Install a package:
# > pip install requests
#
# Install a specific version:
# > pip install requests==2.25.1
#
# Upgrade a package:
# > pip install --upgrade requests
#
# List installed packages:
# > pip list
#
# Uninstall a package:
# > pip uninstall requests
#
# You can also install from requirements.txt:
# > pip install -r requirements.txt

# ----------------------------------------------
# 3. conda (Anaconda/Miniconda Package Manager)
# ----------------------------------------------
# conda is a package manager popular in data science and machine learning.
# It manages packages and environments for Python and other languages.
#
# Conda repositories host many scientific packages optimized for performance.
#
# Common commands:
#
# Create environment:
# > conda create -n myenv python=3.9
#
# Activate environment:
# > conda activate myenv
#
# Install package:
# > conda install numpy
#
# List environments:
# > conda env list
#
# Remove environment:
# > conda remove -n myenv --all

# ----------------------------------------------
# 4. Poetry (Python Dependency Management and Packaging)
# ----------------------------------------------
# Poetry is a modern tool for dependency management and packaging.
# It simplifies managing project dependencies and packaging your project for distribution.
#
# It uses a pyproject.toml file to track dependencies.
#
# Common commands:
#
# Create a new project:
# > poetry new myproject
#
# Add a dependency:
# > poetry add requests
#
# Install dependencies:
# > poetry install
#
# Run a command inside the poetry environment:
# > poetry run python script.py
#
# Export dependencies to requirements.txt:
# > poetry export -f requirements.txt --output requirements.txt

# ----------------------------------------------
# 5. uvicorn (ASGI Server for Async Python Web Apps)
# ----------------------------------------------
# uvicorn is NOT a package manager, but a fast ASGI server used to run async web frameworks like FastAPI and Starlette.
# It's often installed via pip and used to serve your Python async web applications.
#
# Example install:
# > pip install uvicorn
#
# Run a FastAPI app (assumes you have app.py with FastAPI instance called 'app'):
# > uvicorn app:app --reload
#
# The --reload flag auto-restarts the server on code changes (useful in development).

# ----------------------------------------------
# Example: Using pip inside Python (not common, but possible)
# ----------------------------------------------
import subprocess
import sys

def install_package(package_name):
    """
    Programmatically install a package using pip.
    """
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# Example: install requests package programmatically (use with caution)
# install_package("requests")

# ----------------------------------------------
# Summary:
# ----------------------------------------------
# - PyPI is the central repository of Python packages.
# - pip installs packages from PyPI, the default package manager.
# - conda manages packages and environments, popular in data science.
# - Poetry manages dependencies and packaging with modern features.
# - uvicorn is an ASGI server, not a package manager, used to run async apps.
"""
print("Check the comments for detailed explanations on Package Managers!")
"""
