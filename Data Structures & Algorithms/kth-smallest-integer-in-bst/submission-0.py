# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def listMaker(self, root: Optional[TreeNode], k: int) -> list:

        if not root:
            return []

        resultsList = []
        if root.left:
            resultsList += self.listMaker(root.left,  k)
        
        if k > len(resultsList):
            resultsList += [root.val]

        if root.right and k > len(resultsList):
            resultsList += self.listMaker(root.right, k-len(resultsList))
            # NOTES '=' -> '+=', 'k' -> 'k-len(resultsList)'
        
        return resultsList
        


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        resultsList = self.listMaker(root, k)
        return resultsList[k-1]