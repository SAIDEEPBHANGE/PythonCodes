# ---------------------------------------------
# ✅ Python Variables: Rules and Best Practices
# ---------------------------------------------

# ➤ Rules for Python variable names:
# 1. Must begin with a letter (A-Z, a-z) or an underscore (_)
# 2. Cannot start with a number
# 3. Can only contain letters, numbers, and underscores
# 4. Case-sensitive (myVar, MyVar, MYVAR are all different)
# 5. Cannot use Python reserved keywords (like `class`, `def`, `if`, etc.)

# ✅ Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Uncomment the line below to see the output
print("Legal variable:", myVar)

# ❌ Illegal variable names (will cause SyntaxError if used):
# 2myvar = "John"      # Starts with a number
# my-var = "John"      # Contains a hyphen
# my var = "John"      # Contains a space

# ---------------------------------------------
# ✅ Assigning Multiple Variables
# ---------------------------------------------

# ➤ Assign multiple values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print("Multiple assignments:")
print(x)
print(y)
print(z)

# ➤ Assign the same value to multiple variables
x = y = z = "Orange"
print("\nSame value to multiple variables:")
print(x)
print(y)
print(z)

# ➤ Unpacking a collection (e.g., list or tuple)
fruits = ["apple", "banana", "cherry"]

try:
    x, y, z = fruits  # Make sure the number of variables matches number of elements
    print("\nUnpacked list values:")
    print(x)
    print(y)
    print(z)
except ValueError as e:
    print("Error unpacking list:", e)

# ---------------------------------------------
# ✅ Output Variables
# ---------------------------------------------

# ➤ Using print() to display variable values
x = "Python is awesome"
print("\nOutputting a single string variable:")
print(x)

# ➤ Printing multiple variables (comma separates values and supports mixed types)
x = "Python"
y = "is"
z = "awesome"
print("\nOutputting multiple variables with comma:")
print(x, y, z)

# ➤ Using + operator to concatenate strings
x = "Python "
y = "is "
z = "awesome"
print("\nConcatenating string variables with '+':")
print(x + y + z)

# ➤ + operator also works with numbers (as an arithmetic operator)
x = 5
y = 10
print("\nAdding numbers with '+':")
print(x + y)

# ➤ Mixing strings and numbers with '+' will cause an error
x = 5
y = "John"
print("\nMixing string and integer with comma (safe way):")
print(x, y)  # Correct way

# The line below will cause TypeError: Uncomment to test
# print(x + y)

# ---------------------------------------------
# ✅ Global vs Local Variables
# ---------------------------------------------

# ➤ Global variable (can be accessed anywhere in the file)
x = "awesome"

def myfunc():
    print("\nAccessing global variable inside a function:")
    print("Python is " + x)

myfunc()

# ➤ Local variable (defined inside function, shadows global variable)
x = "awesome"

def myfunc():
    x = "fantastic"  # Local to the function
    print("\nUsing local variable inside function:")
    print("Python is " + x)

myfunc()
print("Outside function, x is still:", x)

# ➤ Using `global` keyword to modify global variable inside function
def myfunc():
    global x
    x = "fantastic"  # This modifies the global variable

myfunc()
print("\nAfter using global keyword, x becomes:", x)

# Another example for clarity
x = "awesome"

def myfunc():
    global x
    x = "fantastic"  # Overrides global x

myfunc()
print("Global variable modified by function:", x)

# ---------------------------------------------
# ✅ Python Built-in Data Types
# ---------------------------------------------

# ➤ Python has the following standard data types:
# Text Type:         str
# Numeric Types:     int, float, complex
# Sequence Types:    list, tuple, range
# Mapping Type:      dict
# Set Types:         set, frozenset
# Boolean Type:      bool
# Binary Types:      bytes, bytearray, memoryview
# None Type:         NoneType

# ➤ Examples:
a = "Hello"            # str
b = 10                 # int
c = 3.14               # float
d = [1, 2, 3]          # list
e = (1, 2, 3)          # tuple
f = {"a": 1, "b": 2}   # dict
g = {1, 2, 3}          # set
h = True               # bool
i = None               # NoneType

print("\nExamples of different data types:")
print(type(a), type(b), type(c), type(d))
print(type(e), type(f), type(g), type(h), type(i))
