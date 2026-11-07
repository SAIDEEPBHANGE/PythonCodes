# ---------------------------------------------
# ✅ Python Type Casting (Type Conversion)
# ---------------------------------------------

# ➤ Type casting means converting one data type to another
# There are two types:
# - Implicit casting (done automatically by Python)
# - Explicit casting (done manually using functions like int(), str(), etc.)

# ---------------------------------------------
# ✅ Implicit Type Casting (automatic)
# ---------------------------------------------

# Python automatically converts smaller data types to larger ones

x = 5         # int
y = 2.0       # float

result = x + y  # Python converts x to float automatically
print("Result (implicit):", result)      # 7.0
print("Type of result:", type(result))   # float

# ---------------------------------------------
# ✅ Explicit Type Casting (manual)
# ---------------------------------------------

# ➤ Using built-in functions: int(), float(), str(), bool()

# int() – Converts to integer (removes decimals if float)
a = int(3.9)          # 3
print("int(3.9):", a)

# float() – Converts to float
b = float("5.67")     # 5.67
print("float('5.67'):", b)

# str() – Converts to string
c = str(123)          # "123"
print("str(123):", c)

# bool() – Converts to Boolean
print("bool(0):", bool(0))        # False
print("bool(1):", bool(1))        # True
print("bool(''):", bool(''))      # False
print("bool('hello'):", bool('hello'))  # True

# ---------------------------------------------
# ✅ Converting Between Types – Examples
# ---------------------------------------------

# String to int
num_str = "100"
num_int = int(num_str)
print("String to int:", num_int + 50)

# Int to string
age = 25
age_str = str(age)
print("Age is " + age_str)

# Float to int (note: this truncates decimals, doesn't round!)
print("int(9.99):", int(9.99))  # 9

# Int to float
print("float(10):", float(10))  # 10.0

# ---------------------------------------------
# ✅ Error Handling: Invalid Type Conversion
# ---------------------------------------------

# Example: Trying to convert a non-numeric string to int
value = "abc"

try:
    converted = int(value)  # This will raise ValueError
    print("Converted value:", converted)
except ValueError:
    print("Cannot convert 'abc' to integer!")

# ---------------------------------------------
# ✅ Real-World Example: Input Handling
# ---------------------------------------------

try:
    user_input = input("Enter a number: ")  # Always returns a string
    number = float(user_input)
    print("You entered:", number)
except ValueError:
    print("Invalid input! Please enter a number.")

# ---------------------------------------------
# ✅ Summary: Casting Functions
# ---------------------------------------------

# int(x)     → Converts x to an integer
# float(x)   → Converts x to a floating point number
# str(x)     → Converts x to a string
# bool(x)    → Converts x to a boolean

# ---------------------------------------------
# ✅ Quiz Tip:
# What will this print?
# print(int("5") + float("2.5"))  → Output: 7.5
