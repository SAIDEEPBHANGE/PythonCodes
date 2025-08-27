# ---------------------------------------------
# ✅ What is a Set?
# ---------------------------------------------
# A set is an unordered collection of unique items.
# Sets are mutable but cannot contain duplicate elements.
# Sets do NOT support indexing or slicing.

# Creating a set using {}
fruits = {"apple", "banana", "cherry"}
print("Set:", fruits)

# Creating an empty set (must use set(), not {})
empty_set = set()
print("Empty set:", empty_set)

# ---------------------------------------------
# ✅ Creating Sets from Other Collections
# ---------------------------------------------
# From list
numbers_list = [1, 2, 3, 3, 4]
numbers_set = set(numbers_list)  # duplicates removed
print("Set from list:", numbers_set)

# From string
chars = set("hello")
print("Set from string:", chars)

# ---------------------------------------------
# ✅ Adding and Removing Elements
# ---------------------------------------------
# add() – Add single element
fruits.add("orange")
print("After add:", fruits)

# update() – Add multiple elements (from list, set, etc.)
fruits.update(["mango", "grape"])
print("After update:", fruits)

# remove() – Remove element, raises KeyError if not found
fruits.remove("banana")
print("After remove:", fruits)

# discard() – Remove element if present, no error if not found
fruits.discard("pineapple")  # no error even if not in set

# pop() – Remove and return a random element (since sets are unordered)
popped_item = fruits.pop()
print("Popped item:", popped_item)
print("Set after pop:", fruits)

# clear() – Remove all elements
fruits.clear()
print("After clear:", fruits)

# ---------------------------------------------
# ✅ Looping Through a Set
# ---------------------------------------------
colors = {"red", "green", "blue"}
for color in colors:
    print("Color:", color)

# ---------------------------------------------
# ✅ Set Operations
# ---------------------------------------------
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Set A:", a)
print("Set B:", b)

# Union – Elements in either set
print("Union:", a | b)        # or a.union(b)

# Intersection – Elements common to both sets
print("Intersection:", a & b)  # or a.intersection(b)

# Difference – Elements in a but not in b
print("Difference (A - B):", a - b)  # or a.difference(b)

# Symmetric Difference – Elements in either set but not both
print("Symmetric Difference:", a ^ b)  # or a.symmetric_difference(b)

# ---------------------------------------------
# ✅ Subset, Superset, and Disjoint
# ---------------------------------------------
c = {1, 2}

print("Is c subset of a?", c.issubset(a))        # True
print("Is a superset of c?", a.issuperset(c))    # True
print("Are a and b disjoint?", a.isdisjoint(b))  # False

# ---------------------------------------------
# ✅ Set Comprehension
# ---------------------------------------------
# Create a set of squares of numbers from 1 to 5
squares = {x ** 2 for x in range(1, 6)}
print("Squares set:", squares)

# ---------------------------------------------
# ✅ Frozenset (Immutable Set)
# ---------------------------------------------
# Frozensets are immutable sets, which means their elements cannot be changed after creation.

fs = frozenset([1, 2, 3, 4])
print("Frozenset:", fs)

# fs.add(5)  # This will raise an AttributeError

# ---------------------------------------------
# ✅ When to Use Sets?
# ---------------------------------------------
# ✔ When you need unique items only
# ✔ Fast membership testing (checking if an item exists)
# ✔ Mathematical set operations (union, intersection, etc.)
# ✔ Removing duplicates from collections

# ---------------------------------------------
# ✅ Summary
# ---------------------------------------------
# - Sets are unordered collections of unique elements
# - Use {} or set() to create sets
# - No indexing, slicing; but you can loop through sets
# - Use add(), remove(), union(), intersection() and more
# - Use frozenset for immutable sets
