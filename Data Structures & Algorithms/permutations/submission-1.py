class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numsLen = len(nums)
        def insert(i = 0):
            if i == numsLen - 1:
                return [[nums[i]]]

            res = []
            for prevPermute in insert(i + 1):
                for gap in range(len(prevPermute) + 1):
                    currPermute = prevPermute[0:gap] + [nums[i]] + prevPermute[gap: len(prevPermute)]
                    res.append(currPermute)

            return res
            
        return insert()



#         /     _ 3 4
#    _ 4 —    3 _ 4
#  /      \ 3 4 _
# 4
#  \        /     _ 4 3
#      4 _ —    4 _ 3
#           \ 4 3 _