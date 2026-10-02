class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        i = 0
        c = 0
        curr = intervals[0][1]
        while i < len(intervals) - 1:
            if curr <= intervals[i+1][0]:
                curr = intervals[i+1][1]
                i += 1
            else:
                i += 1
                c += 1
        return c