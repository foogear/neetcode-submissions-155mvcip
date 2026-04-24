class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums = nums[::-1]
        goal = 0
        for i in range(1, len(nums)):
            if i - nums[i] <= goal:
                goal = i
        
        if goal == len(nums) - 1:
            return True
        return False


