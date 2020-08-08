# 1008. Construct Binary Search Tree from Preorder Traversal

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inorder = sorted(preorder)

        return self.prefromin(preorder,inorder)

    def prefromin(self,preorder,inorder):
        prelen = len(preorder)
        inlen = len(inorder)
        if preorder == None or inorder == None or prelen!=inlen or prelen==0  :
            return None

        root = TreeNode(preorder[0])
        rootindex = inorder.index(root.val)



        root.left = self.prefromin(preorder[1:rootindex+1],inorder[:rootindex])
        root.right = self.prefromin(preorder[rootindex+1:],inorder[rootindex+1:])

        return root
