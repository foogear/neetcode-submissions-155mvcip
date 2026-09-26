class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW, COL = len(matrix), len(matrix[0])

        def setNegativeOne(R, C):
            r, c = R - 1, C
            while r >= 0  and matrix[r][c]:
                matrix[r][c] = -1
                r -= 1

            r, c = R + 1, C
            while r < ROW and matrix[r][c]:
                matrix[r][c] = -1
                r += 1

            r, c = R, C - 1
            while c >= 0  and matrix[r][c]:
                matrix[r][c] = -1
                c -= 1

            r, c = R, C + 1
            while c < COL and matrix[r][c]:
                matrix[r][c] = -1
                c += 1

        for r in range(ROW):
            for c in range(COL):
                if not matrix[r][c]:
                    setNegativeOne(r, c)

        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == -1:
                    matrix[r][c] = 0