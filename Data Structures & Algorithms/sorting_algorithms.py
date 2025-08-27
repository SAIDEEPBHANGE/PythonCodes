# ==============================================
# Sorting Algorithms in Python
# ==============================================

# Sorting algorithms arrange data in a particular order (usually ascending).
# Below are common sorting algorithms with clear explanations and code.

# ----------------------------------------------
# 1. Bubble Sort
# ----------------------------------------------
# Repeatedly swaps adjacent elements if they are in wrong order.
# Time Complexity: O(n²)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr1 = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr1)
print("Bubble Sorted:", arr1)

# ----------------------------------------------
# 2. Selection Sort
# ----------------------------------------------
# Selects the smallest element and swaps it with the first unsorted element.
# Time Complexity: O(n²)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr2 = [64, 25, 12, 22, 11]
selection_sort(arr2)
print("Selection Sorted:", arr2)

# ----------------------------------------------
# 3. Insertion Sort
# ----------------------------------------------
# Builds sorted array one element at a time by inserting elements into their correct position.
# Time Complexity: O(n²)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr3 = [12, 11, 13, 5, 6]
insertion_sort(arr3)
print("Insertion Sorted:", arr3)

# ----------------------------------------------
# 4. Merge Sort
# ----------------------------------------------
# Divide and conquer algorithm:
# - Divides array into halves recursively
# - Merges sorted halves
# Time Complexity: O(n log n)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)  # Sorting left half
        merge_sort(right_half)  # Sorting right half

        i = j = k = 0

        # Merge the two halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr4 = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr4)
print("Merge Sorted:", arr4)

# ----------------------------------------------
# 5. Quick Sort
# ----------------------------------------------
# Divide and conquer algorithm:
# - Picks a pivot element and partitions array
# - Recursively sorts sub-arrays
# Time Complexity: Average O(n log n), Worst O(n²)

def quick_sort(arr):
    _quick_sort(arr, 0, len(arr) - 1)

def _quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        _quick_sort(arr, low, pi - 1)
        _quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr5 = [10, 7, 8, 9, 1, 5]
quick_sort(arr5)
print("Quick Sorted:", arr5)

# ----------------------------------------------
# 6. Built-in Python sort()
# ----------------------------------------------
# Python provides a highly optimized built-in sort function.
# It uses Timsort (a hybrid sorting algorithm derived from merge sort and insertion sort).

arr6 = [3, 6, 8, 10, 1, 2, 1]
arr6.sort()  # Sorts in place
print("Built-in sorted:", arr6)

# Or use sorted() to return a new sorted list
arr7 = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = sorted(arr7)
print("Built-in sorted (new list):", sorted_arr)

# ----------------------------------------------
# Summary:
# ----------------------------------------------
# - Bubble, Selection, Insertion Sort are simple but inefficient (O(n²)) for large data.
# - Merge Sort and Quick Sort are efficient (O(n log n)) and commonly used.
# - Python’s built-in sort() is highly optimized and recommended for practical use.
