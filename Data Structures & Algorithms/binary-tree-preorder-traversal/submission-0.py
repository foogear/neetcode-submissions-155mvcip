# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        while stack or root:
            if not root:
                root = stack.pop()
                #res.append(root.val)
                root = root.right
            else:
                stack.append(root)
                res.append(root.val)
                root = root.left

        return res

