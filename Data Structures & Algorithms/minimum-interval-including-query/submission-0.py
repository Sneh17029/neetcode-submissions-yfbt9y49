class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minheap = []
        intervals.sort()
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and q >= intervals[i][0]:
                s, e = intervals[i][0], intervals[i][1]
                l = e - s + 1
                heapq.heappush(minheap, (l, e))
                i += 1
            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
            if minheap:
                res[q] = minheap[0][0]
            else:
                res[q] = -1
        return [res[q] for q in queries]