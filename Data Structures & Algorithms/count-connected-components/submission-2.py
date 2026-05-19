class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [p for p in range(n)]
        # UnboundLocalError
        # components = n
        components = [n]
        print(parent)

        def findRoot(x):
            xp = x
            while xp != parent[xp]:
                xp = parent[xp]
                parent[x] = xp
            return xp

        def union(x, y):
            rx = findRoot(x)
            ry = findRoot(y)

            if rx == ry:
                return False

            # UnboundLocalError
            # components -= 1
            components[0] -= 1

            parent[y] = rx
            return True 

        for e in edges:
            union(e[0], e[1])

        print(parent)

        return components[0]
        





