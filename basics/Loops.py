# ---------------------------------------------
# ✅ for Loop – Used to iterate over sequences
# ---------------------------------------------

# Example 1: Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# Example 2: Loop through a string
for char in "Python":
    print(char)

# Example 3: Using range() in a for loop
for i in range(5):  # 0 to 4
    print("Number:", i)

# Example 4: Range with start, stop, step
for i in range(1, 10, 2):  # From 1 to 9 with step of 2
    print("Odd number:", i)

# ---------------------------------------------
# ✅ while Loop – Runs while a condition is True
# ---------------------------------------------

# Example 1: Basic while loop
i = 1
while i <= 5:
    print("i is", i)
    i += 1  # Increase to avoid infinite loop

# Example 2: Infinite loop with break
count = 0
while True:
    print("Looping...")
    count += 1
    if count == 3:
        break  # Exit loop when count is 3

# ---------------------------------------------
# ✅ break, continue, and pass in loops
# ---------------------------------------------

# break – exits the loop completely
for i in range(10):
    if i == 5:
        print("Breaking at", i)
        break
    print("i =", i)

# continue – skips the rest of the current iteration
for i in range(5):
    if i == 2:
        print("Skipping", i)
        continue
    print("i =", i)

# pass – does nothing (used as a placeholder)
for i in range(3):
    if i == 1:
        pass  # Placeholder for future code
    print("i =", i)

# ---------------------------------------------
# ✅ else with loops
# ---------------------------------------------

# The else block runs only if the loop completes without a break

for i in range(3):
    print("i =", i)
else:
    print("Loop finished normally (no break)")

# With break
for i in range(3):
    if i == 1:
        break
    print("i =", i)
else:
    print("This won't run because of break")

# ---------------------------------------------
# ✅ Nested loops – Loop inside another loop
# ---------------------------------------------

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for a in adj:
    for f in fruits:
        print(a, f)

# ---------------------------------------------
# ✅ Looping through dictionaries
# ---------------------------------------------

my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Loop through keys
for key in my_dict:
    print("Key:", key)

# Loop through values
for value in my_dict.values():
    print("Value:", value)

# Loop through key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")

# ---------------------------------------------
# ✅ Using enumerate() in loops
# ---------------------------------------------

# Useful for getting both index and value
names = ["John", "Jane", "Doe"]

for index, name in enumerate(names):
    print(f"{index}: {name}")

# ---------------------------------------------
# ✅ Using zip() to loop through multiple sequences
# ---------------------------------------------

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")
