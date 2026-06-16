class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minEdges = []
        parent = {}
        for l, r, w in edges:
            heapq.heappush(minEdges, (w, l, r))
            heapq.heappush(minEdges, (w, r, l))
            parent[l] = l
            parent[r] = r

        def findParent(v):
            p = v
            while p != parent[p]:
                p = parent[p]
                parent[v] = p
            return p

        mst = []
        weight = 0
        while minEdges:
            w, l, r = heapq.heappop(minEdges)

            pl, pr = findParent(l), findParent(r)
            inSameGroup = (pl == pr)
            if inSameGroup:
                continue
            mst.append((l, r))
            weight += w
            # parent[r] = pl BUG
            parent[pr] = pl

        return weight if len(mst) == n - 1 else -1



            