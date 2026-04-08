class Solution:
    def reverse(self, x: int) -> int:

        sgn = 1
        if x < 0:
            sgn = -1
            x *= -1

        res = 0
        while x:
            res = (res + (x % 10)) * 10
            x = int(x / 10)

        if res - ((1 << 32) - 1) > 0:
            return 0

        return sgn * int(res / 10)
