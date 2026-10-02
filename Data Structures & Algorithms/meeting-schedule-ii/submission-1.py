"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s = [i.start for i in intervals]
        e = [i.end for i in intervals]
        s.sort()
        e.sort()
        rooms = 0
        curr = 0
        i, j = 0, 0
        while i<len(s) and j<len(e):
            if s[i] < e[j]:
                curr += 1
                rooms = max(curr, rooms)
                i += 1
            else:
                curr -= 1
                j += 1
        return rooms