class Solution:
    def reverse(self, x: int) -> int:

        # It won't work 
        #    -2147483648         2147483647
        # if -8463847412 <= x <= 7463847412
        #                        1863847412
        #                        2147483681

        MIN = (-1 * (1 << 31)) - 1 # -1 ???
        MAX = ((1 << 31) - 1)

        res = 0
        while x:
            res *= 10
            res += int(math.fmod(x, 10))
            x = int(x / 10)

            if res > MAX:
                return 0
            
            if res < MIN:
                return 0

        return res