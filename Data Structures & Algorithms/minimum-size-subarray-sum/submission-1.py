class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        sum = 0
        length = 0
        res = 0
        # array = []
        numsLen = len(nums)
        l, r = 0, -1

        while r < numsLen or sum >= target:
            r += 1
            while sum >= target:
                # print(">")
                length = r - l 
                if not res:
                    res = length
                res = min(res, length)
                # print(array)
                # array.remove(nums[l])
                sum -= nums[l]
                l += 1
            if r < numsLen:
                sum += nums[r]
                # array.append(nums[r])
            # print(array)

        return res


