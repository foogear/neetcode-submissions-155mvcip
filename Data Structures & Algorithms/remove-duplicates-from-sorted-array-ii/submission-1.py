class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0
        currGroup = nums[L]
        # count = 1
        count = 0

        # for R in range(1, len(nums)):
        for R in range(0, len(nums)):
            if nums[R] == currGroup:
                if count >= 2:
                    # count += 1
                    continue
            else:
                currGroup = nums[R]
                count = 0

            # nums[L], nums[R] = nums[R], nums[L]
            nums[L] = nums[R]
            count += 1
            L += 1

        return L



# 最初はswapしているように見えないが
# swapやってる　あるいは　やってもいい
# ようなアルゴリズム