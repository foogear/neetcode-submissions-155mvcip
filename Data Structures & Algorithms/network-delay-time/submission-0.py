class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = []
        for i in range(n + 1):
            adj.append([])
        for start, end, cost in times:
            adj[start].append((cost, end))

        minimumTime = 0
        costMap = {}
        minCostPath = [(0, k)]
        while minCostPath:
            currCost, curr = heapq.heappop(minCostPath)
            if curr in costMap:
                continue
            costMap[curr] = currCost
            minimumTime = max(minimumTime, currCost)

            for nextCost, next in adj[curr]:
                if next in costMap:
                    continue
                heapq.heappush(minCostPath, (currCost + nextCost, next))

        for node in range(1, n + 1):
            if node not in costMap:
                return -1

        return minimumTime

        