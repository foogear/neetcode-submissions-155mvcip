class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = 0
        for n in nums:
            if not n:
                if zero:
                    product = 0
                    break 
                zero += 1
                continue
            product *= n
        
        for i in range(len(nums)):
            numsI = nums[i]
            nums[i] = 0
            if zero:
                if zero == 1 and numsI == 0:
                    nums[i] = product
                continue
            nums[i] = int(product / numsI)

        return nums


