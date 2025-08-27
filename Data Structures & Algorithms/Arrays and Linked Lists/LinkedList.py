# ---------------------------------------------
# What is a Linked List?
# ---------------------------------------------
# A linked list is a linear data structure where each element (node) points to the next.
# Unlike arrays, linked lists store elements non-contiguously in memory.
# Useful for efficient insertions/deletions at any position.

# ---------------------------------------------
# Implementing a singly linked list from scratch:
# ---------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to next node (initially None)

class LinkedList:
    def __init__(self):
        self.head = None  # Start of linked list

    def append(self, data):
        """Add a node at the end"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # If list empty, new node is head
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        """Add a node at the beginning"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Delete first node with given data"""
        current = self.head

        if current and current.data == key:
            self.head = current.next  # Change head
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"Value {key} not found in list.")
            return

        prev.next = current.next

    def print_list(self):
        """Print all nodes"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# ---------------------------------------------
# Usage example:
# ---------------------------------------------
ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()  # Output: 1 -> 2 -> 3 -> None

ll.prepend(0)
ll.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None

ll.delete(2)
ll.print_list()  # Output: 0 -> 1 -> 3 -> None

ll.delete(10)  # Output: Value 10 not found in list.
