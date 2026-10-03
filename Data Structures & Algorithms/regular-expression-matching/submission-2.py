class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[None] * (len(p)+1) for _ in range(len(s) + 1)]
        def dfs(i, j):
            if dp[i][j] != None:
                return dp[i][j]
            if j == len(p):
                dp[i][j] = i == len(s)
                return dp[i][j]
            first_match = False
            if i < len(s) and (s[i] == p[j] or p[j] == "."):
                first_match = True
            if j + 1 < len(p) and p[j + 1] == '*':
                dp[i][j] = (
                    dfs(i, j + 2)
                    or
                    (first_match and dfs(i + 1, j))
                )
            else:
                dp[i][j] = first_match and dfs(i + 1, j + 1)
            return dp[i][j]
        return dfs(0, 0)
