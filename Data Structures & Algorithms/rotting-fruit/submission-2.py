import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def bfs(grid, lis, visited):
            ROW = len(grid); COL = len(grid[0])
            ##r, c = lis.popleft() BIGBIG BUG
            ##visited.add((r, c)) BIGBIG BUG

            countTime = 0
            direction = ((-1, 0),(+1, 0),(0, -1),(0, +1))

            while lis:

                ##print(lis)
                ##print(countTime)
                ##print()

                r, c, l = lis.popleft() 
                visited.add((r, c))

                for dr, dc in direction:
                    cantVisit = (r + dr < 0 or r + dr >= ROW or
                                 c + dc < 0 or c + dc >= COL or 
                                 (r + dr, c + dc) in visited or ## BUG NOT (r, c)
                                 grid[r + dr][c + dc] != 1)   ## BUG NOT grid[r][c]
                    if cantVisit:
                        continue
                    else:
                        lis.append((r + dr, c + dc, l + 1))
                        visited.add((r + dr, c + dc)) ## MUST DO
                        countTime = max(countTime, l + 1)

            return countTime

        rottedFruits = collections.deque()
        totalFruits = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    totalFruits += 1
                if grid[r][c] == 2:
                    rottedFruits.append((r, c, 0))
            
        visited = set()
        res = bfs(grid, rottedFruits, visited)

        if len(visited) != totalFruits:
            res = -1
        return res


