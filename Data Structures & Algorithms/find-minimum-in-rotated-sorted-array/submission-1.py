class Solution:
    def findMin(self, nums: List[int]) -> int:
        lenNums = len(nums)
        def findDsc(lo, hi):
            if lo > hi:
                return -1
            # print(f"{lo} {hi}") ####

            m = (lo + hi) // 2
            l = m - 1
            r = m + 1
            if l >= 0:
                if nums[l] > nums[m]:
                    return m
            if r < lenNums:
                if nums[m] > nums[r]:
                    return r

            # check other nums
            leftIndex  = findDsc(lo, m - 1)
            if leftIndex  != -1:
                return leftIndex
            rightIndex = findDsc(m + 1, hi)
            if rightIndex != -1:
                return rightIndex

            return -1

        res = findDsc(0, lenNums - 1)
        # print(res) ####

        return nums[res] if res != -1 else nums[0]