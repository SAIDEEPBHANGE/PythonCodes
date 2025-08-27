# Auther : Saideep Bhange
# Modern Python Developer Roadmap — README

This repository is your guided path to becoming a modern Python developer and building a comprehensive capstone project that ties everything together.

> Source inspiration: Python Developer Roadmap (roadmap.sh) PDF uploaded alongside this repo.

## 🎯 Goals
- Master Python fundamentals and data structures
- Get comfortable with packaging, environments, typing, documentation, formatting, and testing
- Learn synchronous & asynchronous web frameworks
- Understand concurrency (threads, processes, async)
- Build, package, document, and test a production-grade project

## 📚 Curriculum Outline
Below is the study plan derived from the roadmap PDF and organized into weekly sprints. Each section links to tasks and exercises in `/exercises` and milestones in the capstone project.

### 1) Learn the Basics
- Basic syntax, variables & data types
- Conditionals, type casting, exceptions
- Functions (incl. builtins), lambdas, decorators, iterators
- Comprehensions & generator expressions
- Regular expressions
- Modules & packages

### 2) Data Structures & Algorithms
- Lists, tuples, sets, dicts
- Arrays & linked lists
- Stacks, queues, heaps
- Hash tables
- Binary search tree
- Recursion & sorting algorithms

### 3) Object-Oriented Programming
- Classes, instances, methods (incl. dunder methods)
- Inheritance & composition
- Context managers

### 4) Package Managers & Environments
- pip / PyPI, pipx
- Poetry or pip-tools
- Conda (optional)
- virtualenv, pyenv
- `pyproject.toml` and build backends
- Pipenv (optional)

### 5) Static Typing
- `typing` module
- mypy / pyright / pyre
- Pydantic for data validation

### 6) Code Quality
- Formatters: black, yapf
- Linters: ruff
- Docstrings & documentation generators: Sphinx / MkDocs
- Pre-commit hooks
- tox / nox for matrix testing

### 7) Testing
- unittest / pyUnit
- pytest
- doctest (optional)

### 8) Concurrency & Asynchrony
- GIL & when it matters
- Threading, multiprocessing
- Asynchronous programming (`asyncio`), event loops
- uvicorn (ASGI server)

### 9) Learn a Framework
- Sync: Flask / Django / Pyramid
- Async: FastAPI / aiohttp / Sanic / Tornado
- Dash / Plotly for data apps

### 10) DevOps Foundations
- Packaging & publishing to PyPI (testpypi first)
- Docker basics
- CI/CD (GitHub Actions)
- Versioning & releases

---

## 🏗 Capstone Project: **DataHub 360**

A production-grade **data-driven web service** with:
- **FastAPI** backend (ASGI) + async I/O
- **Celery / RQ** (or `asyncio` tasks) for background jobs
- **PostgreSQL** (SQLModel/SQLAlchemy) + Redis
- **Pydantic** models with strict typing
- **pytest** + coverage + property-based tests
- **black** + **ruff** + pre-commit
- **Sphinx** docs published to GitHub Pages
- **Docker** containers and GitHub Actions CI
- Optional **Dash** micro-UI for analytics

### Core Features
1. Ingest CSV/JSON datasets via API (async file upload and validation)
2. Store datasets and metadata in Postgres
3. Run async analysis jobs (descriptive stats, profiling)
4. Expose results via REST endpoints
5. Serve live charts via a small Dash app or a static frontend
6. Role-based users & tokens (FastAPI dependencies)
7. Background scheduled cleanups
8. Health checks and metrics endpoint

### Tech Mapping (Roadmap ➜ Feature)
- **Basics/OOP** → project structure, modules, dunder methods
- **DS&A** → efficient parsing, queues/priority jobs
- **Typing/Pydantic** → strict data validation
- **Async/Concurrency** → async endpoints & workers
- **Framework** → FastAPI + uvicorn
- **Testing** → pytest unit/integration tests
- **Quality** → black, ruff, pre-commit
- **Docs** → Sphinx + autodoc
- **DevOps** → Dockerfile, compose, GitHub Actions