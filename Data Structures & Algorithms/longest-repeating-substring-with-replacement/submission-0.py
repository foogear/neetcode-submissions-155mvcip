class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charMap = {}
        l = 0
        res = 0
        # array = []

        for r in range(len(s)):
            if k or s[r] == s[l]:
                # print('append')
                if s[r] not in charMap:
                    charMap[s[r]] = 0
                charMap[s[r]] += 1
                # array.append(s[r])
                # print(array)
                if s[r] != s[l]:
                    # print("!=")
                    k -= 1
            else:
                # print('not append')
                charMap[s[l]] -= 1
                # del array[0]
                if s[l] != s[l + 1]: # BUG
                    k += charMap[s[l + 1]]
                l += 1
                # print(array)

            res = max(r - l + 1, res)
            # print("*",end="")
            # print(res)
            # print(f"k={k}")
            # print(charMap)
            
        return res
        
