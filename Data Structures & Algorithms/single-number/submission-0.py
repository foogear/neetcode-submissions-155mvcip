class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        res = 1

        for i in nums: # Addition "+" won't work
            if res % i == 0:
                res /= i
            else:
                res *= i

        return int(res)
