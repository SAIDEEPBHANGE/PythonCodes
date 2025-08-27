# ---------------------------------------------
# ✅ What is a List?
# ---------------------------------------------
# A list is a collection which is ordered and mutable (can be changed).
# Lists can contain elements of different data types.

# Creating a list
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
mixed = [1, "hello", True, 3.14]

# Printing a list
print("Fruits list:", fruits)

# ---------------------------------------------
# ✅ Accessing List Elements (Indexing)
# ---------------------------------------------
print("First fruit:", fruits[0])     # apple
print("Last fruit:", fruits[-1])     # cherry

# ---------------------------------------------
# ✅ Modifying List Elements
# ---------------------------------------------
fruits[1] = "mango"
print("Modified list:", fruits)  # ['apple', 'mango', 'cherry']

# ---------------------------------------------
# ✅ List Length
# ---------------------------------------------
print("Number of fruits:", len(fruits))

# ---------------------------------------------
# ✅ Adding Items to a List
# ---------------------------------------------
# append() – Adds to end of the list
fruits.append("orange")
print("After append:", fruits)

# insert(index, value) – Inserts at specific position
fruits.insert(1, "banana")
print("After insert:", fruits)

# extend() – Add multiple items from another list
more_fruits = ["grape", "pineapple"]
fruits.extend(more_fruits)
print("After extend:", fruits)

# ---------------------------------------------
# ✅ Removing Items from a List
# ---------------------------------------------
# remove(value) – Removes first matching value
fruits.remove("banana")
print("After remove:", fruits)

# pop() – Removes and returns last item (or item at index)
removed = fruits.pop()
print("Popped item:", removed)
print("After pop:", fruits)

# clear() – Empties the list
temp_list = [1, 2, 3]
temp_list.clear()
print("Cleared list:", temp_list)

# ---------------------------------------------
# ✅ Looping Through a List
# ---------------------------------------------
print("All fruits:")
for fruit in fruits:
    print(fruit)

# Loop with index
for i in range(len(fruits)):
    print(f"Fruit at index {i}:", fruits[i])

# Using enumerate()
for index, value in enumerate(fruits):
    print(f"Index {index} has {value}")

# ---------------------------------------------
# ✅ List Slicing
# ---------------------------------------------
numbers = [10, 20, 30, 40, 50]
print("First 3 elements:", numbers[:3])
print("Last 2 elements:", numbers[-2:])
print("Middle elements:", numbers[1:4])

# ---------------------------------------------
# ✅ Check if Item Exists
# ---------------------------------------------
if "apple" in fruits:
    print("Yes, apple is in the list")

# ---------------------------------------------
# ✅ Sorting and Reversing
# ---------------------------------------------
num_list = [3, 1, 4, 1, 5, 2]

num_list.sort()   # Sorts in place (ascending)
print("Sorted list:", num_list)

num_list.reverse()  # Reverses the list
print("Reversed list:", num_list)

# sorted() – Returns a new sorted list (original stays same)
original = [5, 3, 1]
print("Sorted copy:", sorted(original))
print("Original remains:", original)

# ---------------------------------------------
# ✅ Copying a List
# ---------------------------------------------
# Wrong way (shares reference):
a = [1, 2, 3]
b = a
b.append(4)
print("Original a after b changes:", a)  # Also changed!

# Correct way (creates a copy)
a = [1, 2, 3]
b = a.copy()
b.append(4)
print("Copy b:", b)
print("Original a remains:", a)

# Or use list slicing:
c = a[:]

# ---------------------------------------------
# ✅ List Comprehension (Short way to create lists)
# ---------------------------------------------
squares = [x ** 2 for x in range(1, 6)]
print("Squares:", squares)

even_numbers = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", even_numbers)

# ---------------------------------------------
# ✅ Nested Lists (List inside a list)
# ---------------------------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Middle element of matrix:", matrix[1][1])  # 5

# ---------------------------------------------
# ✅ Useful Built-in Functions with Lists
# ---------------------------------------------
numbers = [10, 20, 30, 40, 50]

print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))

# ---------------------------------------------
# ✅ Summary
# ---------------------------------------------
# - Lists are ordered, mutable collections
# - Use indexing to access/modify items
# - Use methods like append(), remove(), insert(), sort()
# - Use loops or comprehensions to process lists
# - Lists can be nested and support many operations

