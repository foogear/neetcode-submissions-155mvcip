class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = []
        for i in range(n):
            adj.append([])

        for start, end, weight in edges:
            adj[start].append((weight, end))

        shortestWeight = {}
        minEdgesHeap = [(0, src)]
        while minEdgesHeap:
            currWeight, curr = heapq.heappop(minEdgesHeap)

            if curr in shortestWeight: # ⭐⭐⭐
                continue # ⭐⭐⭐
            shortestWeight[curr] = currWeight

            for nextWeight, next in adj[curr]:
                # if next in shortestWeight: #　なくても良い
                    # continue #　なくても良い
                heapq.heappush(minEdgesHeap, (currWeight + nextWeight, next))

        for i in range(n):
            if i not in shortestWeight:
                shortestWeight[i] = -1

        return shortestWeight


