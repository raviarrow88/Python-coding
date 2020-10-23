# 449. Serialize and Deserialize BST
# Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.
#
# The encoded string should be as compact as possible.
#
#
#
# Example 1:
#
# Input: root = [2,1,3]
# Output: [2,1,3]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def encode(root, string):
            if root is None:
                string += '#,'
            else:
                string += str(root.val) + ','
                string = encode(root.left, string)
                string = encode(root.right, string)
            return string
        return encode(root, '')


    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def decode(l):
            if(l[0] == "#"):
                l.pop(0)
                return None
            root = TreeNode( l.pop(0) )
            root.left = decode(l)
            root.right = decode(l)
            return root
        return decode( data.split(",")[:-1] )

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
