class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs   = {}
        indexes = {}
        for i in range(len(nums)):
            otherHalf = target - nums[i]
            if otherHalf in pairs:
                if otherHalf * 2 == target: ## fix this
                    i1 = indexes[otherHalf]
                    i2 = i
                    return [min(i1, i2), max(i1, i2)]
            pairs  [nums[i]] = otherHalf
            indexes[nums[i]] = i
        
        print(pairs)
        print(indexes)

        for p in pairs:
            otherHalf = pairs[p]
            if otherHalf in indexes:
                i1 = indexes[p]
                i2 = indexes[otherHalf]
                if i1 == i2: # fix this
                    continue 
                return [min(i1, i2), max(i1, i2)]