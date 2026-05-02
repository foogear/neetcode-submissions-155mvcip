class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        sSet = set()

        l = 0
        res = -1


        for r in range(len(s)):

            while s[r] in sSet:
                sSet.remove(s[l])
                l += 1
            if len(s) - l <= res:
                break
                
            sSet.add(s[r])
            res = max(res, len(sSet))

        return res


