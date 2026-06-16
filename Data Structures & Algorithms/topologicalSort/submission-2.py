class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        visited = set()
        currPath = set()
        topological = []
        
        adj = []
        for l in range(n): #
            adj.append([]) #
        for l, r in edges:
            adj[l].append(r)

        def dfs(start):
            if start in visited: # has to check first
                return True 
            if start in currPath:
                return False
            currPath.add(start)

            # if start in adj: not using map now
            for r in adj[start]:
                # if r not in visited:
                if not dfs(r):
                    return False

            currPath.remove(start)
            topological.append(start)
            visited.add(start)

            return True

        for start in range(n):
            if not dfs(start):
                return []

        topological.reverse()
        return topological



