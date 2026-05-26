# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr, stack = root, []
        res = []
        while curr or stack:
            if curr:
                stack.append(curr.right)
                res.append(curr.val)
                curr = curr.left
            else:
                curr = stack.pop()
                
        return res


