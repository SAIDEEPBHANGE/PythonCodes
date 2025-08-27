"""
Sphinx Documentation in Python Projects
---------------------------------------

Sphinx is a powerful tool that converts reStructuredText (and docstrings)
into HTML, PDF, and other readable documentation formats.

Sphinx uses:
- `.rst` or `.md` files
- Python docstrings
- Themes (e.g., Read the Docs)
"""

# ------------------------------------------
# 1. INSTALL & SETUP
# ------------------------------------------

"""
Install Sphinx:
    pip install sphinx

Create a docs folder and initialize:
    sphinx-quickstart docs

Answer setup prompts:
    > Project name, author, version, etc.
    > Separate source/build dirs [y]

Inside `docs/conf.py`, configure:
    - Add extensions like 'sphinx.ext.autodoc', 'sphinx.ext.napoleon'
    - Set project and version
    - Set paths (sys.path.append) to include your code
"""

# ------------------------------------------
# 2. EXAMPLE MODULE WITH DOCSTRINGS
# ------------------------------------------

def multiply(a: int, b: int) -> int:
    """
    Multiply two integers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The result of a * b.
    """
    return a * b


class Calculator:
    """
    A simple calculator class.

    Attributes:
        memory (int): Stores the last calculated result.
    """

    def __init__(self):
        """
        Initializes the calculator with memory set to zero.
        """
        self.memory = 0

    def add(self, x: int, y: int) -> int:
        """
        Add two integers and store in memory.

        :param x: First number
        :param y: Second number
        :return: The sum
        """
        self.memory = x + y
        return self.memory

# ------------------------------------------
# 3. ENABLE AUTODOC & NAPOLEON IN conf.py
# ------------------------------------------

"""
In docs/conf.py:

extensions = [
    'sphinx.ext.autodoc',      # Pulls in docstrings
    'sphinx.ext.napoleon',     # Supports Google/NumPy-style docstrings
]

# Include source directory:
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))  # Adjust as needed
"""

# ------------------------------------------
# 4. ADD AUTOMODULE DIRECTIVE IN index.rst
# ------------------------------------------

"""
Inside docs/index.rst or a separate .rst file (e.g., api.rst):

.. automodule:: your_module_name
    :members:
    :undoc-members:
    :show-inheritance:

Then build docs:
    cd docs
    make html        # On Unix/macOS
    .\make.bat html  # On Windows

Output will be in: docs/_build/html/index.html
"""

# ------------------------------------------
# 5. SPHINX + MARKDOWN (Optional)
# ------------------------------------------

"""
To use Markdown instead of .rst files:
    pip install myst-parser

In conf.py:
    extensions.append('myst_parser')
    source_suffix = ['.rst', '.md']
"""

# ------------------------------------------
# 6. SUMMARY
# ------------------------------------------

"""
Sphinx Steps Recap:
1. pip install sphinx
2. sphinx-quickstart docs/
3. Edit conf.py (enable autodoc, napoleon, set path)
4. Add docstrings to your code (Google or reST style)
5. Create .rst files and use automodule directive
6. Run `make html` to generate documentation

Bonus:
- Use Read the Docs theme: `pip install sphinx-rtd-theme`
- Host your docs on https://readthedocs.io

Best practice:
- Use Google-style docstrings with Napoleon
- Keep docstrings clean and concise
- Automate doc builds via CI if needed
"""
 