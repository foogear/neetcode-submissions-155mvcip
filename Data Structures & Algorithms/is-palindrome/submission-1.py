class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:

            if not (65 <= ord(s[l]) <= 90 or 97 <= ord(s[l]) <= 122 or 48 <= ord(s[l]) <= 57):
                l += 1
                continue 

            if not (65 <= ord(s[r]) <= 90 or 97 <= ord(s[r]) <= 122 or 48 <= ord(s[r]) <= 57):
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
            
        return True