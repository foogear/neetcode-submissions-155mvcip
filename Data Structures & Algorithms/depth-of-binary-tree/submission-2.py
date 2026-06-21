# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = [0]
        def dfs(root):
            if not root:
                return

            nodes = [(root, 1)]
            while nodes:
                node, currDepth = nodes.pop()
                depth[0] = max(depth[0], currDepth)
                if node.right:
                    nodes.append((node.right, currDepth + 1))
                if node.left:
                    nodes.append((node.left,  currDepth + 1))

        dfs(root)
        
        return depth[0]


