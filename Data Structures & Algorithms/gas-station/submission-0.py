class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        sum = 0
        index = -1
        for i in range(len(gas)):
            sum = sum + (gas[i] - cost[i])
            if sum >= 0:
                index = i


        if sum < 0:
            return -1

        return index



