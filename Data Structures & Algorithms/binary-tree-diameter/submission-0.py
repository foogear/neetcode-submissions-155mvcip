# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxPathLen = [0]
        def dfs(root):
            if not root:
                return 0

            L = dfs(root.left)
            R = dfs(root.right)
            maxPathLen[0] = max(maxPathLen[0], L + R)

            return 1 + max(L, R)

        dfs(root)
        
        return maxPathLen[0]


