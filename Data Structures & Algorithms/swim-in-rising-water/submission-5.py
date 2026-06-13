class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        def getAdj(curr, grid):
            adj = []
            r, c = curr
            if c - 1 > -1:
                left = (r, c - 1)
                adj.append(left)
            if c + 1 < len(grid[0]):
                right = (r, c + 1)
                adj.append(right)
            if r - 1 > -1:
                up   = (r - 1, c)
                adj.append(up)
            if r + 1 < len(grid):
                down = (r + 1, c)
                adj.append(down)

            return adj

        costMap = {}
        currLevel = 0
        # minCostHeap = [(         0, (0,0))] # BUG
        minCostHeap   = [(grid[0][0], (0,0))]
        end = (len(grid) - 1, len(grid[0]) - 1)
        while minCostHeap and (end not in costMap):
            currCost, curr = heapq.heappop(minCostHeap)
            if curr in costMap:
                continue
            costMap[curr] = currCost
            currLevel = max(currLevel, grid[curr[0]][curr[1]])

            currAdj = getAdj(curr, grid)
            for next in currAdj:
                if next in costMap:
                    continue

                if grid[next[0]][next[1]] <= currLevel:
                    nextCost = 0
                else:
                    nextCost = grid[next[0]][next[1]] - currLevel
                heapq.heappush(minCostHeap, (currCost + nextCost, next))

        return costMap[end]
        

