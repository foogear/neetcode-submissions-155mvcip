class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        LEN = len(matrix)

        for i in range(int(LEN / 2)):
            for j in range(i, LEN - 1 - i):
                t = None
                t, matrix[i][j] = matrix[i][j], t
                t, matrix[j][LEN - 1 - i] = matrix[j][LEN - 1 - i], t
                t, matrix[LEN - 1 - i][LEN - 1 - j] = matrix[LEN - 1 - i][LEN - 1 -j], t
                t, matrix[LEN - 1 - j][i] = matrix[LEN - 1 - j][i], t
                t, matrix[i][j] = matrix[i][j], t


