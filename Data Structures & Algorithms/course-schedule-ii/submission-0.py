class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [] # i reversed the tree here
        for _ in range(numCourses):
            adj.append([])
        for c, p in prerequisites:
            adj[c].append(p)

        visited = set()
        currPath = set()
        order = []

        def dfs(curr):
            if curr in visited:
                return True
            if curr in currPath:
                return False # loop
            currPath.add(curr)

            for neighbor in adj[curr]:
                if not dfs(neighbor): # forgot adding this
                    return False # forgot adding this
            currPath.remove(curr)
            visited.add(curr)
            order.append(curr)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return [] # loop

        return order



