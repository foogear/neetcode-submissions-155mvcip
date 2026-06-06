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
            if not digits:
                return []
            if i == len(digits) - 1:
                res = [[c] for c in ncMap[digits[i]]]
                return res

            res = []
            for l in ncMap[digits[i]]:
                for r in combination(digits, digitsLen, i + 1):
                    res.append([l] + r)

            return res

        resList = combination(digits)
        res = []
        for l in resList:
            res.append("".join(l))
            
        return res

