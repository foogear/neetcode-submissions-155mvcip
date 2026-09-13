class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            if n == 1:
                return True
            return False

        # undirected Tree should consider as GROUP not ROOT
        vertexGroup = {}

        # Tree should only have ONE group
        groupID = 1
        v1, v2 = edges[0]
        vertexGroup[v1] = groupID
        vertexGroup[v2] = groupID

        for v1, v2 in edges[1:]:
            g1 = vertexGroup.get(v1, None)
            g2 = vertexGroup.get(v2, None)
            if not g1 and not g2:
                # Tree only has ONE group
                return False
            elif not g1:
                vertexGroup[v1] = vertexGroup[v2]
            elif not g2:
                vertexGroup[v2] = vertexGroup[v1]
            else: # default がなければ未知な条件網羅できないから
                if vertexGroup[v1] == vertexGroup[v2]:
                    return False

        if n == len(vertexGroup):
            return True
            
        return False