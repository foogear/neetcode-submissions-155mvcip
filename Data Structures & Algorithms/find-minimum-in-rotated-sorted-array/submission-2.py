class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binarySearch(lo, hi):
            # no need recursive
            while (lo < hi - 1): # I bf it out
                mi = (lo + hi) // 2
                # print("+++++++++++++")####
                # print(f"lo{lo}, mi{mi}, hi{hi}")####
                # print(f"isRotated {isRotated}")####
                if nums[lo] < nums[mi]:
                    lo = mi
                else:
                    hi = mi
                # print(f"lo{lo}, mi{mi}, hi{hi}")####

            # print(f"lo{lo}, hi{hi}")####
            if nums[lo] < nums[hi]:
                return 0

            return hi

        index = binarySearch(0, len(nums) - 1)

        return nums[index]