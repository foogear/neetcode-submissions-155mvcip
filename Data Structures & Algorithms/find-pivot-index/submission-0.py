class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lenNums = len(nums)

        prefix = [0] + nums
        for i in range(lenNums):
            prefix[i + 1] += prefix[i]

        postfix = [n for n in nums] + [0]
        for i in range(lenNums - 1, 0, -1):
            postfix[i - 1] += postfix[i]

        # print(prefix)
        # print(postfix)

        for i in range(lenNums - 1):
            if prefix[i] == postfix[i + 1]:
                return i

        return -1














