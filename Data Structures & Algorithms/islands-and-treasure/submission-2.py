class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])

        def minBfs(minSearch):


            while minSearch:
                currStep, r, c = heapq.heappop(minSearch)


                up    = (r - 1, c)
                down  = (r + 1, c)
                left  = (    r, c - 1)
                right = (    r, c + 1)
                direction = (up, down, left, right)
                for nextR, nextC in direction:
                    if nextR < 0 or nextR >= ROW:
                        continue
                    if nextC < 0 or nextC >= COL:
                        continue
                    if  grid[nextR][nextC] > currStep + 1:
                        grid[nextR][nextC] = currStep + 1###
                        heapq.heappush(minSearch, (currStep + 1, nextR, nextC))

        minSearch = []
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    step = 0
                    heapq.heappush(minSearch, (step, r, c))

        minBfs(minSearch)