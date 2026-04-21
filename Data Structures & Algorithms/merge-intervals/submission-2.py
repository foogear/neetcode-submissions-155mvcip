class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals)

        if len(intervals) < 2:
            return intervals

        res = []
        newInterval = intervals[0]

        for i in range(1, len(intervals)):

            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                newInterval = intervals[i]
                continue

            leftEnd, rightStart = newInterval[1], intervals[i][0]
            if leftEnd >= rightStart:
                newInterval = [min(newInterval[0], intervals[i][0]),
                               max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res






