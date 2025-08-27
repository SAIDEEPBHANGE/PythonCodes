# ---------------------------------------------
# ✅ What is a Dictionary?
# ---------------------------------------------
# A dictionary is an unordered, mutable collection of key-value pairs.
# Keys must be unique and immutable (like strings, numbers, or tuples).
# Values can be any data type and can be duplicated.

# Creating a dictionary with {}
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Person dictionary:", person)

# ---------------------------------------------
# ✅ Accessing Values by Key
# ---------------------------------------------
print("Name:", person["name"])    # Alice

# Using get() method – safer, returns None or default if key not found
print("Phone:", person.get("phone"))           # None
print("Phone with default:", person.get("phone", "Not available"))

# ---------------------------------------------
# ✅ Modifying Values
# ---------------------------------------------
person["age"] = 31
print("Updated age:", person["age"])

# Adding new key-value pair
person["email"] = "alice@example.com"
print("Added email:", person)

# ---------------------------------------------
# ✅ Removing Items
# ---------------------------------------------
# pop() – Remove item by key and return its value
age = person.pop("age")
print("Popped age:", age)
print("Dictionary after pop:", person)

# popitem() – Remove and return last inserted item (key, value)
last_item = person.popitem()
print("Popped last item:", last_item)
print("After popitem:", person)

# del – Remove item by key
del person["city"]
print("After deleting city:", person)

# clear() – Remove all items
person.clear()
print("After clear:", person)

# ---------------------------------------------
# ✅ Looping Through Dictionaries
# ---------------------------------------------
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Loop through keys
print("Keys:")
for key in person:
    print(key)

# Loop through values
print("Values:")
for value in person.values():
    print(value)

# Loop through key-value pairs
print("Items:")
for key, value in person.items():
    print(key, "->", value)

# ---------------------------------------------
# ✅ Dictionary Methods
# ---------------------------------------------
d = {"a": 1, "b": 2}

# keys() – returns keys view
print("Keys:", d.keys())

# values() – returns values view
print("Values:", d.values())

# items() – returns key-value pairs view
print("Items:", d.items())

# update() – update dictionary with another dictionary or iterable of pairs
d.update({"c": 3, "d": 4})
print("After update:", d)

# setdefault() – returns value if key exists, otherwise inserts key with a default value
value = d.setdefault("e", 5)
print("Set default for 'e':", value)
print("Dictionary now:", d)

# ---------------------------------------------
# ✅ Nested Dictionaries
# ---------------------------------------------
employees = {
    "emp1": {"name": "John", "age": 28},
    "emp2": {"name": "Jane", "age": 32}
}
print("Employee 1 name:", employees["emp1"]["name"])

# ---------------------------------------------
# ✅ Dictionary Comprehension
# ---------------------------------------------
# Create a dictionary with keys as numbers and values as their squares
squares = {x: x**2 for x in range(1, 6)}
print("Squares dict:", squares)

# ---------------------------------------------
# ✅ Check if Key Exists
# ---------------------------------------------
if "name" in employees["emp1"]:
    print("Name exists for emp1")

# ---------------------------------------------
# ✅ Using Different Data Types as Keys
# ---------------------------------------------
d = {
    1: "integer key",
    3.14: "float key",
    (1, 2): "tuple key"
}
print("Dictionary with different key types:", d)

# ---------------------------------------------
# ✅ When to Use Dictionaries?
# ---------------------------------------------
# ✔ Store data as key-value pairs
# ✔ Fast lookups by keys
# ✔ Organize complex data (like JSON)

# ---------------------------------------------
# ✅ Summary
# ---------------------------------------------
# - Dictionaries are mutable mappings of unique keys to values
# - Use {} or dict() to create
# - Access values by keys or get()
# - Modify, add, and delete key-value pairs easily
# - Loop with keys(), values(), items()
# - Supports nested dictionaries and comprehensions
