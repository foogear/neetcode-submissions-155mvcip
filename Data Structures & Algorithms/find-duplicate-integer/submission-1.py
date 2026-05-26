class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        memo = set()

        for n in nums:
            if n in memo:
                return n
            memo.add(n)
            
        return -1