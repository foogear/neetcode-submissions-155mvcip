"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        nodeList = collections.deque()
        visited = set()
        nodeList.append(node)
        visited.add(node)

        newList = {}

        while nodeList:
            n = nodeList.popleft()
            if n.val not in newList:
                newList[n.val] = Node(n.val)
            for nei in n.neighbors:
                if nei not in visited:
                    nodeList.append(nei)
                    visited.add(nei)

        nodeList = collections.deque()
        visited = set()
        nodeList.append(node)
        visited.add(node)

        while nodeList:
            n = nodeList.popleft()
            for nei in n.neighbors:
                if nei not in visited:
                    nodeList.append(nei)
                    visited.add(nei)
                if not newList[n.val].neighbors:
                    newList[n.val].neighbors = []
                newList[n.val].neighbors.append(newList[nei.val])

        for n in newList:
            return newList[n]






