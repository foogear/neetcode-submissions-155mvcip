class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # Sorted List
        if len(intervals) < 1:
            return [newInterval]
        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0]:
                intervals = intervals[:i] + [newInterval] + intervals[i:]

        res = []
        newInterval = intervals[0]
        for i in range(1, len(intervals)):

            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                newInterval = intervals[i]

            if newInterval[1] >= intervals[i][0]:
                newInterval = [min(newInterval[0], intervals[i][0]),
                               max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res


