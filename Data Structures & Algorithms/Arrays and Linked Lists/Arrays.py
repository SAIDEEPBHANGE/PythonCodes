# ---------------------------------------------
# Python does not have a built-in array data type like some other languages,
# but the list type acts like a dynamic array.
# For fixed-type arrays, the 'array' module can be used.
# ---------------------------------------------

# Using Python lists as dynamic arrays:
arr = [10, 20, 30, 40]

print("Array:", arr)
print("Element at index 2:", arr[2])  # Output: 30

# Adding elements
arr.append(50)
print("After append:", arr)

# Removing elements
arr.remove(20)
print("After remove:", arr)

# Iterating over array
for element in arr:
    print(element)

# ---------------------------------------------
# Using the array module for fixed-type arrays:
import array

# 'i' means signed integer
int_array = array.array('i', [1, 2, 3, 4])

print("Array module array:", int_array)
print("First element:", int_array[0])
