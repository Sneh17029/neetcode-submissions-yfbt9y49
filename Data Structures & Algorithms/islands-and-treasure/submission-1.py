class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r, c = len(grid), len(grid[0])
        q = deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    q.append((i, j))
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        INF = 2147483647
        while q:
            n = len(q)
            for _ in range(n):
                x, y = q.popleft()
                for i, j in d:
                    xc = x + i
                    yc = y + j
                    if 0 <= xc < r and 0 <= yc < c and grid[xc][yc] == INF:
                        grid[xc][yc] = grid[x][y] + 1
                        q.append((xc, yc))