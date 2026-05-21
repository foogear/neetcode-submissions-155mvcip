class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        parent = {}
        height = {}
        res = [0]

        def findRoot(x):
            xp = x
            while xp != parent[xp]:
                xp = parent[xp]
                parent[x] = xp
            return xp

        def union(x, y):
            xp = findRoot(x)
            yp = findRoot(y)

            height[xp] += height[yp]
            res[0] = max(res[0], height[xp])
            parent[yp] = xp

        for n in nums:
            if n in parent:
                continue

            parent[n] = n
            height[n] = 1
            res[0] = max(res[0], height[n])

            if n - 1 in parent:
                union(n, n - 1)
            if n + 1 in parent:
                union(n, n + 1)

        return res[0]



