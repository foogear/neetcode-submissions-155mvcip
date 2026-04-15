class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        L, R = newInterval[0], newInterval[1]
        p = {"L":None, "R":None}
        intervals = [[-2,-1]] + intervals

        for i in range(len(intervals)):
            if L >= intervals[i][0]:
                p["L"] = i
            if R >= intervals[i][0]:
                p["R"] = i
        
        mid = []

        print(p)

        leftEnd = p["L"]
        if L > intervals[p["L"]][1]:
            leftEnd += 1
            mid.append(L)
        else:
            mid.append(intervals[p["L"]][0])

        rightStart = p["R"] + 1
        if R > intervals[p["R"]][1]:
            mid.append(R)
        else:
            mid.append(intervals[p["R"]][1])

        if leftEnd == rightStart:
            return intervals[1:leftEnd] + [mid] + intervals[rightStart:]

        intervals[leftEnd] = mid
        for i in range(leftEnd + 1, rightStart):
            del intervals[leftEnd + 1]

        return intervals[1:]




