class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        visited = set()
        currPath = set()
        topological = []

        adj = {}
        for l, r in edges:
            if l not in adj:
                adj[l] = []
            adj[l].append(r)

        def dfs(start):
            if start in visited: # BUG
                return True 
            if start in currPath:
                return False
            currPath.add(start)

            if start in adj:
                for r in adj[start]:
                    # if r not in visited:
                    if not dfs(r):
                        return False

            currPath.remove(start)
            topological.append(start)
            visited.add(start)

            return True

        for l, r in edges:
            if not dfs(l):
                return []

        topological.reverse()
        return topological



