class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist = x*x + y*y
            heap.append((dist, x, y))
        heapq.heapify(heap)
        l = []
        for _ in range(k):
            x, y, z = heapq.heappop(heap)
            l.append([y, z])
        return l