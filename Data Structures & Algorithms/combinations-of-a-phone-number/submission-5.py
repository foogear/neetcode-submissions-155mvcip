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

        digitsLen = len(digits)
        def backtrack(i = 0, currStr = ""):
            if i == digitsLen:
                res.append(currStr)
                return

            for c in ncMap[digits[i]]:
                backtrack(i + 1, currStr + c)

        res = []
        if digits:
            backtrack()

        return res

