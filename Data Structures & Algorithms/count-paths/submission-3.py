class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        prevR = [0] * n # Can solve small grid Instead of using [1]
        count = 0

        for r in range(m - 1, -1, -1): # To solve very small grid instead of m - 2
            currR = [1] * n
            count += 1

            for c in range(n - 2, -1, -1):
                currR[c] = currR[c + 1] + prevR[c]
                count += 1
            
            prevR = currR

        print(count)
        return currR[0]



