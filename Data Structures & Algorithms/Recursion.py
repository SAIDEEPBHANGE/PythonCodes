# ==============================================
# Recursion in Python - Explained with Examples
# ==============================================

# ----------------------------------------------
# What is Recursion?
# ----------------------------------------------
# Recursion is a programming technique where a function calls itself.
# The recursive function solves a problem by breaking it down into smaller sub-problems.
#
# Key parts of recursion:
# 1. Base Case: Condition to stop recursion (prevents infinite loops).
# 2. Recursive Case: Function calls itself with a smaller/simpler input.

# ----------------------------------------------
# Example 1: Factorial using recursion
# ----------------------------------------------
def factorial(n):
    """
    Calculate the factorial of n (n!)
    factorial(n) = n * factorial(n-1)
    Base case: factorial(0) = 1
    """
    if n == 0:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive call

print("Factorial of 5:", factorial(5))  # Output: 120

# ----------------------------------------------
# Example 2: Fibonacci sequence using recursion
# ----------------------------------------------
def fibonacci(n):
    """
    Return the nth Fibonacci number.
    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...
    Base cases: fibonacci(0) = 0, fibonacci(1) = 1
    Recursive case: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    """
    if n == 0:
        return 0  # Base case
    elif n == 1:
        return 1  # Base case
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # Recursive call

print("Fibonacci number at position 7:", fibonacci(7))  # Output: 13

# ----------------------------------------------
# Example 3: Sum of elements in a list using recursion
# ----------------------------------------------
def sum_list(lst):
    """
    Recursively calculate the sum of elements in a list.
    Base case: empty list returns 0
    Recursive case: sum of first element + sum of rest of list
    """
    if not lst:
        return 0  # Base case
    else:
        return lst[0] + sum_list(lst[1:])  # Recursive call

print("Sum of [1, 2, 3, 4, 5]:", sum_list([1, 2, 3, 4, 5]))  # Output: 15

# ----------------------------------------------
# Example 4: Recursive function to reverse a string
# ----------------------------------------------
def reverse_string(s):
    """
    Reverse a string using recursion.
    Base case: empty string or single character returns itself
    Recursive case: last character + reverse of rest of string
    """
    if len(s) <= 1:
        return s  # Base case
    else:
        return s[-1] + reverse_string(s[:-1])  # Recursive call

print("Reverse of 'hello':", reverse_string("hello"))  # Output: 'olleh'

# ----------------------------------------------
# Example 5: Recursive traversal of a nested list
# ----------------------------------------------
def flatten_list(nested_list):
    """
    Flatten a nested list into a single list using recursion.
    Example: [1, [2, 3], [4, [5, 6]]] => [1, 2, 3, 4, 5, 6]
    """
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            # Recursive call to flatten sublist
            flat_list.extend(flatten_list(element))
        else:
            flat_list.append(element)
    return flat_list

nested = [1, [2, 3], [4, [5, 6]], 7]
print("Flattened list:", flatten_list(nested))  # Output: [1, 2, 3, 4, 5, 6, 7]

# ----------------------------------------------
# Important notes on recursion:
# ----------------------------------------------
# - Always have a base case, or the recursion will run infinitely and cause a stack overflow.
# - Recursive functions use the call stack, so deep recursion can lead to performance issues.
# - Sometimes iteration is more efficient, but recursion can simplify code and is essential for some algorithms (like tree traversals).

# ----------------------------------------------
# Example 6: Recursion with a depth limit (to avoid infinite recursion)
# ----------------------------------------------
import sys

def safe_factorial(n, depth=0, max_depth=1000):
    """
    Factorial with depth check to avoid infinite recursion.
    """
    if depth > max_depth:
        raise RecursionError("Maximum recursion depth reached")
    if n == 0:
        return 1
    else:
        return n * safe_factorial(n - 1, depth + 1, max_depth)

print("Safe factorial of 5:", safe_factorial(5))

# ----------------------------------------------
# Summary:
# ----------------------------------------------
# Recursion is a powerful technique for problems that can be divided into smaller similar sub-problems.
# Key to recursion:
# - Base case to stop recursion
# - Recursive case that breaks problem down and calls itself
# Use recursion for tree traversals, divide and conquer algorithms, and problems naturally defined recursively.

