class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:



        mostFrontHeap = []
        numGroup = 1

        for i in range(len(position)):
            p, s = -position[i], speed[i]
            heapq.heappush(mostFrontHeap, (p, s))

        while len(mostFrontHeap) > 1:
            #print()
            #print(f"numGroup {numGroup}")
            front, fSpeed  = heapq.heappop(mostFrontHeap)
            front  *= -1
            # behind, bSpeed = heapq.heappop(mostFrontHeap)
            behind, bSpeed = mostFrontHeap[0]
            behind *= -1
            #print((front, fSpeed))
            #print((behind, bSpeed))

            fFinishTime = (target - front)  / fSpeed
            bFinishTime = (target - behind) / bSpeed

            if bFinishTime <= fFinishTime:
                pass
            else:
                numGroup += 1

        return numGroup###($($($(bbjjk


    