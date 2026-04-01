# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def getIndex(self, _list: List[int], target):
        for i in range(0,len(_list)):
            if target == _list[i]:
                return i
        return None

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None

        if len(inorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        rootIndex = self.getIndex(inorder, root.val)

        root.left  = self.buildTree(preorder[1:1+rootIndex], inorder[0:rootIndex])
        root.right = self.buildTree(preorder[1+rootIndex: ], inorder[1+rootIndex:])

        return root