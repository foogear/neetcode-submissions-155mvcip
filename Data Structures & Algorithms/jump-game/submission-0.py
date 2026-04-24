class Solution:
    def canJump(self, nums: List[int]) -> bool:

        def dfs(nums, s = 0, memo = {}):
            if s in memo:
                return memo[s]
            if s == len(nums) - 1:
                return True

            for i in range(1, nums[s] + 1):
                if dfs(nums, s + i, memo):
                    memo[s + i] = True
                    return True
            
            memo[s] = False
            return False

        return dfs(nums, 0)
        

