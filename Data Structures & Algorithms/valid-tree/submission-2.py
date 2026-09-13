class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            if n == 1:
                return True
            return False

        # undirected Tree should consider as GROUP not ROOT

        vertexGroup = {}

        for v1, v2 in edges:
            g1 = vertexGroup.get(v1, None)
            g2 = vertexGroup.get(v2, None)
            if not g1 and not g2:
                groupID = 1 # Tree should only have 1 group
                vertexGroup[v1] = groupID
                vertexGroup[v2] = groupID
            elif not g1:
                vertexGroup[v1] = vertexGroup[v2]
            elif not g2:
                vertexGroup[v2] = vertexGroup[v1]
            else: # default がなければ未知な条件網羅できないから
                if vertexGroup[v1] == vertexGroup[v2]:
                    return False

        print(vertexGroup)
        if n == len(vertexGroup):
            return True

        return False