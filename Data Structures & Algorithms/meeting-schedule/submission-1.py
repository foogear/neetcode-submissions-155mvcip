"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            intervals[i] = (start, end)
        intervals = sorted(intervals)
        for i in range(1, len(intervals)):
            leftEnd, rightStart = intervals[i - 1][1], intervals[i][0]
            if leftEnd > rightStart:
                return False 
        return True 


