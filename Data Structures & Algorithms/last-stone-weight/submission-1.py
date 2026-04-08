class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            v1 = -heapq.heappop(heap)
            v2 = -heapq.heappop(heap)
            if v1 == v2:
                continue
            heapq.heappush(heap, -(v1-v2))
        return -heapq.heappop(heap) if heap else 0