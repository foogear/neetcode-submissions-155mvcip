class TimeMap:

    def __init__(self):
        self.memo    = {}
        self.maxHeap = {}

        

    def set(self, key: str, value: str, timestamp):
        if key not in self.memo:
            self.memo[key]    = {}
            self.maxHeap[key] = []
        self.memo[key][timestamp] = value
        heapq.heappush(self.maxHeap[key], (-timestamp, value))



    def get(self, key: str, timestamp: int) -> str:
        if key not in self.memo:
            return ""

        if timestamp in self.memo[key]:
            return self.memo[key][timestamp]

        MAX_ONE, VALUE = 0, 1
        return self.maxHeap[key][MAX_ONE][VALUE]


        #####