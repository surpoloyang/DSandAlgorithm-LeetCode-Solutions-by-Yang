# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def createTree(inorder, postorder, n):
            if n == 0:
                return None
            k = 0
            while postorder[n-1] != inorder[k]:
                k += 1
            root = TreeNode(inorder[k])
            root.left = createTree(inorder[:k], postorder[:k], k)
            root.right = createTree(inorder[k+1:], postorder[k:-1], n-1-k)
            return root
        return createTree(inorder, postorder, len(inorder))
