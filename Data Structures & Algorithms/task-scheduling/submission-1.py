class Solution:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)
        heap = [-v for v in freq.values()]
        heapq.heapify(heap)
        time = 0
        while heap:
            temp = []
            for _ in range(n + 1):
                if heap:
                    f = -heapq.heappop(heap)
                    f -= 1
                    if f > 0:
                        temp.append(-f)
                time += 1
                if not heap and not temp:
                    break
            for f in temp:
                heapq.heappush(heap, f)

        return time