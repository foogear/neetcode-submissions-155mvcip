class Solution:
    def reverse(self, x: int) -> int:
        
        sgn = 1
        if x < -1:
            sgn = -1
            x *= -1
            
        res = 0
        while x:
            res = (res + (x % 10)) * 10
            x = int(x / 10)

        res = sgn * int(res / 10)
        if -1 * (1 << 31) <= res <= (1 << 31) - 1:
            return res
            
        return 0