# ---------------------------------------------
# ✅ What is a Tuple?
# ---------------------------------------------
# A tuple is a collection that is:
# - Ordered
# - Immutable (cannot be changed)
# - Allows duplicate values

# Create a tuple using ()
my_tuple = ("apple", "banana", "cherry")
print("Tuple:", my_tuple)

# ---------------------------------------------
# ✅ Tuple vs List
# ---------------------------------------------
# Tuple:    () and immutable
# List:     [] and mutable

# ---------------------------------------------
# ✅ Creating Tuples
# ---------------------------------------------

# Tuple with multiple data types
mixed = ("text", 100, True, 3.14)

# Tuple with one item (must include comma)
one_item = ("hello",)
print("Type of one_item:", type(one_item))  # tuple

# Without comma → becomes a string
not_a_tuple = ("hello")
print("Type of not_a_tuple:", type(not_a_tuple))  # str

# ---------------------------------------------
# ✅ Accessing Elements
# ---------------------------------------------
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# ---------------------------------------------
# ✅ Slicing Tuples
# ---------------------------------------------
numbers = (10, 20, 30, 40, 50)
print("First 3:", numbers[:3])
print("Middle 3:", numbers[1:4])
print("Last 2:", numbers[-2:])

# ---------------------------------------------
# ✅ Looping Through a Tuple
# ---------------------------------------------
for item in my_tuple:
    print("Fruit:", item)

# Using index
for i in range(len(my_tuple)):
    print(f"Index {i} = {my_tuple[i]}")

# ---------------------------------------------
# ✅ Tuple Immutability
# ---------------------------------------------
# Tuples cannot be changed
# The following will cause an error:
# my_tuple[1] = "mango"  ❌

# But if tuple contains mutable objects, they can be changed:
mutable_tuple = ([1, 2], "hello")
mutable_tuple[0][0] = 99  # Modifying list inside tuple
print("Modified tuple:", mutable_tuple)

# ---------------------------------------------
# ✅ Tuple Unpacking
# ---------------------------------------------
person = ("Alice", 25, "Engineer")

name, age, job = person
print("Name:", name)
print("Age:", age)
print("Job:", job)

# You can also unpack partially using *
a, *b = (1, 2, 3, 4)
print("a:", a)
print("b:", b)

# ---------------------------------------------
# ✅ Tuple Methods
# ---------------------------------------------

# count() – counts how many times an item appears
t = (1, 2, 2, 3, 2)
print("Count of 2:", t.count(2))

# index() – returns first index of a value
print("Index of 3:", t.index(3))

# ---------------------------------------------
# ✅ Membership Test
# ---------------------------------------------
if "banana" in my_tuple:
    print("Yes, 'banana' is in the tuple")

# ---------------------------------------------
# ✅ Tuple Concatenation and Repetition
# ---------------------------------------------
t1 = (1, 2)
t2 = (3, 4)

# Concatenation
t3 = t1 + t2
print("Concatenated:", t3)

# Repetition
print("Repeat t1 3 times:", t1 * 3)

# ---------------------------------------------
# ✅ Nested Tuples
# ---------------------------------------------
nested = (1, 2, (3, 4), (5, 6))
print("Access nested:", nested[2][1])  # 4

# ---------------------------------------------
# ✅ Using Tuples as Dictionary Keys
# ---------------------------------------------
# Tuples are hashable (immutable), so can be used as keys
coordinates = {(0, 0): "Origin", (1, 2): "Point A"}
print("Point at (1,2):", coordinates[(1, 2)])

# ---------------------------------------------
# ✅ Built-in Functions with Tuples
# ---------------------------------------------
nums = (4, 1, 7, 2)

print("Length:", len(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))
print("Sorted (returns list):", sorted(nums))  # Doesn't modify the tuple

# ---------------------------------------------
# ✅ When to Use a Tuple?
# ---------------------------------------------
# ✔ When data should not be modified
# ✔ For faster performance than lists
# ✔ To use as dictionary keys or set elements

# ---------------------------------------------
# ✅ Summary
# ---------------------------------------------
# - Tuple is ordered, immutable
# - Use () to define tuples
# - Supports indexing, slicing, looping
# - Use count(), index() for basic methods
# - Supports unpacking, nesting, and can be used as dict keys
