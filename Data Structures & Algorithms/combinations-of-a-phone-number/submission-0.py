class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ncMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def combination(digits, digitsLen = len(digits), i = 0):

            if not digits:
                return []
            if i == len(digits) - 1:
                return ncMap[digits[i]]

            res = []
            for l in ncMap[digits[i]]:
                for r in combination(digits, digitsLen, i + 1):
                    res.append(l + r)

            return res

        return combination(digits)

