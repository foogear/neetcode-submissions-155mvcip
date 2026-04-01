class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:


        def solve(r, c, obstacleGrid):
            ROW, COL = len(obstacleGrid), len(obstacleGrid[0])

            if r > ROW - 1 or c > COL - 1:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if r == ROW - 1 and c == COL - 1:
                return 1

            res = (solve(r + 1, c,     obstacleGrid) + 
                   solve(r,     c + 1, obstacleGrid))

            return res

        return solve(0, 0, obstacleGrid)
