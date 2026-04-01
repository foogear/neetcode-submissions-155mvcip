import collections

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        toVisit = collections.deque()
        visited = set() ## O(1)

        def dfs(r,c):
            ##print("dfs")

            if grid[r][c] == 0:
                return 0

            toVisit.append((r, c))
            visited.add((r, c))
            count = 1

            while len(toVisit) > 0:
                ##print(f"to visit{toVisit}")
                ##print(f"visited{visited}")
                r, c = toVisit.popleft()
                ##visited.add((r, c)) ## Forgot this will loop
                directions = ((-1, 0),(1, 0),(0, -1),(0, 1))

                for dr, dc in directions:
                    if r + dr in range(len(grid)) and \
                       c + dc in range(len(grid[0])) and \
                       (r + dr, c + dc) not in visited and grid[r + dr][c + dc] == 1:
                        toVisit.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc)) ##
                        count += 1
            
            return count

        res = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                p = (r, c)
                if p not in visited and \
                   grid[r][c] == 1: ## Forgot this too
                    res = max(res, dfs(r, c))
                    ##print(res)

        
        return res

