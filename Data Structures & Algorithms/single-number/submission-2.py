class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # res = None
        # n XOR 0 = n
        res = 0
        for n in nums:
            # if not res:
                # res = n
                # continue
            res ^= n

        return res




