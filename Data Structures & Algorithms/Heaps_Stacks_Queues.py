# ==============================================
# Heaps, Stacks, and Queues in Python
# ==============================================

# ----------------------------------------------
# 1. STACKS
# ----------------------------------------------
# Stack is a linear data structure that follows
# Last-In-First-Out (LIFO) principle.
# The last element added is the first to be removed.

# Python lists can be used as stacks using append() and pop()

print("=== STACKS ===")

stack = []  # create an empty stack

# Push elements to the stack
stack.append('a')
stack.append('b')
stack.append('c')
print("Stack after pushes:", stack)  # ['a', 'b', 'c']

# Pop elements from the stack
print("Popped:", stack.pop())  # 'c'
print("Stack after pop:", stack)  # ['a', 'b']

# Peek the top element without removing it
top_element = stack[-1] if stack else None
print("Top element (peek):", top_element)

print("\n" + "="*50 + "\n")

# ----------------------------------------------
# 2. QUEUES
# ----------------------------------------------
# Queue is a linear data structure that follows
# First-In-First-Out (FIFO) principle.
# The first element added is the first to be removed.

# Python’s collections module has a deque class ideal for queues.

from collections import deque

print("=== QUEUES ===")

queue = deque()  # create an empty queue

# Enqueue elements (add to the right)
queue.append('a')
queue.append('b')
queue.append('c')
print("Queue after enqueues:", queue)  # deque(['a', 'b', 'c'])

# Dequeue elements (remove from the left)
print("Dequeued:", queue.popleft())  # 'a'
print("Queue after dequeue:", queue)  # deque(['b', 'c'])

# Peek the front element without removing it
front_element = queue[0] if queue else None
print("Front element (peek):", front_element)

print("\n" + "="*50 + "\n")

# ----------------------------------------------
# 3. HEAPS
# ----------------------------------------------
# Heap is a specialized tree-based data structure
# that satisfies the heap property.
# Min-heap: Parent node is smaller than or equal to children.
# Max-heap: Parent node is greater than or equal to children.

# Python provides a min-heap implementation in the heapq module.

import heapq

print("=== HEAPS ===")

# Create an empty list to represent heap
min_heap = []

# Push elements onto the heap
heapq.heappush(min_heap, 20)
heapq.heappush(min_heap, 15)
heapq.heappush(min_heap, 30)
heapq.heappush(min_heap, 10)

print("Min-Heap after pushes:", min_heap)
# The smallest element is at index 0

# Pop the smallest element
smallest = heapq.heappop(min_heap)
print("Popped smallest element:", smallest)
print("Min-Heap after pop:", min_heap)

# Peek the smallest element without popping
smallest_peek = min_heap[0] if min_heap else None
print("Smallest element (peek):", smallest_peek)

# ----------------------------------------------
# If you want a max-heap, you can invert values
# by pushing negative numbers (because heapq is min-heap)
max_heap = []

heapq.heappush(max_heap, -20)
heapq.heappush(max_heap, -15)
heapq.heappush(max_heap, -30)
heapq.heappush(max_heap, -10)

print("\nMax-Heap (using negatives):", max_heap)

# Pop the largest element (which is the smallest negative)
largest = -heapq.heappop(max_heap)
print("Popped largest element:", largest)
print("Max-Heap after pop:", max_heap)

# ----------------------------------------------
# Summary:
# ----------------------------------------------
# Stack: LIFO, implemented easily with list (append/pop).
# Queue: FIFO, best implemented with collections.deque (append/popleft).
# Heap: Min-heap by default via heapq; max-heap by negating values.
#
# These are fundamental data structures useful in algorithms and problem-solving.
