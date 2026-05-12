class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        prefix = 1
        for i in range(len(nums) - 1):
            prefix *= nums[i]
            res.append(prefix)

        # print(nums)
        # print(res)

        postfix = 1
        for i in range(len(nums) - 1, 0, -1):
            postfix *= nums[i]
            res[i - 1] *= postfix

        return res
        


