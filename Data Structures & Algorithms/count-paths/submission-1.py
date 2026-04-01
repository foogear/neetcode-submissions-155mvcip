class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def solve(r, c, ROW, COL, count, memo = {}):
            count[0] += 1

            if r == ROW or c == COL:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            if r == ROW - 1 and c == COL - 1:
                return 1

            memo[(r, c)] = (solve(r + 1, c,     ROW, COL, count, memo) + 
                            solve(r,     c + 1, ROW, COL, count, memo))

            return memo[(r, c)]


        count = [0]
        res = solve(0, 0, m, n, count)
        print(count[0])
        return res





