class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
                return ""
        if not s or not t:
            return ""
        l, start, end = 0, 0, len(s) + 2
        c = Counter(t)
        miss = len(t)
        for r in range(len(s)):
                if c[s[r]] > 0:
                        miss -= 1
                c[s[r]] -= 1
                while miss == 0:
                        if r - l < end - start:
                                start, end = l, r
                        c[s[l]] += 1
                        if c[s[l]] > 0:
                                miss += 1
                        l += 1
        return "" if end == len(s) + 2 else s[start:end+1]