class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        numSet = set()
        for i in range(min(k + 1, len(nums))):
            n = nums[i]
            if n in numSet:
                return True
            numSet.add(n)
        
        for i in range(k + 1, len(nums)):
            mostLeftNum = nums[i - k - 1]
            numSet.remove(mostLeftNum)
            n = nums[i]
            if n in numSet:
                return True
            numSet.add(n)
            
        return False






