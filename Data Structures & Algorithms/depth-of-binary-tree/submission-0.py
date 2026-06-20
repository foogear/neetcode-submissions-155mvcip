# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = [0]
        def dfs(root, currDepth):
            if not root:
                return 

            depth[0] = max(depth[0], currDepth)

            dfs(root.left,  currDepth + 1)
            dfs(root.right, currDepth + 1)

        dfs(root, 1)
        
        return depth[0]




