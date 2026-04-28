class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = nums[0]

        for i in range(len(nums)):
            curSum = 0
            for j in nums[i:]:
                curSum += j
                maxSum = max(maxSum, curSum)

        return maxSum

