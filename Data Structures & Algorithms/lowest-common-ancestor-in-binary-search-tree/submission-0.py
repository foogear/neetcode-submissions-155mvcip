# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:



        def bstSearch(root, t1, t2):

            if root == t1 or root == t2:
                return root

            if t1.val < root.val < t2.val:
                return root
            if t2.val < root.val < t1.val:
                return root

            if t1.val < root.val and t2.val < root.val:
                return bstSearch(root.left, t1, t2)
            
            if t1.val > root.val and t2.val > root.val:
                return bstSearch(root.right, t1, t2)


            







        return bstSearch(root, p, q)