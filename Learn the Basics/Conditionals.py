# ---------------------------------------------
# ✅ Python Conditionals (if, elif, else)
# ---------------------------------------------

# ➤ Python uses `if`, `elif`, and `else` for decision making.

# ➤ Basic structure:

# if condition:
#     # code if condition is True
# elif another_condition:
#     # code if another condition is True
# else:
#     # code if none of the above conditions are True

# ---------------------------------------------
# ✅ Example 1: Simple if statement
x = 10

if x > 5:
    print("x is greater than 5")

# ---------------------------------------------
# ✅ Example 2: if...else
x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is NOT greater than 5")

# ---------------------------------------------
# ✅ Example 3: if...elif...else
x = 5

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# ---------------------------------------------
# ✅ Logical Operators: and, or, not

a = 10
b = 20

if a > 5 and b > 15:
    print("Both conditions are True")

if a > 15 or b > 15:
    print("At least one condition is True")

if not (a < 5):
    print("a is NOT less than 5")

# ---------------------------------------------
# ✅ Example 4: Nested if
age = 18

if age >= 18:
    if age < 21:
        print("You are an adult but not yet 21.")
    else:
        print("You are 21 or older.")
else:
    print("You are under 18.")

# ---------------------------------------------
# ✅ Example 5: Short-hand (Ternary) if

# Syntax: value_if_true if condition else value_if_false
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print("x is", result)

# ---------------------------------------------
# ✅ Example 6: Using input with error handling

try:
    num = int(input("Enter a number: "))
    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")
except ValueError:
    print("Invalid input. Please enter a valid number.")

# ---------------------------------------------
# ✅ Example 7: Check if a number is divisible by both 2 and 3
x = 12

if x % 2 == 0 and x % 3 == 0:
    print("x is divisible by both 2 and 3")
else:
    print("x is NOT divisible by both 2 and 3")

# ---------------------------------------------
# ✅ Example 8: Grade checker using conditionals
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# ---------------------------------------------
# ✅ Summary of Keywords:
# - `if`: Executes a block if the condition is True
# - `elif`: Else if; checks another condition
# - `else`: Executes if none of the above are True
# - Logical operators: `and`, `or`, `not`
