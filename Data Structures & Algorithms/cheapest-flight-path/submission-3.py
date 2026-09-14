class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        print()
        adjMap = {}
        for i in range(n):
            adjMap[i] = []
        for start, end, cost in flights:
            adjMap[start].append((cost, end))

        dstCost = [10000]

        def dfs(start, cost, step, visited = set()):
            if start in visited:
                return
            visited.add(start)

            if step == k + 1:
                if start == dst:
                    dstCost[0] = min(dstCost[0], cost)
                visited.remove(start)
                return

            #if start in visited:
                #return
            #visited.add(start)

            for nextCost, next in adjMap[start]:
                dfs(next, nextCost + cost, step + 1, visited)

            visited.remove(start)

    


        dfs(src, 0, 0)
        if dstCost[0] != 10000:
            return dstCost[0]
        
        return -1####


