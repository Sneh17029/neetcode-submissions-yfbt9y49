class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            res = 1
            for a,b in directions:
                x, y = i+a, j+b
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                    if matrix[x][y] > matrix[i][j]:
                        res = max(1+ dfs(x, y), res)
            dp[(i, j)] = res
            return res
        val = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val = max(val, dfs(i, j))
        return val