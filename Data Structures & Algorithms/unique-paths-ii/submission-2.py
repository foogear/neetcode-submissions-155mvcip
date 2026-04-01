class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[ROW - 1][COL - 1]:
            return 0

        prevR = [0] * COL
        for r in range(ROW - 1, -1, -1):

            currR = [0] * COL
            for c in range(COL - 1, -1, -1):
                if not obstacleGrid[r][c]:
                    if r == ROW - 1 and c == COL - 1:
                        currR[c] = 1
                    elif c + 1 > COL - 1:
                        currR[c] =            0 + prevR[c]
                    else:
                        currR[c] = currR[c + 1] + prevR[c]
            prevR = currR

        return currR[0]


