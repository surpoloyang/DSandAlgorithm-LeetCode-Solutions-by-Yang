# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         def postorder(root):
#             if not root:
#                 return
#             postorder(root.left)
#             postorder(root.right)
#             res.append(root.val)
#         postorder(root)
#         return res

# 显示栈
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if not node.right or node.right == prev:
                res.append(node.val)
                prev = node
                root = None
            else:
                stack.append(node)
                root = node.right
        return res