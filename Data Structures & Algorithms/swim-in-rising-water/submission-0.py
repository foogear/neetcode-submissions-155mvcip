class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        adj = []
        for i in range(len(grid)):
            adj.append([])
            for j in range(len(grid[0])):
                adj[i].append([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                left  = grid[i][j - 1] - grid[i][j] if j - 1 > -1 else None
                right = grid[i][j + 1] - grid[i][j] if j + 1 < len(grid[0]) else None
                up    = grid[i - 1][j] - grid[i][j] if i - 1 > -1 else None
                down  = grid[i + 1][j] - grid[i][j] if i + 1 < len(grid) else None
                if left  != None:
                    cost = left  if left  > 0 else 0
                    adj[i][j].append((cost, (i, j - 1)))
                if right != None:
                    cost = right if right > 0 else 0
                    adj[i][j].append((cost, (i, j + 1)))
                if up    != None:
                    cost = up if up > 0 else 0
                    adj[i][j].append((cost, (i - 1, j)))
                if down  != None:
                    cost = down if down > 0 else 0
                    adj[i][j].append((cost, (i + 1, j)))

        costMap = {}
        minCostHeap = [(0, (0,0))]
        end = (len(grid) - 1, len(grid[0]) - 1)
        while minCostHeap and (end not in costMap):
            currCost, curr = heapq.heappop(minCostHeap)
            if curr in costMap:
                continue
            costMap[curr] = currCost

            for nextCost, next in adj[curr[0]][curr[1]]:
                if next in costMap:
                    continue
                heapq.heappush(minCostHeap, (currCost + nextCost, next))
                
        return costMap[end]

