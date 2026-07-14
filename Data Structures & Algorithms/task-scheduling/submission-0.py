class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        m = 0
        count = 0
        t = 0
        for i,v in c.items():
            t += v
            if m>v:
                continue
            if m == v:
                count += 1
                continue
            m = max(m, v)
            count = 1
        return max(t, (m-1)*(n+1) + count)