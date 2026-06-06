class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ncMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def combination(digits, digitsLen = len(digits), i = 0):
            res = []
            for i in range(len(digits) - 1, -1, -1):
                if not res:
                    res = [c for c in ncMap[digits[-1]]]
                    continue

                t = []
                for l in ncMap[digits[i]]:
                    t += [l + r for r in res.copy()]
                res = t

            return res
            
        return combination(digits)

