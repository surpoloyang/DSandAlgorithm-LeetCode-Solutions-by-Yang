# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        def createTree(preorder, inorder, n):
            if n == 0:
                return None
            k = 0
            while preorder[0] != inorder[k]:
                k += 1
            root = TreeNode(preorder[0])
            root.left = createTree(preorder[1:k+1], inorder[:k], k)
            root.right = createTree(preorder[k+1:], inorder[k+1:], n-1-k)
            return root
        return createTree(preorder, inorder, n)
