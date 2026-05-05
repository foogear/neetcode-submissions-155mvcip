class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # -10 -5 -2 |  1  2 3 4
        #  -6 -1  2 |  5  6 7 *
        #  -7 -2  1 |  4  5 *
        #  -8 -3  0 | (3) *
        #  -9 -4 -1 |  *
        # -12 -7  * |
        # -15  *    |
        #   *       | 
        # 　　離れる　|　近づく　目標は3
        # 　　飛ばせる|

        # -4 -3 -2  -1  |  2  5  10
        #  * -7 -6  -5  | -2  1  6
        #     * -5  -4  | -1  2  7
        #        * (-3) |  0  3  8
        #            *  |  1  4  9
        #               |  *  7  12
        #               |     *  15
        #               |        *
        #　     　近づく　|　離れる　目標は-3
        #               |　飛ばせる

        l, r = 0, len(numbers) - 1

        while l < r:

            if numbers[r] + numbers[l] > target:
                r -= 1
            elif numbers[r] + numbers[l] < target:
                l += 1
            else:
                return [numbers[l], numbers[r]]


