# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = [0]
        def bfs(root):
            if not root:
                return
            nodes = [root]

            while nodes:
                currlayerNode = len(nodes)
                children = []
                for i in range(currlayerNode):
                    lc, rc = nodes[i].left, nodes[i].right
                    if lc:
                        children.append(lc)
                    if rc:
                        children.append(rc)
                depth[0] += 1
                nodes = children

        bfs(root)
        
        return depth[0]




