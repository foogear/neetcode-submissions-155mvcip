class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adjMap = {}
        for airport in range(n):
            adjMap[airport] = []
        for start, end, cost in flights:
            adjMap[start].append((cost, end))


        if src not in adjMap:
            return -1

        step, cost, end = 0, 0, src
        bfsMinCost = [(step, cost, end)]
        # no need visited maybe

        dstCost = 10000

        while bfsMinCost:
            #print()
            #print(bfsMinCost)
            step, cost, end = heapq.heappop(bfsMinCost)

            if step <= k + 1:
                if end == dst:
                    dstCost = min(dstCost, cost)
            else:
                continue
            

            for nextCost, next in adjMap[end]:
                nextCost += cost
                heapq.heappush(bfsMinCost, (step + 1, nextCost, next))

        if dstCost != 10000:
            return dstCost
        else:
            return -1

