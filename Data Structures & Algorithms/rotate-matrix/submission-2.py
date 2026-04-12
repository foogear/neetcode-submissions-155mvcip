class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # use pointer so code is easier to read 
        left, right = 0, len(matrix) - 1

        while left <= right:
            top, bottom = left, right

            for i in range(right - left):
                # reverse the swap so only use one T
                topLeft = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = topLeft

            left += 1
            right -= 1







