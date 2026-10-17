class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW, COL = len(matrix), len(matrix[0])

        def printMatrix():
            for r in matrix:
                print(r)
                
        def setRowColToNone(R, C):
            # print("start") ####
            # printMatrix() ####

            # NOT "-1"
            r, c = R - 1, C
            while r >= 0  and matrix[r][c] != 0:
                matrix[r][c] = None
                r -= 1

            r, c = R + 1, C
            while r < ROW and matrix[r][c] != 0:
                matrix[r][c] = None
                r += 1

            r, c = R, C - 1
            while c >= 0  and matrix[r][c] != 0:
                matrix[r][c] = None
                c -= 1

            r, c = R, C + 1
            while c < COL and matrix[r][c] != 0:
                matrix[r][c] = None
                c += 1

            # print("end") ####
            # printMatrix() ####
            # print() ####

        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    # setNegativeOne(r, c)
                    setRowColToNone(r, c)

        # print("allSetToNone") ####
        # printMatrix() ####
        # print() ####

        for r in range(ROW):
            for c in range(COL):
                # if matrix[r][c] == -1:
                if not matrix[r][c]:
                    matrix[r][c] = 0

        # print("return") ####
        # printMatrix() ####