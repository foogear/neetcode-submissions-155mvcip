# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkNode(root, leftBoundary, rightBoundary):
            if not root:
                return True
            # print(f"root {root.val}") ####
            if not (leftBoundary < root.val < rightBoundary):
                return False

            l = root.left
            r = root.right
            #if l and l.val > root.val:
                #return False
            #if r and r.val < root.val:
                #return False
            if not checkNode(l, leftBoundary, root.val):
                return False
            if not checkNode(r, root.val, rightBoundary):
                return False

            return True

        return checkNode(root, -float("inf"), float("inf"))