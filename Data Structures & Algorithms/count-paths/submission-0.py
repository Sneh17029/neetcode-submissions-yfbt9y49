class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                r, c = i, j
                if i < 0:
                    r = 0
                if j < 0:
                    c = 0
                if i == 0 and j == 0:
                    continue
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[m-1][n-1]