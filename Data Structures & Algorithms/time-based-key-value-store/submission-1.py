class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        v = self.m[key]
        l, r = 0, len(v) - 1
        ans = -1
        while l<=r:
            m = l + (r-l)//2
            if v[m][0] <= timestamp:
                l = m + 1
                ans = m
            else:
                r = m - 1
        return "" if ans == -1 else v[ans][1]