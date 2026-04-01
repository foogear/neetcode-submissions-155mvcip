class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def solve(r, c, ROW, COL, count):
            count[0] += 1

            if r == ROW or c == COL:
                return 0
            if r == ROW - 1 and c == COL - 1:
                return 1

            return (solve(r + 1, c,     ROW, COL, count) + 
                    solve(r,     c + 1, ROW, COL, count))

        count = [0]
        res = solve(0, 0, m, n, count)
        print(count[0])
        return res





