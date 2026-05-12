class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        maxRow = len(matrix)
        maxCol = len(matrix[0])
        for r in range(maxRow):
            for c in range(maxCol):
                if r - 1 >= 0 and c - 1 >= 0:
                    matrix[r][c] -= matrix[r - 1][c - 1]
                if r + 1 < maxRow:
                    matrix[r + 1][c] += matrix[r][c]
                if c + 1 < maxCol:
                    matrix[r][c + 1] += matrix[r][c]
                # if r - 1 >= 0 and c - 1 >= 0: BUG
                    # matrix[r][c] -= matrix[r - 1][c - 1]
        self.m = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        T, B = row1, row2
        L, R = col1, col2
        res = self.m[B][R]
        if T - 1 >= 0:
            res -= self.m[T - 1][R]
        if L - 1 >= 0:
            res -= self.m[B][L - 1]
        if T - 1 >= 0 and L - 1 >= 0:
            res += self.m[T - 1][L - 1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)