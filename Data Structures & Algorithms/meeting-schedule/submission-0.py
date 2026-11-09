"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)

        for i in range(1, len(intervals)):
            base = intervals[i - 1]
            nxt = intervals[i]

            if base.end > nxt.start:
                return False
        return True

        # startの時間でソートして、前のend <= 次のstartが成立したらTrue, otherwise false
        # 考え方は初めから導き出せた