class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [p for p in range(n)]
        components = n

        def findRoot(x):
            xp = x
            while xp != parent[xp]:
                xp = parent[xp]
                parent[x] = xp
            return xp

        def union(x, y):
            components -= 1

            rx = findRoot(x)
            ry = findRoot(y)

            if rx == ry:
                return False

            parent[y] = rx
            return True 

        for e in edges:
            union(e[0], e[1])
            
        return components
        





