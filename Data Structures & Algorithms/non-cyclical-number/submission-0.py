class Solution:
    def isHappy(self, n: int) -> bool:

        res = set()
        while True:

            sum = 0
            while n:
                sum += (n % 10) ** 2
                n = int(n / 10)
            n = sum

            if n == 1:
                return True
            if n in res:
                return False
            res.add(n)
            








