class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            adj[(x, y)] = []
            
            for j in range(len(points)):
                if i == j:
                    continue
                rx = points[j][0]
                ry = points[j][1]
                cost = abs(x - rx) + abs(y - ry)
                adj[(x, y)].append((cost, rx, ry))

        minTreeWeight = 0
        # minCostHeap = [(0,            0,            0)]
        minCostHeap   = [(0, points[0][0], points[0][1])]
        visited = set()
        pointsAmount = len(points)
        while minCostHeap and len(visited) < pointsAmount:
            currCost, currX, currY = heapq.heappop(minCostHeap)
            if (currX, currY) in visited:
                continue
            visited.add((currX, currY))
            minTreeWeight += currCost

            for nextCost, nextX, nextY in adj[(currX, currY)]:
                if (nextX, nextY) in visited:
                    continue
                heapq.heappush(minCostHeap, (nextCost, nextX, nextY))

        return minTreeWeight


