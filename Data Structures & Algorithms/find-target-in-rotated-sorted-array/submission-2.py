class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def myBinarySearch(target, lo, hi):
            while (lo <= hi):
                mi = (lo + hi) // 2
                # print(f"++++++++")####
                # print(f"lo{lo}, mi{mi}, hi{hi}")####
                if target == nums[mi]:
                    return mi

                if nums[lo] < nums[mi]:
                    # print("asc")####
                    # if target == nums[mi]:
                        # return mi
                    if nums[lo] <= target < nums[mi]:
                        hi = mi - 1
                    else:
                        lo = mi + 1
                else:
                    # print("no asc")####
                    # if target == nums[mi]:
                        # return mi
                    if nums[mi] < target < nums[lo]:
                        lo = mi + 1
                    else:
                        hi = mi - 1
                # print(f"lo{lo}, mi{mi}, hi{hi}")####
            return -1

        index = myBinarySearch(target, 0, len(nums) - 1)
        # print()####
        # print(index)####
        return index