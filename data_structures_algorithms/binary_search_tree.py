# ==============================================
# Binary Search Tree (BST) Implementation in Python
# ==============================================

# ----------------------------------------------
# What is a Binary Search Tree?
# ----------------------------------------------
# A BST is a binary tree where each node has:
# - A value (data)
# - Left child contains nodes with values less than the node's value
# - Right child contains nodes with values greater than the node's value
#
# This property allows efficient searching, insertion, and deletion.

# ----------------------------------------------
# Define the Node class representing each node in the BST
# ----------------------------------------------

class Node:
    def __init__(self, key):
        self.key = key      # Node value
        self.left = None    # Left child
        self.right = None   # Right child

# ----------------------------------------------
# Define the BST class with core operations
# ----------------------------------------------

class BinarySearchTree:
    def __init__(self):
        self.root = None  # Start with an empty tree

    def insert(self, key):
        """Insert a new node with given key."""
        if self.root is None:
            self.root = Node(key)
            print(f"Inserted root node with key: {key}")
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        """Recursive helper for insert."""
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
                print(f"Inserted {key} to left of {current_node.key}")
            else:
                self._insert(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
                print(f"Inserted {key} to right of {current_node.key}")
            else:
                self._insert(current_node.right, key)
        else:
            print(f"Key {key} already exists in the BST. Duplicate keys are not allowed.")

    def search(self, key):
        """Search for a node with given key."""
        return self._search(self.root, key)

    def _search(self, current_node, key):
        """Recursive helper for search."""
        if current_node is None:
            return False  # Not found

        if key == current_node.key:
            return True
        elif key < current_node.key:
            return self._search(current_node.left, key)
        else:
            return self._search(current_node.right, key)

    def inorder_traversal(self):
        """Return the keys of the BST in sorted order (inorder)."""
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, current_node, result):
        """Recursive helper for inorder traversal."""
        if current_node:
            self._inorder_traversal(current_node.left, result)
            result.append(current_node.key)
            self._inorder_traversal(current_node.right, result)

    def find_min(self):
        """Return the minimum key in the BST."""
        current = self.root
        if current is None:
            return None
        while current.left:
            current = current.left
        return current.key

    def find_max(self):
        """Return the maximum key in the BST."""
        current = self.root
        if current is None:
            return None
        while current.right:
            current = current.right
        return current.key

    def delete(self, key):
        """Delete a node with given key."""
        self.root = self._delete(self.root, key)

    def _delete(self, current_node, key):
        """Recursive helper for delete."""
        if current_node is None:
            print(f"Key {key} not found in the BST.")
            return None

        if key < current_node.key:
            current_node.left = self._delete(current_node.left, key)
        elif key > current_node.key:
            current_node.right = self._delete(current_node.right, key)
        else:
            # Node to delete found

            # Case 1: Node has no children (leaf)
            if current_node.left is None and current_node.right is None:
                print(f"Deleting leaf node with key {key}")
                return None

            # Case 2: Node has one child
            if current_node.left is None:
                print(f"Deleting node with key {key}, replacing with right child")
                return current_node.right
            if current_node.right is None:
                print(f"Deleting node with key {key}, replacing with left child")
                return current_node.left

            # Case 3: Node has two children
            # Find inorder successor (smallest node in right subtree)
            min_larger_node = self._find_min_node(current_node.right)
            print(f"Deleting node with key {key}, replacing with inorder successor {min_larger_node.key}")
            current_node.key = min_larger_node.key
            # Delete the inorder successor
            current_node.right = self._delete(current_node.right, min_larger_node.key)

        return current_node

    def _find_min_node(self, node):
        """Find the node with minimum key in a subtree."""
        current = node
        while current.left:
            current = current.left
        return current

# ----------------------------------------------
# Usage example
# ----------------------------------------------

bst = BinarySearchTree()

# Insert nodes
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("\nInorder traversal (sorted keys):")
print(bst.inorder_traversal())  # Should print sorted keys

# Search nodes
print("\nSearch for 40:", bst.search(40))  # True
print("Search for 90:", bst.search(90))  # False

# Find min and max
print("\nMinimum key:", bst.find_min())
print("Maximum key:", bst.find_max())

# Delete nodes
bst.delete(20)  # Leaf node
bst.delete(30)  # Node with one child
bst.delete(50)  # Node with two children (root)

print("\nInorder traversal after deletions:")
print(bst.inorder_traversal())

