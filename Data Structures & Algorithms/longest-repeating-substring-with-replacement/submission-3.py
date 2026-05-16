class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        l, subLen, charMap = 0, 0, {}
        for r in range(len(s)):
            if s[r] not in charMap:
                charMap[s[r]] = 0

            shrink = not (k > 0 or (k == 0 and s[l] == s[r]))
            while shrink and l < r:
                subLen -= 1
                charMap[s[l]] -= 1
                l += 1
                if s[l] != s[l - 1]:
                    k += charMap[s[l]] - charMap[s[l - 1]]
                shrink = not (k > 0 or (k == 0 and s[l] == s[r]))

            charMap[s[r]] += 1

            if s[l] != s[r]:
                k -= 1

            subLen += 1
            res = max(res, subLen)

        return res




