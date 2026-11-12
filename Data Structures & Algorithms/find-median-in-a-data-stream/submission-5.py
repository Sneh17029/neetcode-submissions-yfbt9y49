import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # Max heap (smaller half)
        self.large = []  # Min heap (larger half)

    def addNum(self, num: int) -> None:

        # Add to max heap
        heapq.heappush(self.small, -num)

        # Move largest element of small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Balance the heaps
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            return -self.small[0]

        return (-self.small[0] + self.large[0]) / 2