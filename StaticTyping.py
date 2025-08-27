"""
Python Code Formatting Tools:
- black
- yapf
- ruff

These tools help keep your code clean, readable, and consistent across your team.
"""

# ------------------------------------------
# 1. BLACK (The Uncompromising Code Formatter)
# ------------------------------------------

"""
Install:
    pip install black

Usage:
    black your_script.py

Key features:
- Opinionated formatting (you can't configure style much)
- Focuses on consistency and eliminating debates about style
- Auto-sorts imports with --preview

Example before formatting:
"""

# def some_function(x:int,y:int=10)->int: return x+y

# After running `black`:
def some_function(x: int, y: int = 10) -> int:
    return x + y

"""
You can also format entire projects:
    black .

Optional flags:
    --check      : Check if formatting is needed (CI use)
    --diff       : Show diff without changing files
    --line-length 88 (default) or customize
"""


# ------------------------------------------
# 2. YAPF (Yet Another Python Formatter)
# ------------------------------------------

"""
Install:
    pip install yapf

Usage:
    yapf -i your_script.py  # -i means edit in-place

Key Features:
- Style can be customized (unlike black)
- Google-style and PEP8-style out of the box

Example:
    yapf --style google -i script.py
    yapf --style pep8 -i script.py

You can create a .style.yapf file for config:
    [style]
    based_on_style = google
    indent_width = 4
"""

# Example before formatting (unformatted):
def messy_code(a,b):return[a*b for a in range(1,10)]

# After yapf with Google style:
def messy_code(a, b):
    return [a * b for a in range(1, 10)]


# ------------------------------------------
# 3. RUFF (Fast Python Linter and Formatter)
# ------------------------------------------

"""
Install:
    pip install ruff

Usage:
    ruff format your_script.py     # for formatting
    ruff check your_script.py      # for linting

Why Ruff?
- Extremely fast (written in Rust)
- Can do formatting, linting, fix common issues
- Replaces: flake8, isort, black, pylint, etc.

Supports configs:
    pyproject.toml:
        [tool.ruff]
        line-length = 88
        exclude = ["migrations"]

        [tool.ruff.format]
        quote-style = "double"
        indent-style = "space"
"""

# Example bad code:
def ruff_example():
    print(  "Hello Ruff!" )

# Ruff will reformat to:
def ruff_example():
    print("Hello Ruff!")


# ------------------------------------------
# SUMMARY
# ------------------------------------------

"""
black   -> Zero-config, opinionated, consistent formatting
yapf    -> Customizable code formatter (Google/PEP8 styles)
ruff    -> Fast linter + formatter (supports rules, checks, auto-fixes)

Best practice:
- Use one formatter (black or ruff) for consistency
- Use pre-commit hooks to auto-format before commits
- Use `ruff` if you also want linting and speed
"""
