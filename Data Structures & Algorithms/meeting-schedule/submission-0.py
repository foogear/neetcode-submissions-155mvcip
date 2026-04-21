"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        cal = []
        eventId = 0

        for i in intervals:
            eventId += 1
            start, end = i.start, i.end
            while len(cal) < end + 1:
                cal.append(0)
            if (cal[start] == cal[end] and
                cal[start] and cal[end]):
                return False
            for j in range(start + 1, end):
                if cal[j]:
                    return False
            for j in range(start, end + 1):
                cal[j] = eventId

        return True

