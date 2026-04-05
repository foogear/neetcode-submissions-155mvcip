class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        short = text1
        long = text2
        if len(text1) > len(text2):
            short = text2
            long = text1

        def solve(short, long):
            res = 0
            index = 0
            for i in range(len(long)):
                if short[0] == long[i]:
                    index = i + 1
                    res += (1 + solve(short[1:], long[index:]))
                    break
            return res

        res = 0
        for i in range(len(short)):
            res = max(res, solve(short[i:], long))
            if res == len(short):
                break

        return res


