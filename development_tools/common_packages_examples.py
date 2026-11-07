# -----------------------------------------------
# pyproject.toml Configuration
# -----------------------------------------------
# 'pyproject.toml' is a configuration file used to specify build system requirements and tool configurations 
# for Python projects. It's used by tools like poetry, flit, black, isort, etc.

# Example (This would go inside pyproject.toml, not Python code):
# [tool.black]
# line-length = 88

# Since pyproject.toml is not executable Python, we don’t write it here directly.

# -----------------------------------------------
# List Comprehensions
# -----------------------------------------------
# List comprehensions provide a concise way to create lists in a single line of code.

squares = [x ** 2 for x in range(10)]  # [0, 1, 4, 9, ..., 81]
print("Squares:", squares)

# Filtering with condition
evens = [x for x in range(20) if x % 2 == 0]
print("Even numbers:", evens)

# -----------------------------------------------
# Generator Expressions
# -----------------------------------------------
# Generator expressions are similar to list comprehensions but use () and generate items lazily (one at a time).

square_gen = (x ** 2 for x in range(5))
print("Generated squares:", list(square_gen))  # Convert to list to print all values

# Generator expressions are memory efficient for large data.

# -----------------------------------------------
# Paradigms
# -----------------------------------------------
# Python supports multiple programming paradigms:
# 1. Procedural Programming
# 2. Object-Oriented Programming (OOP)
# 3. Functional Programming

# Example of OOP:
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

dog = Dog()
print("Dog says:", dog.speak())

# Example of Functional Programming:
def square(x):
    return x * x

print("Map result:", list(map(square, [1, 2, 3, 4])))

# -----------------------------------------------
# Context Manager
# -----------------------------------------------
# Context managers handle setup and teardown actions using the 'with' statement.

# File I/O example
with open('example.txt', 'w') as file:
    file.write("This file was written using a context manager.\n")

# Custom context manager using 'contextlib'
from contextlib import contextmanager

@contextmanager
def open_resource(name):
    print(f"Opening resource: {name}")
    yield f"Resource: {name}"
    print(f"Closing resource: {name}")

with open_resource("my_resource") as res:
    print("Using", res)
