class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product, index, zero = 1, -1, 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
                index = i
                continue
            product *= nums[i]

        if zero > 1:
            nums = [0] * len(nums)
            return nums
        elif zero == 1:
            nums = ([0] * index) + [product] + ([0] * (len(nums) - index - 1))
            return nums
        prev, i = 1, 0
        for curr in nums:
            if not zero:
                product = int((product / curr) * prev)
                prev = curr
                nums[i] = product
                i += 1
        return nums


