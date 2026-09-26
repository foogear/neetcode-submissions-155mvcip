class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW, COL = len(matrix), len(matrix[0])

        setRow, setCol = set(), set()
        for r in range(ROW):
            for c in range(COL):
                if not matrix[r][c]:
                    setRow.add(r)
                    setCol.add(c)
                    
        for r in range(ROW):
            for c in range(COL):
                if r in setRow or c in setCol:
                    matrix[r][c] = 0