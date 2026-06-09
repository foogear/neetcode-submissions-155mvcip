class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        weight = {}
        for i in range(n):
            weight[i] = -1

        nodesMap = {}
        for e in edges:
            l, r ,w = e[0], e[1], e[2]
            if l not in nodesMap:
                nodesMap[l] = []
            nodesMap[l].append((r, w))

        def dijkstra(start):
            minHeap = []
            weight[start] = 0

            nextWeight, nextNode = (weight[start], start)
            heapq.heappush(minHeap, (nextWeight, nextNode))

            while minHeap:
                currW, curr = heapq.heappop(minHeap)
                if weight[curr] == -1:
                    weight[curr] = currW

                if curr in nodesMap:
                    for next in nodesMap[curr]:
                        nextWeight, nextNode = next[1], next[0]
                        heapq.heappush(minHeap, (weight[curr] + nextWeight, nextNode))

        dijkstra(src)
        return weight



