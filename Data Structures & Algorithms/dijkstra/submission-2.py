class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        weight = {}
        for i in range(n):
            weight[i] = -1
            
        adj = [None] * n
        for e in edges:
            l, r, w = e[0], e[1], e[2]
            if not adj[l]:
                adj[l] = []
            adj[l].append((r, w))

        def dijkstra(start):
            weight[start] = 0
            minHeap = [(weight[start], start)]

            while minHeap:
                currW, curr = heapq.heappop(minHeap)
                if weight[curr] == -1:
                    weight[curr] = currW

                if adj[curr]:
                    for i in range(len(adj[curr])):
                        nextNode, nextWeight = adj[curr][i][0], adj[curr][i][1]
                        if nextNode is None:
                            continue
                        heapq.heappush(minHeap, (weight[curr] + nextWeight, nextNode))
                        adj[curr][i] = (None, None)

        dijkstra(src)
        return weight



