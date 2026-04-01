class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for c in s:
            if c in count:
                count[c] += 1 ##=
            else:
                count[c] = 1
        ##print(count)
        ##print('-------')
        for c in t:
            if c not in count:
                return False 
            else:
                if count[c] == 0: ##==
                    return False
                count[c] -= 1 ##=
        return True

            