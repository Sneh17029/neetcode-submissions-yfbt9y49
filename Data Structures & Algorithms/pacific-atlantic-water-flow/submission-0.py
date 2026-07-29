class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r, c = len(heights), len(heights[0])
        pq, resp = deque(), set()
        aq, resa = deque(), set()
        for i in range(r):
            for j in range(c):
                if i == 0 or j == 0:
                    pq.append((i, j))
                    resp.add((i, j))
                if i == r-1 or j == c-1:
                    aq.append((i, j))
                    resa.add((i, j))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while pq:
            x, y = pq.popleft()
            for a, b in directions:
                xc = x + a
                yc = y + b
                if 0<=xc<r and 0<=yc<c and heights[xc][yc] >= heights[x][y] and (xc, yc) not in resp:
                    pq.append((xc, yc))
                    resp.add((xc, yc))
        while aq:
            x, y = aq.popleft()
            for a, b in directions:
                xc = x + a
                yc = y + b
                if 0<=xc<r and 0<=yc<c and heights[xc][yc] >= heights[x][y] and (xc, yc) not in resa:
                    aq.append((xc, yc))
                    resa.add((xc, yc))
        return list(resp & resa)