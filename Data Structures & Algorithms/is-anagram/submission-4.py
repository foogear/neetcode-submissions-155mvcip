class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # it's a good solution 
        s = sorted(s)
        t = sorted(t)
        
        if s == t:
            return True
        
        return False