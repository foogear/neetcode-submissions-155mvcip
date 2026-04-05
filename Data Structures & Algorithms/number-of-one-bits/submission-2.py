class Solution:
    def hammingWeight(self, n: int) -> int:

        res = 0
        # while n > 0:
        while n:
            #if n % 2 == 1:
            res += n % 2
            n = n >> 1
        return res