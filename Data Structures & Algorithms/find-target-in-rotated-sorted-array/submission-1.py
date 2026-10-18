class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bsPivot(lo, hi):
            while (lo < hi - 1):
                mi = (lo + hi) // 2
                if nums[lo] < nums[mi]:
                    lo = mi
                else:
                    hi = mi
            if nums[lo] < nums[hi]:
                return 0

            return hi

        def binarySearch(target, numList, lo, hi):
            while (lo <= hi):
                mi = (lo + hi) // 2
                if   target == numList[mi]:
                    return mi
                elif target <  numList[mi]:
                    hi = mi - 1
                else:
                    lo = mi + 1

            return -1

        lenNums = len(nums)
        pivot = bsPivot(0, lenNums - 1)
        # print(f"pivot{pivot}")####

        l = binarySearch(target, nums,     0, pivot - 1)
        if l != -1:
            return l
        r = binarySearch(target, nums, pivot, lenNums - 1)
        if r != -1:
            return r
            
        return -1