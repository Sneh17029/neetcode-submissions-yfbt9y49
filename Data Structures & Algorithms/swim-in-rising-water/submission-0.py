class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        min_heap = [(grid[0][0], 0, 0)]
        r, c = len(grid), len(grid[0])
        curr = 0
        visited = set()
        while min_heap:
            v, x, y = heapq.heappop(min_heap)
            if (x, y) in visited:
                continue
            visited.add((x,y))
            curr = max(curr, v)
            if x == r-1 and y == c-1:
                break
            for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx = x + i
                ny = y + j
                if 0<=nx<r and 0<=ny<c:
                    heapq.heappush(min_heap, (grid[nx][ny], nx, ny))
        return curr