class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        def howSum(nums, target):
            if target == 0:
                return [[]]
            if target < 0:
                return [[]]
            res = []
            for i in range(len(nums)):
                nextTarget = target - nums[i]
                if not nextTarget < 0:
                    subRes = howSum(nums[i:], nextTarget)
                    if subRes:
                        for s in subRes:
                                res.append([nums[i]]+s)
            return res
        
        res = howSum(nums, target)
        return res