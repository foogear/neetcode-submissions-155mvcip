class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:


        costMap = {}
        adjMap = {}

        for airport in range(n):
            costMap[airport] = [10000, airport]
            adjMap[airport] = []

        for start, end, cost in flights:
            adjMap[start].append((cost, end))

        COSTINDEX = 0
        if src not in costMap:
            return -1
        costMap[src][COSTINDEX] = 0

        visited = set()
        minCostHeap = []
        heapq.heappush(minCostHeap, costMap[src])
        remainStop = k + 1

        print(costMap)
        print(adjMap)
        print(minCostHeap)
        while minCostHeap:
            currCost, curr = heapq.heappop(minCostHeap)
            if curr in visited:
                continue
            visited.add(curr)
            remainStop -= 1
            for nextCost, next in adjMap[curr]:
                if  costMap[next][COSTINDEX] > currCost + nextCost:
                    costMap[next][COSTINDEX] = currCost + nextCost
                    minCostHeap.append(costMap[next])

            if remainStop <= 0:
                break

        
        if costMap[dst][COSTINDEX] != 10000:
            return costMap[dst][COSTINDEX]

        return -1
