class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pacific  = []
        for _ in range(ROW):
            pacific.append( [False] * COL)
        atlantic = []
        for _ in range(ROW):
            atlantic.append([False] * COL)

        def dfs(ocean, coord):
            stack = [coord]
            while stack:
                r, c = stack.pop()
                if (r, c) in visited:
                    continue
                visited.add((r, c))

                ocean[r][c] = True

                up    = (r - 1, c)
                down  = (r + 1, c)
                left  = (r    , c - 1)
                right = (r    , c + 1)
                direction = (up, down, left, right)
                for nextR, nextC in direction:
                    if nextR < 0 or nextR >= ROW:
                        continue
                    if nextC < 0 or nextC >= COL:
                        continue
                    if heights[r][c] <= heights[nextR][nextC]:
                        stack.append((nextR, nextC))

        visited = set()
        for c in range(COL):
            dfs(pacific, (0, c))
        for r in range(ROW):
            dfs(pacific, (r, 0))

        visited = set()
        for c in range(COL):
            dfs(atlantic, (ROW - 1, c))
        for r in range(ROW):
            dfs(atlantic, (      r, COL - 1))

        res = []
        for r in range(ROW):
            for c in range(COL):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])

        return res