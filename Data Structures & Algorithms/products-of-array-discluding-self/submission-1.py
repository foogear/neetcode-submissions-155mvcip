class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenNums = len(nums)

        postfix = [n for n in nums]
        for i in range(lenNums - 1, 0, -1):
            postfix[i - 1] *= postfix[i]
        postfix.append(1)

        prefix = nums
        for i in range(lenNums - 1):
            prefix[i + 1] *= prefix[i]
        prefix.pop()

        # print(postfix)
        # print(prefix)

        res = []
        res.append(postfix[1])
        for i in range(len(prefix)):
            res.append(prefix[i] * postfix[i + 2])

        return res




