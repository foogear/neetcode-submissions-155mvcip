class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        finish = target

        mostFrontHeap = []
        for i in range(len(position)):
            p, s = position[i], speed[i]
            heapq.heappush(mostFrontHeap, (-p, p, s))

        numGroup = 1
        timePassed = 0
        while len(mostFrontHeap) > 1:
            frontPos,  fSpeed = heapq.heappop(mostFrontHeap)[1:]
            
            behindPos, bSpeed = heapq.heappop(mostFrontHeap)[1:]
            behindPos = behindPos + (timePassed * bSpeed)

            if behindPos > frontPos:
                group = (-frontPos, frontPos, fSpeed)
                heapq.heappush(mostFrontHeap, group)
                continue

            frontFinishTime = (finish - frontPos) / fSpeed
            if bSpeed <= fSpeed:
                catchUpTime = float("INF")
            else:
                catchUpTime = (frontPos - behindPos) / (bSpeed - fSpeed)

            if catchUpTime <= frontFinishTime:
                timePassed += catchUpTime
                groupPos   = behindPos + (catchUpTime * bSpeed)

                group = (-groupPos, groupPos, fSpeed)
                heapq.heappush(mostFrontHeap, group)
            else:
                numGroup += 1

                group = (-behindPos, behindPos, bSpeed)
                heapq.heappush(mostFrontHeap, group)
                
        return numGroup