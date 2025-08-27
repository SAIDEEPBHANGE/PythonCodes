# ---------------------------------------------
# ✅ What is a Decorator?
# ---------------------------------------------
# A decorator is a function that takes another function as input,
# adds some functionality to it, and returns it.
# It allows you to modify or enhance functions without changing their code.

# ---------------------------------------------
# ✅ Basic Decorator Example
# ---------------------------------------------

def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

# Using the decorator manually:
def say_hello():
    print("Hello!")

decorated_function = my_decorator(say_hello)
decorated_function()

# ---------------------------------------------
# ✅ Using the @ Syntax to Apply Decorators
# ---------------------------------------------
@my_decorator
def say_goodbye():
    print("Goodbye!")

say_goodbye()

# The @my_decorator line is equivalent to:
# say_goodbye = my_decorator(say_goodbye)

# ---------------------------------------------
# ✅ Decorators with Arguments in the Original Function
# ---------------------------------------------
def decorator_with_args(func):
    def wrapper(name):
        print(f"Before calling {func.__name__}")
        func(name)
        print(f"After calling {func.__name__}")
    return wrapper

@decorator_with_args
def greet(name):
    print(f"Hello, {name}!")

greet("Saideep")

# ---------------------------------------------
# ✅ Decorators with Arbitrary Arguments (*args, **kwargs)
# ---------------------------------------------
def smart_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper

@smart_decorator
def add(x, y):
    return x + y

add(10, 20)

# ---------------------------------------------
# ✅ Decorating Functions that Return Values
# ---------------------------------------------
@smart_decorator
def multiply(x, y):
    return x * y

result = multiply(5, 4)
print("Result of multiply:", result)

# ---------------------------------------------
# ✅ Using functools.wraps to Preserve Metadata
# ---------------------------------------------
from functools import wraps

def better_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

@better_decorator
def say_welcome():
    """This function says welcome"""
    print("Welcome!")

say_welcome()
print("Function name:", say_welcome.__name__)
print("Docstring:", say_welcome.__doc__)

# ---------------------------------------------
# ✅ Applying Multiple Decorators
# ---------------------------------------------
def decorator1(func):
    def wrapper():
        print("Decorator 1 start")
        func()
        print("Decorator 1 end")
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2 start")
        func()
        print("Decorator 2 end")
    return wrapper

@decorator1
@decorator2
def say_hi():
    print("Hi!")

say_hi()

# Output:
# Decorator 1 start
# Decorator 2 start
# Hi!
# Decorator 2 end
# Decorator 1 end

# ---------------------------------------------
# ✅ Summary
# ---------------------------------------------
# - Decorators modify/enhance functions without changing their code
# - Use @decorator syntax for clarity and simplicity
# - Use *args and **kwargs in wrappers to support all functions
# - Use functools.wraps to preserve original function metadata
# - Decorators can be stacked (multiple decorators on one function)
