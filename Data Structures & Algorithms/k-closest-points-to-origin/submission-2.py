import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # it's "K" not "K-th"
        heap = []
        heapq.heapify(heap)

        for p in points:
            dis = p[0]**2 + p[1]**2
            if len(heap) <= k:
                heapq.heappush(heap, [-dis]+p)
            else:
                if dis < -heap[1][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, [-dis]+p)

        res = []
        i = len(heap) - 1
        for _ in range(k):
          # if i > 0:
                res.append([heap[i][1], heap[i][2]])
                i -= 1
              # continue 
          # break 
        
        return res