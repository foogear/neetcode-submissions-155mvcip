class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def makePowerSub(nums):
            if len(nums) <= 1:
                return [nums]
            res = []
            for i in range(len(nums)):
                res.append([nums[i]])
                sub = makePowerSub(nums[i+1:])
                for s in sub:
                    if len(s) > 0:
                        res.append([nums[i]]+s)
            return res

        res = [[]] + makePowerSub(nums)
        return res

