class Solution:
    def multiply(self, num1: str, num2: str) -> str:



        def strToInt(s):
            map = {"0":0, "1":1, "2":2, "3":3, "4":4,
                   "5":5, "6":6, "7":7, "8":8, "9":9}
            res = 0
            for i in range(len(s)):
                res += map[s[len(s) - 1 - i]] * (10 ** i)
            return res

        return str(strToInt(num1) * strToInt(num2))



