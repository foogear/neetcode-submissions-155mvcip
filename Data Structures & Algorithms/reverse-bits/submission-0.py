class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0
        for _ in range(32):
            res += (n & 1)
            res *= 2
            n = n >> 1
        
        return int(res/2)





