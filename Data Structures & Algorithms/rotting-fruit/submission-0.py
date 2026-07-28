class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        minutes = 0
        isMinutes = False
        while q:
            n = len(q)
            for _ in range(n):
                x, y = q.popleft()
                for i in directions:
                    xc = x + i[0]
                    yc = y + i[1]
                    if 0 <= xc < r and 0 <= yc < c and grid[xc][yc] == 1:
                        grid[xc][yc] = 2
                        isMinutes = True
                        fresh -= 1
                        q.append((xc, yc))
            if isMinutes:
                minutes += 1
                isMinutes = False
        return minutes if fresh == 0 else -1