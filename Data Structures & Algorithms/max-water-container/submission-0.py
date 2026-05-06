class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                l, r = heights[i], heights[j]
                res = max(res, (j - i) * min(l, r))

        return res

