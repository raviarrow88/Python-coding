# 111. Minimum Depth of Binary Tree
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        lNode = self.minDepth(root.left)
        rNode = self.minDepth(root.right)


        if not lNode and not rNode:
            return 1

        if lNode and not rNode:
            return lNode+1

        if rNode and not lNode:
            return rNode+1



        return min(lNode,rNode)+1
