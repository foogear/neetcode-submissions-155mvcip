class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums.sort()
        res = 0
        for i in nums:
            if res != i:
                break 
            res += 1
        return res



