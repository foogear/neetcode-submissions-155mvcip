class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charMap = {}
        l = 0
        res = 0
        array = []

        for r in range(len(s)):
            print("***********")
            print(s[r])

            while not k and not s[r] == s[l]:
                print('not append') #
                charMap[s[l]] -= 1
                del array[0] #
                if s[l + 1] not in charMap: # BUG
                    charMap[s[l + 1]] = 0
                if s[l] != s[l + 1]: # BUG
                    k += charMap[s[l + 1]]
                    k -= charMap[s[l]]
                if l == r:
                    break
                l += 1
                print(array) #

            if k or s[r] == s[l]:
                print("append") #
                if s[r] not in charMap:
                    charMap[s[r]] = 0
                charMap[s[r]] += 1
                array.append(s[r]) #
                print(array) 
                if s[r] != s[l]:
                    print("!=")
                    k -= 1
            
            res = max(r - l + 1, res)
            print(f"res = {res}") #
            print(f"k={k}") #
            print(charMap) #
            
        return res
        
