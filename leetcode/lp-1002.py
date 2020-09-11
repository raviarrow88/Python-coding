# 1022. Sum of Root To Leaf Binary Numbers
# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
#
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
#
# Return the sum of these numbers.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def sumRootToLeaf(root,sum):
            if root is None:
                return 0

            sum = ( sum <<1 )+root.val

            if (root.left is None) and (root.right is None):
                return sum
            else:
                return sumRootToLeaf(root.left,sum) + sumRootToLeaf(root.right,sum)


        return sumRootToLeaf(root,0)
        
