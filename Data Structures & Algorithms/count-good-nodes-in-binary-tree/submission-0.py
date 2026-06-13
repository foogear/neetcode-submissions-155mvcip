# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, pathMaxNum):
            if not root:
                return
            if root.val >= pathMaxNum:
                res[0] += 1
            pathMaxNum = max(pathMaxNum, root.val)
            dfs(root.left,  pathMaxNum)
            dfs(root.right, pathMaxNum)

        pathMaxNum = root.val
        res = [1]
        dfs(root.left,  pathMaxNum)
        dfs(root.right, pathMaxNum)
        
        return res[0]



