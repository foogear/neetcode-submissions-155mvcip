class Solution:
    def getSum(self, a: int, b: int) -> int:

        def cal(c, x, y):
            # print(f"{x},{y}")
            s = c ^ (x ^ y)
            c = (x & y) | (c & (x ^ y))
            # s = c ^ (x ^ y) ORDER MATTER 
            # print((c, s))
            return (c, s)

        res, c ,i= 0, 0, 0
        while a or b:
            c, s = cal(c, (a & 1), (b & 1))
            res = res | (s << i)
            i += 1
            a = a >> 1
            b = b >> 1

        return res | (c << i)
