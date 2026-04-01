import collections
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:


        def bfs(r = 0, c = 0, visited = set()): ## hashSet
            if grid[r][c] == 1:
                return -1
            ROW, COL = len(grid), len(grid[0])

            toBeVisit = collections.deque()
            toBeVisit.append((r, c))
            visited.add((r, c))

            res = 1
            countNodesOfLayer = 0 ## Bug
            while toBeVisit:

                ##print(f"res{res}")
                ###print(toBeVisit)
                ##print()

                if (ROW - 1, COL - 1) in visited:
                    return res

                if countNodesOfLayer == 0:
                    countNodesOfLayer = len(toBeVisit)
                    res += 1 ## Bug

                r, c = toBeVisit.popleft()
                countNodesOfLayer -= 1

                directions = ((-1, -1),(-1, 0),(-1, 1),
                              (+0, -1),(+0, 0),(+0, 1),
                              (+1, -1),(+1, 0),(+1, 1))
                for dr, dc in directions:
                    nextR , nextC = (r + dr, c + dc)
                    if nextR < 0 or nextC < 0 or \
                    nextR >= ROW or nextC >= COL or \
                    grid[nextR][nextC] == 1 or \
                    (nextR, nextC) in visited:
                        pass
                    else:
                        toBeVisit.append((nextR, nextC))
                        visited.add((nextR, nextC))
            
            return -1

        return bfs()