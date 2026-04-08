class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []
        def dfs(start):
            if start == len(s):
                res.append(sub[:])
                return
            for i in range(start + 1, len(s) + 1):
                st = s[start:i]
                if st == st[::-1]:
                    sub.append(st)
                    dfs(i)
                    sub.pop()
        dfs(0)
        return res