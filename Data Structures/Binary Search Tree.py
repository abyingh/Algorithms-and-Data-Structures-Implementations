""" Binary Search Tree is a node-based binary tree data structure which has the following properties:

- The left subtree of a node contains only nodes with keys lesser than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s key.
- The left and right subtree each must also be a binary search tree.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, item):
        if not self.root:
            self.root = Node(item)
        else:
            if self.root.value < Node(item).value:
                if self.root.right is None:
                    self.root.right = Node(item)
                else:
                    insert(self.root.right, item)
            else:
                if self.root.left is None:
                    self.root.left = Node(item)
                else:
                    insert(self.root.left, item)

    def inorder(self, root):
        root = self.root
        if root:
            inorder(root.left)
            print(root.value)
            inorder(root.right)
        else:
            return None

    def search(self, root, item):
        if item == root.value or not root:
            return root.value
        else:
            if item > root.value:
                self.search(root.right, item)
            else:
                self.search(root.left, item)

    def remove(self, root, item):
        if root.value == item or not root:
            root.value = None
            return

        if item > root.value:
            self.remove(root.right, item)
            root.right = None
        else:
            self.remove(root.left, item)
            root.left = None
