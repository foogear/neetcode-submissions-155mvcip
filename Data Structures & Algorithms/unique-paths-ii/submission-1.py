class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:


        def solve(r, c, obstacleGrid, memo = {}):
            ROW, COL = len(obstacleGrid), len(obstacleGrid[0])

            if r > ROW - 1 or c > COL - 1:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            if obstacleGrid[r][c] == 1:
                return 0
            if r == ROW - 1 and c == COL - 1:
                return 1

            memo[(r, c)] = (solve(r + 1, c,     obstacleGrid, memo) + 
                   solve(r,     c + 1, obstacleGrid, memo))

            return memo[(r, c)]

        return solve(0, 0, obstacleGrid)
