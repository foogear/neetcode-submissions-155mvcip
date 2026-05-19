class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        for e in edges:
            currLen = len(nodes)
            nodes.add(e[0])
            nodes.add(e[1])
            if currLen == len(nodes):
                return e