class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap count
        if len(s) != len(t):
            return False
            
        # use '.get(i, default)' !!!
        countS, countT = {}, {}
        for i in range(len(s)):
            # if s[i] not in countS:
                # countS[s[i]] = 0
            # countS[s[i]] = 1 + countS[s[i]]
            countS[s[i]] = 1 + countS.get(i, 0)

            # if t[i] not in countT:
                # countT[t[i]] = 0
            # countT[t[i]] = 1 + countT[t[i]]
            countT[t[i]] = 1 + countT.get(i, 0)

        for c in countS:
            # if countS[c] != countT[c]:
            if countS[c] != countT.get(c, 0):
                return False
                
        return True