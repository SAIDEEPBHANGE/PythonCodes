# ==============================================
# Hash Tables in Python – Complete Guide
# ==============================================

# ----------------------------------------------
# What is a Hash Table?
# ----------------------------------------------
# A hash table is a data structure that stores key-value pairs.
# It uses a hash function to compute an index where the value is stored.
# This allows for very fast data retrieval, usually O(1) time complexity.
#
# Python's built-in 'dict' type is implemented as a hash table.

# ----------------------------------------------
# Using Python's Built-in Dictionary (Hash Table)
# ----------------------------------------------

# Create a dictionary with some key-value pairs
my_dict = {
    "name": "Saideep",
    "age": 25,
    "city": "New York"
}

# Access elements by key (fast lookup)
print("Name:", my_dict["name"])  # Output: Saideep

# Add a new key-value pair or update existing key
my_dict["email"] = "saideep@example.com"
print("After adding email:", my_dict)

# Remove a key-value pair
del my_dict["age"]
print("After deleting age:", my_dict)

# Check if a key exists in the dictionary
if "city" in my_dict:
    print("City exists:", my_dict["city"])

# Iterate over all keys and values in the dictionary
print("All key-value pairs:")
for key, value in my_dict.items():
    print(f"  {key} : {value}")

print("\n" + "="*50 + "\n")

# ----------------------------------------------
# How Hash Tables Work (Conceptual Example)
# ----------------------------------------------
# Below is a simplified hash table implementation with chaining to handle collisions.

class SimpleHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Initialize table with None

    def _hash(self, key):
        """
        Simple hash function:
        Calculates sum of ASCII values of characters in the key
        and takes modulo with table size to get an index.
        """
        return sum(ord(char) for char in key) % self.size

    def set(self, key, value):
        """
        Insert or update the key with given value.
        Handles collisions with chaining (list at each bucket).
        """
        index = self._hash(key)

        # If no bucket exists at index, create an empty list
        if self.table[index] is None:
            self.table[index] = []

        # Check if key already exists in bucket, update value if found
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                print(f"Updated key '{key}' at index {index}.")
                return

        # If key not found, append new key-value pair
        self.table[index].append((key, value))
        print(f"Inserted key '{key}' at index {index}.")

    def get(self, key):
        """
        Retrieve value for the given key.
        Returns None if key is not found.
        """
        index = self._hash(key)

        if self.table[index] is None:
            return None  # No bucket, key not found

        for k, v in self.table[index]:
            if k == key:
                return v  # Return value if key matches

        return None  # Key not found in bucket

    def __str__(self):
        """String representation to show the hash table contents"""
        return str(self.table)


# ----------------------------------------------
# Usage of the SimpleHashTable class
# ----------------------------------------------
hash_table = SimpleHashTable(5)  # Small size to force collisions

# Insert key-value pairs
hash_table.set("name", "Saideep")
hash_table.set("age", 25)
hash_table.set("city", "New York")
hash_table.set("email", "saideep@example.com")

print("\nHash Table Contents:")
print(hash_table)

# Retrieve values by key
print("\nRetrieve values:")
print("Name:", hash_table.get("name"))      # Saideep
print("Age:", hash_table.get("age"))        # 25
print("City:", hash_table.get("city"))      # New York
print("Email:", hash_table.get("email"))    # saideep@example.com
print("Country:", hash_table.get("country"))  # None (not found)

print("\n" + "="*50 + "\n")

# ----------------------------------------------
# Collision Handling
# ----------------------------------------------
# When two different keys hash to the same index, a collision occurs.
# In this example, we handle collisions using chaining,
# where each index stores a list of key-value pairs.

# Example: Insert keys that likely collide due to the simple hash function
hash_table.set("abc", 123)
hash_table.set("bca", 456)  # 'abc' and 'bca' have the same letters, so likely collision

print("\nHash Table After Adding Colliding Keys:")
print(hash_table)

print("\nRetrieve Colliding Keys:")
print("abc:", hash_table.get("abc"))  # 123
print("bca:", hash_table.get("bca"))  # 456

# ----------------------------------------------
# Summary
# ----------------------------------------------
# - Python's dict is a built-in hash table with O(1) average lookup, insert, and delete.
# - Hash tables store key-value pairs using a hash function to compute storage index.
# - Collisions occur when two keys hash to the same index.
# - Chaining is one collision resolution method, storing multiple items per bucket.
# - Implementing a simple hash table helps understand the internals of Python dictionaries.
