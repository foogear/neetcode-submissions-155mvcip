class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        lo=0
        hi=(len(matrix)*len(matrix[0]))-1
        innerLen=len(matrix[0])

        while hi>=lo:
            mid=int((hi+lo)/2)

            if target > matrix[int(mid/innerLen)][int(mid%innerLen)]:
                lo=mid+1
            elif target < matrix[int(mid/innerLen)][int(mid%innerLen)]:
                hi=mid-1
            else:
                return True
        return False