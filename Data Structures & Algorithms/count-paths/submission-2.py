class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        prevR = [1] * n
        count = 0

        for r in range(m - 2, -1, -1):
            currR = [1] * n
            count += 1

            for c in range(n - 2, -1, -1):
                currR[c] = currR[c + 1] + prevR[c]
                count += 1
            
            prevR = currR

        print(count)
        return currR[0]



