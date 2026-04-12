class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        i, j = top, left

        res = []
        while (left <= right) and (top <= bottom):
            
            # print(0)
            # print(f"{i},{j}")
            res.append(matrix[i][j])

            while j < right:
                j += 1
                # print(1)
                # print(f"{i},{j}")
                res.append(matrix[i][j])
                
            while i < bottom:
                i += 1
                # print(2)
                # print(f"{i},{j}")
                res.append(matrix[i][j])
                
            while j > left and bottom - top:
                j -= 1
                # print(3)
                # print(f"{i},{j}")
                res.append(matrix[i][j])
                    
            while i > top + 1 and right - left:
                i -= 1
                # print(4)
                # print(f"{i},{j}")
                res.append(matrix[i][j])

            left, right = left + 1, right - 1
            top, bottom = top + 1, bottom - 1
            i, j = top, left
           

        return res


