class Solution:
    def strStr(self, haystack: str, needle: str) -> int:


        for i in range(len(haystack)):
            res = -1
            if haystack[i] == needle[0]:
                res = i
                for j in range(len(needle)):
                    if not (i+j < len(haystack)):
                        res = -1
                        break
                    if needle[j] != haystack[i+j]:
                        res = -1
                        break
            if res != -1:
                break 
        
        
        return res