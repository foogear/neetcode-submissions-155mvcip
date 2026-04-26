from _heapq import heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1

        # Review
        heap = []
        for i in count:
            if len(heap) < k:
                heapq.heappush(heap, i)
                print(heap)
                continue
            if count[heap[0]] < count[i]:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
                print(heap)
                continue

        return heap
            

