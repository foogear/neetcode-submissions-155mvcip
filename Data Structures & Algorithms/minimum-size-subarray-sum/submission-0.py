class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        sum = 0
        length = 0
        l = 0
        res = 0
        
        for r in range(len(nums)):
            while sum >= target:
                length = r - l 
                if not res:
                    res = length
                res = min(res, length)
                sum -= nums[l]
                l += 1
            sum += nums[r]

        return res








