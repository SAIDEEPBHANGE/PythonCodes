# ---------------------------------------------
# ✅ What is a Function?
# ---------------------------------------------
# A function is a block of reusable code that performs a specific task.
# It helps make programs modular and easier to maintain.

# ---------------------------------------------
# ✅ Defining and Calling a Function
# ---------------------------------------------

# Define a function using 'def' keyword
def greet():
    print("Hello from a function!")

# Call the function
greet()

# ---------------------------------------------
# ✅ Function with Parameters
# ---------------------------------------------
def greet_user(name):
    print("Hello", name)

greet_user("Alice")  # Pass argument

# ---------------------------------------------
# ✅ Function with Return Value
# ---------------------------------------------
def add(a, b):
    return a + b

result = add(5, 3)
print("Addition result:", result)

# ---------------------------------------------
# ✅ Function with Default Arguments
# ---------------------------------------------
def greet_user(name="Guest"):
    print("Hello", name)

greet_user()        # Uses default value
greet_user("Bob")   # Overrides default

# ---------------------------------------------
# ✅ Keyword Arguments
# ---------------------------------------------
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info(age=20, name="John")  # Order doesn't matter with keywords

# ---------------------------------------------
# ✅ Variable-Length Arguments (*args and **kwargs)
# ---------------------------------------------

# *args: Allows any number of positional arguments
def total_marks(*marks):
    print("Marks received:", marks)
    print("Total:", sum(marks))

total_marks(70, 85, 90)

# **kwargs: Allows any number of keyword arguments
def student_details(**info):
    print("Student Details:")
    for key, value in info.items():
        print(key, ":", value)

student_details(name="Alice", age=22, course="Python")

# ---------------------------------------------
# ✅ Scope: Local and Global Variables
# ---------------------------------------------

# Global variable
x = "global"

def my_func():
    x = "local"  # Local variable
    print("Inside function:", x)

my_func()
print("Outside function:", x)

# Use 'global' to modify global variable inside function
def modify_global():
    global x
    x = "changed globally"

modify_global()
print("After global change:", x)

# ---------------------------------------------
# ✅ Built-in Functions in Python (Common Examples)
# ---------------------------------------------

# ➤ print() – Outputs to console
print("This is a message")

# ➤ input() – Takes user input (as string)
# user_input = input("Enter your name: ")
# print("Hello", user_input)

# ➤ len() – Returns length of a sequence
name = "Python"
print("Length of name:", len(name))

# ➤ type() – Returns the data type
print("Type of name:", type(name))

# ➤ int(), float(), str(), bool() – Type casting
print(int("10") + 5)
print(float("3.14"))
print(str(100) + " is a string now")
print(bool(0))  # False

# ➤ max(), min(), sum()
numbers = [4, 9, 2, 7]
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))

# ➤ sorted(), reversed()
print("Sorted:", sorted(numbers))           # [2, 4, 7, 9]
print("Reversed:", list(reversed(numbers))) # [7, 2, 9, 4]

# ➤ abs() – Absolute value
print("Absolute of -5:", abs(-5))

# ➤ round() – Round a float
print("Rounded value:", round(3.567, 2))

# ➤ isinstance() – Check type
print("Is 5 an int?", isinstance(5, int))  # True

# ---------------------------------------------
# ✅ Anonymous Functions (lambda)
# ---------------------------------------------
# lambda functions are small, one-line anonymous functions

square = lambda x: x * x
print("Square of 4:", square(4))

add = lambda a, b: a + b
print("Addition using lambda:", add(3, 7))

# ---------------------------------------------
# ✅ Summary of Key Points
# ---------------------------------------------

# ➤ Use `def` to define a function
# ➤ Functions can take parameters and return values
# ➤ Use `*args` for variable positional args, `**kwargs` for keyword args
# ➤ Python has many built-in functions (print, input, len, type, etc.)
# ➤ Use lambda for small, one-line functions
