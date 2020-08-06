''' Program to find the element in tree ,returns True if value is found otherwise False'''

import collections


class BinarySearchTree:
    Node = collections.namedtuple('Node', ['left', 'right', 'value'])

    @staticmethod
    def contains(root, value):

        if root is None:
            return False
        if root.value == value:
            return True
        if value < root.value:
            return BinarySearchTree.contains(root.left, value)
        else:
           return BinarySearchTree.contains(root.right, value)


n1 = BinarySearchTree.Node(value=1, left=None, right=None)
n3 = BinarySearchTree.Node(value=3, left=None, right=None)
n2 = BinarySearchTree.Node(value=2, left=n1, right=n3)

print(BinarySearchTree.contains(n2, 3))