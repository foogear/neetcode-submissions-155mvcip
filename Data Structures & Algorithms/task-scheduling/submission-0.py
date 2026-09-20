class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        gap = n

        countTask = {}
        for t in tasks:
            if t not in countTask:
                countTask[t] = 0
            countTask[t] += 1

        maxHeap = []
        for task in countTask:
            amount = -countTask[task]
            heapq.heappush(maxHeap, (amount, task))


        print(maxHeap)##
        totalTime = 0
        totalGap  = 0
        while maxHeap:

            print("new gap")
            print("**************")
            
            amount, task = heapq.heappop(maxHeap)
            maxAmount = -amount
            
            totalGap  = n * (maxAmount - 1)
            totalTime += totalGap + maxAmount
            print(f"totalGap {totalGap}, totalTime{totalTime}")

            print("fill gap")
            while totalGap and maxHeap:
                amount, task = heapq.heappop(maxHeap)
                taskAmount = -amount

                if taskAmount == maxAmount:
                    totalTime += 1
                    totalGap -= (taskAmount - 1)
                else:
                    totalGap -= taskAmount
                print(f"totalGap {totalGap}, totalTime {totalTime}")


        return totalTime