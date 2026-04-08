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

        res = sgn * int(res / 10)

        if not ((1 << 32) * -1) <= res <= ((1 << 32) - 1):
            return 0

        return res