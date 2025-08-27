# ---------------------------------------------
# ✅ What is a Lambda Function?
# ---------------------------------------------
# A lambda function is an anonymous (unnamed) small function defined with the keyword 'lambda'.
# It can have any number of arguments but only one expression.
# Lambda functions are useful for short, throwaway functions.

# Syntax:
# lambda arguments: expression

# ---------------------------------------------
# ✅ Basic Lambda Example
# ---------------------------------------------
add = lambda x, y: x + y  # Function to add two numbers
print("Sum:", add(5, 3))  # Output: 8

# Equivalent regular function:
def add_func(x, y):
    return x + y

print("Sum with regular function:", add_func(5, 3))

# ---------------------------------------------
# ✅ Lambda with No Arguments
# ---------------------------------------------
greet = lambda: "Hello, World!"
print(greet())  # Output: Hello, World!

# ---------------------------------------------
# ✅ Using Lambda with map()
# ---------------------------------------------
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared:", squared)  # Output: [1, 4, 9, 16]

# ---------------------------------------------
# ✅ Using Lambda with filter()
# ---------------------------------------------
# Filter even numbers from a list
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)  # Output: [2, 4]

# ---------------------------------------------
# ✅ Using Lambda with sorted()
# ---------------------------------------------
# Sort a list of tuples by the second item
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("Sorted pairs by second item:", sorted_pairs)

# ---------------------------------------------
# ✅ Lambda as a Return Value (Closures)
# ---------------------------------------------
def make_multiplier(n):
    return lambda x: x * n

times3 = make_multiplier(3)
print("3 times 7:", times3(7))  # Output: 21

times5 = make_multiplier(5)
print("5 times 7:", times5(7))  # Output: 35

# ---------------------------------------------
# ✅ Limitations of Lambda Functions
# ---------------------------------------------
# - Only a single expression (no statements or multiple expressions)
# - No annotations or docstrings
# - Should be used for simple functions, else define a regular function

# ---------------------------------------------
# ✅ When to Use Lambda Functions?
# ---------------------------------------------
# ✔ Short, simple functions
# ✔ Inline functions for functions like map(), filter(), sorted()
# ✔ Passing functions as arguments

# ---------------------------------------------
# ✅ Summary
# ---------------------------------------------
# - Lambda functions are anonymous, one-expression functions
# - Use lambda args: expression syntax
# - Ideal for quick functions without needing a full function definition
# - Widely used with built-in functions like map, filter, and sorted
