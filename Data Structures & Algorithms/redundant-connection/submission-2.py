class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # グループ化して解く
        # par = {}
        par = [None] * (len(edges) + 10)

        def find(x):
            p = x
            while p != par[p]:
                p = par[p]
                par[x] = par[p]
            return p

        def union(x, y):
            rx = find(x)
            ry = find(y)

            if rx == ry:
                return False

            par[ry] = rx
            return True
            
        for e in edges:
            # if e[0] not in par:
            if par[e[0]] == None:
                par[e[0]] = e[0]
            # if e[1] not in par:
            if par[e[1]] == None:
                par[e[1]] = e[1]
            if not union(e[0], e[1]):
                return e





