# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:###????
            return []


        if (not root.left) and (not root.right):
            return [root.val]


        resultList = []

        if root.left:
            resultList = resultList+(self.inorderTraversal(root.left))

        resultList = resultList+[root.val]

        if root.right:
            resultList = resultList+(self.inorderTraversal(root.right))

        return resultList