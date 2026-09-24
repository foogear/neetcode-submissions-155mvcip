class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        finish = target

###(_(_(($($)))))

        mostFrontHeap = []
        numGroup = 1

        for i in range(len(position)):
            p, s = -position[i], speed[i]
            heapq.heappush(mostFrontHeap, (p, s))

        print(mostFrontHeap)

        print("start")
        timePassed = 0
        while mostFrontHeap:
            frontPos,  fSpeed = heapq.heappop(mostFrontHeap)
            frontPos *= -1
            behindPos, bSpeed = mostFrontHeap[0]
            behindPos *= -1
            behindPos = behindPos + (timePassed * bSpeed)

            
            if behindPos > frontPos:
                frontPos *= -1
                mostFrontHeap[0] = (frontPos, fSpeed)
                continue

            print()
            print((frontPos, fSpeed))
            print((behindPos, bSpeed))


            frontFinishTime = (finish - frontPos) / fSpeed
            if bSpeed <= fSpeed:
                catchUpTime = float("INF")
            else:
                catchUpTime = (frontPos - behindPos) / (bSpeed - fSpeed)
            
            print(f"frontFinishTime {frontFinishTime}")
            print(f"catchUpTime {catchUpTime}")

            if catchUpTime <= frontFinishTime:
                timePassed += catchUpTime
                groupPos   = behindPos + (catchUpTime * bSpeed)
                groupSpeed = fSpeed

                groupPos *= -1
                mostFrontHeap[0] = (groupPos, groupSpeed)
            else:
                numGroup += 1

            print(f"numGroup {numGroup}")
            print(mostFrontHeap)


        print("wtf")

        
        



        return numGroup###($($($


    