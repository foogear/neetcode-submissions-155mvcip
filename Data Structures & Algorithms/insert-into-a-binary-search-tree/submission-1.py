# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)
        
        targetNode = root
        while True:
            if   targetNode.val > val and targetNode.left:
                 targetNode = targetNode.left
                 continue
            elif targetNode.val < val and targetNode.right:
                 targetNode = targetNode.right
                 continue 
            break
        
        if val < targetNode.val:
            targetNode.left  = TreeNode(val)
        else:
            targetNode.right = TreeNode(val)

        return root
