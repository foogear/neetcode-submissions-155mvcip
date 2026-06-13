class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = []
        for i in range(n):
            adj.append([])
        for l, r, w in edges:
            adj[l].append((w, r))
            adj[r].append((w, l))

        visited = set()
        minWeightHeap = [(0, 0)]
        totalWeight = 0
        while minWeightHeap and (len(visited) < n):
            currWeight, curr = heapq.heappop(minWeightHeap)
            if curr in visited:
                continue
            visited.add(curr)
            totalWeight += currWeight

            for nextWeight, next in adj[curr]:
                if next in visited:
                    continue
                heapq.heappush(minWeightHeap, (nextWeight, next))
                
        return totalWeight if len(visited) == n else -1






