# ---------------------------------------------
# ✅ What is a Module?
# ---------------------------------------------
# A module is a file containing Python code (functions, variables, classes) that can be imported and used in other Python files.
# Modules help organize code into reusable components.

# Python comes with many built-in modules (standard library),
# and you can also create your own custom modules.

# ---------------------------------------------
# ✅ Using Built-in Modules
# ---------------------------------------------

# Example 1: Importing the math module (built-in)
import math

print("Pi:", math.pi)
print("Square root of 16:", math.sqrt(16))

# You can import specific functions only:
from math import factorial, pow

print("Factorial of 5:", factorial(5))
print("2 raised to 3:", pow(2, 3))

# Using alias for modules or functions
import math as m
print("Cosine of 0:", m.cos(0))

from math import sqrt as square_root
print("Square root of 25:", square_root(25))

# ---------------------------------------------
# ✅ Using the random Module (Built-in)
# ---------------------------------------------
import random

print("Random integer between 1 and 10:", random.randint(1, 10))
print("Random choice from list:", random.choice(['apple', 'banana', 'cherry']))

# ---------------------------------------------
# ✅ Creating and Using Custom Modules
# ---------------------------------------------

# Step 1: Create a Python file named my_module.py with the following code:
# ----------------------------------------
# # my_module.py
# def greet(name):
#     return f"Hello, {name}!"
#
# pi = 3.14159
# ----------------------------------------

# Step 2: In your main script, import and use the custom module

import my_module  # make sure my_module.py is in the same folder or Python path

print(my_module.greet("Saideep"))
print("Value of pi from my_module:", my_module.pi)

# You can also import specific items from your custom module
from my_module import greet

print(greet("Alice"))

# ---------------------------------------------
# ✅ Reloading Modules (useful during development)
# ---------------------------------------------
import importlib

# If you modify my_module.py after import, reload it to get updates
importlib.reload(my_module)

# ---------------------------------------------
# ✅ Module Search Path
# ---------------------------------------------
import sys

print("Module search paths:")
for path in sys.path:
    print(path)

# You can add directories to sys.path to import modules from other locations:
# sys.path.append('/path/to/your/modules')

# ---------------------------------------------
# ✅ __name__ and __main__ in Modules
# ---------------------------------------------
# Every Python file has a built-in variable __name__
# When a file is run directly, __name__ is "__main__"
# When imported as a module, __name__ is the module's name

# Example usage in my_module.py:
# ----------------------------------------
# if __name__ == "__main__":
#     print("This runs only when my_module.py is executed directly")
# ----------------------------------------

# ---------------------------------------------
# ✅ Summary
# ---------------------------------------------
# - Modules are reusable Python files
# - Use import to bring in modules (built-in or custom)
# - Use from module import item to import specific functions or variables
# - Use aliases with 'as' for convenience
# - Custom modules must be in your script's folder or Python path
# - Use __name__ == "__main__" to separate script and module behavior
