class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        finish = target

        mostFrontHeap = []
        numGroup = 1

        for i in range(len(position)):
            p, s = position[i], speed[i]
            heapq.heappush(mostFrontHeap, (-p, p, s))

        #print(mostFrontHeap)

        #print("start")
        timePassed = 0
        while len(mostFrontHeap) > 1:
            frontPos,  fSpeed = heapq.heappop(mostFrontHeap)[1:]
            behindPos, bSpeed = heapq.heappop(mostFrontHeap)[1:]
            # behindPos, bSpeed = mostFrontHeap[0]
            behindPos = behindPos + (timePassed * bSpeed)

            if behindPos > frontPos:
                group = (-frontPos, frontPos, fSpeed)
                heapq.heappush(mostFrontHeap, group)
                continue

            #print()
            #print((frontPos, fSpeed))
            #print((behindPos, bSpeed))


            frontFinishTime = (finish - frontPos) / fSpeed
            if bSpeed <= fSpeed:
                catchUpTime = float("INF")
            else:
                catchUpTime = (frontPos - behindPos) / (bSpeed - fSpeed)
            
            #print(f"frontFinishTime {frontFinishTime}")
            #print(f"catchUpTime {catchUpTime}")

            if catchUpTime <= frontFinishTime:
                timePassed += catchUpTime
                groupPos   = behindPos + (catchUpTime * bSpeed)

                group = (-groupPos, groupPos, fSpeed)
                heapq.heappush(mostFrontHeap, group)
            
            else:
                numGroup += 1
                group = (-behindPos, behindPos, bSpeed)
                heapq.heappush(mostFrontHeap, group)

            #print(f"numGroup {numGroup}")
            #print(mostFrontHeap)


        #print("wtf")

        
        



        return numGroup###($($($


    