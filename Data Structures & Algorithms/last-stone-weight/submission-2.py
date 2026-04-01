import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = -heapq.heappop(stones)
            s2 = -heapq.heappop(stones)
            res = max(s1,s2) - min(s1,s2)
            if res:
                heapq.heappush(stones, -res)

        if len(stones) == 0:
            return 0
            
        return -stones[0]