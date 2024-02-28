# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def createTree(preorder, postorder, n):
            if n == 0:
                return None
            root = TreeNode(preorder[0])
            if n == 1:
                return root
            k = 0
            while postorder[k] != preorder[1]: #后序遍历的第k位为左子树的根节点，即左子树有k+1个节点
                k += 1
            root.left = createTree(preorder[1:k+2], postorder[:k+1], k+1)
            root.right = createTree(preorder[k+2:], postorder[k+1:-1], n-2-k)
            return root
        return createTree(preorder, postorder, len(preorder))
