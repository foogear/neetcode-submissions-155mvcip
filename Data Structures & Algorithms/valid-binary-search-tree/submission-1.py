# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:



        def checkNode(root):
            if not root:
                return True
            # print(f"root {root.val}") ####

            l = root.left
            r = root.right

            #if l and root.val < l.val:
            if l and root.val <= l.val:
                return False
            #if r and root.val > r.val:
            if r and root.val >= r.val:
                return False

            if not checkNode(l):
                return False
            if not checkNode(r):
                return False

            return True

        return checkNode(root)