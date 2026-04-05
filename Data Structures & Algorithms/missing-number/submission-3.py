class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        total = int(0.5 * (1 + len(nums)) * len(nums))

        return total - sum(nums)