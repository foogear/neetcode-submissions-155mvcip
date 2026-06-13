class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        for i in range(len(points)):
            adj[i] = []

            for j in range(len(points)):
                if i == j:
                    continue
                lx, rx = points[i][0], points[j][0]
                ly, ry = points[i][1], points[j][1]
                cost = abs(lx - rx) + abs(ly - ry)
                adj[i].append((cost, j))
                
        minTreeWeight = 0
        minCostHeap   = [(0, 0)]
        visited = set()
        pointsAmount = len(points)
        while minCostHeap and len(visited) < pointsAmount:
            currCost, curr = heapq.heappop(minCostHeap)
            if curr in visited:
                continue
            visited.add(curr)
            minTreeWeight += currCost

            for nextCost, next in adj[curr]:
                if next in visited:
                    continue
                heapq.heappush(minCostHeap, (nextCost, next))

        return minTreeWeight


