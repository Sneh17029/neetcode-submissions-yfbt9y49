class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r, c = len(board), len(board[0])
        q = deque()
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O' and (i == 0 or i == r-1 or j == 0 or j == c - 1):
                    q.append((i, j))
                    board[i][j] = 'T'
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            n = len(q)
            for _ in range(n):
                x, y = q.popleft()
                for i, j in direction:
                    xc = x + i
                    yc = y + j
                    if 0 <= xc < r and 0 <= yc < c and board[xc][yc] == 'O':
                        board[xc][yc] = 'T'
                        q.append((xc, yc))
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
