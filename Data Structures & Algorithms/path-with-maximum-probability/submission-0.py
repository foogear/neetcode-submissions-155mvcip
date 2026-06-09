class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = []
        for node in range(n):
            adj.append([])
        for i in range(len(edges)):
            l, r, p = edges[i][0], edges[i][1], succProb[i]
            adj[l].append((p, r))
            # adj[r].append((p, l)) # 要る?

        probabilityMap = {}
        maxProbabilityEdge = [(-1, start_node)]

        while maxProbabilityEdge and (end_node not in probabilityMap):
            currProbability, curr = heapq.heappop(maxProbabilityEdge)
            currProbability *= -1

            if curr in probabilityMap:
                continue
            probabilityMap[curr] = currProbability

            for nextProbability, next in adj[curr]:
                heapq.heappush(maxProbabilityEdge, (currProbability * nextProbability * -1, next))

        return 0 if (end_node not in probabilityMap) else probabilityMap[end_node]



