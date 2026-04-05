class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums = set(nums)

        missing = 0
        for i in range(len(nums) + 1):
            if missing not in nums:
                return missing
            missing += 1

        return 0






