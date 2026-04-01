class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydit = {}
        for n in nums:
            if n in mydit:
                return True
            else:
                mydit[n] = 0
        return False