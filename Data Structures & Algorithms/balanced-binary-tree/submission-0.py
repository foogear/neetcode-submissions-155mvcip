# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(root):
            nonlocal res
            if not root or not res:
                return 0

            L = dfs(root.left)
            R = dfs(root.right)

            if abs(L - R) > 1 or not res:
                res = False
                return 0

            return 1 + max(L, R)

        dfs(root)
        
        return res
