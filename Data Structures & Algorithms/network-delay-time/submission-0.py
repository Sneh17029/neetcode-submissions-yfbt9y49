class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        s = set()
        m = defaultdict(list)
        for i in range(len(times)):
            m[times[i][0]].append((times[i][1], times[i][2]))
        curr = [(0, k)]
        shortest = {}
        while curr:
            time, node = heapq.heappop(curr)
            if node in shortest:
                continue
            shortest[node] = time
            if len(shortest) == n:
                return time
            for ele, t in m[node]:
                if ele not in shortest:
                    heapq.heappush(curr, [t+time, ele])
        return -1