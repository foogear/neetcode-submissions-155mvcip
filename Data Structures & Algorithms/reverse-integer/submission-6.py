class Solution:
    def reverse(self, x: int) -> int:

        # It won't work 
        #    -2147483648         2147483647
        # if -8463847412 <= x <= 7463847412
        #                        1863847412
        #                        2147483681

        MIN = int((-1 * (1 << 31)) / 10)
        MAX = int(((1 << 31) - 1)  / 10)

        res = 0
        while x:
            res *= 10
            res += int(math.fmod(x, 10))
            x = int(x / 10)

            print(res)

            if res > MAX:
                return 0
            
            if res < MIN:
                return 0

        return res