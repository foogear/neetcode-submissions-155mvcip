class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minIndex = -1
        # while l <= r:
        while   l <  r:
            # print(f"l{l}, r{r}")####
            if nums[l] > nums[l + 1]:
                minIndex = l + 1
                break
            if nums[r - 1] > nums[r]:
                minIndex = r
                break
            l += 1
            r -= 1
            
        # print(minIndex)####
        if minIndex == -1:
            minIndex = 0

        return nums[minIndex]