class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lenTemperatures = len(temperatures)

        res = [0] * lenTemperatures
        problemStack = [(temperatures[0], 0)]
        for currIndex in range(1, lenTemperatures):
            while (problemStack):
                # print(problemStack)####
                problem, pIndex = problemStack.pop()
                # print(f"problem {problem}, curr {temperatures[currIndex]}")####
                if problem > temperatures[currIndex]:
                    problemStack.append((problem, pIndex))
                    break
                else:
                    res[pIndex] = currIndex - pIndex
            problemStack.append((temperatures[currIndex], currIndex))

        return res