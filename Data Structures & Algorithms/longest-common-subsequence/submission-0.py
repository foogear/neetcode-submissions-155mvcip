class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        textMap1 = {}
        for s in text1:
            if s not in textMap1:
                textMap1[s] = 0
            textMap1[s] += 1

        textMap2 = {}
        for s in text2:
            if s not in textMap2:
                textMap2[s] = 0
            textMap2[s] += 1

        shorterMap = textMap1
        if len(textMap2) < len(textMap1):
            shorterMap = textMap2
        
        res = 0
        for s in shorterMap:
            res += min(textMap1.get(s, 0), textMap2.get(s, 0))

        return res
