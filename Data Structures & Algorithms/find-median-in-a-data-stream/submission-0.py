class MedianFinder:

    def __init__(self):
        # For smaller nums
        self.maxHeap = []
        # For bigger nums
        self.minHeap = []

    def addNum(self, num: int) -> None:
        minHeap, maxHeap = self.minHeap, self.maxHeap
        if not maxHeap:
            heapq.heappush(maxHeap, -num)
            return 
        if not minHeap:
            heapq.heappush(minHeap, num)
            return

        if num < -maxHeap[0]:
            heapq.heappush(maxHeap, -num)
        else:
            heapq.heappush(minHeap, num)

        if len(maxHeap) < len(minHeap):
            t = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -t)
        elif len(minHeap) < len(maxHeap) - 1:
            t = -heapq.heappop(maxHeap)
            heapq.heappush(minHeap, t)
            
    def findMedian(self) -> float:
        maxHeap, minHeap = self.maxHeap, self.minHeap
        if len(maxHeap) == len(minHeap):
            return (-maxHeap[0] + minHeap[0]) / 2

        return float(-maxHeap[0])


