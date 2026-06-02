class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        curr, count = nums[0], 0
        for n in nums:
            if n != curr:
                if count < 2:
                    return curr
                else:
                    curr = n
                    count = 0
                    # count += 1
            # else:
                # count += 1
            count += 1
            
        return nums[-1] # for will stop if not enough nums in the end



