# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        queue = deque()
        queue.append(root)
        
        results = []
        
        while root and len(queue) > 0:
            level = []
            for _ in range(len(queue)):
                popedNode = queue.popleft()
                if popedNode.left:
                    queue.append(popedNode.left)
                if popedNode.right:
                    queue.append(popedNode.right)
                level.append(popedNode.val)
            results.append(level[-1])
        
        return results
# Better read leetcode example first