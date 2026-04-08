class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        used = [[False]*n for _ in range(m)]        
        res = False
        k = 0
        def dfs(x, y, i):
            if i == len(word):
                return True
            if ( x < 0 or x >= m or
                y < 0 or y >= n or used[x][y] == True or word[i] != board[x][y]
                ):
                return False

            used[x][y] = True

            value = (dfs(x+1, y, i+1) or dfs(x, y+1, i+1) or
            dfs(x-1, y, i+1) or dfs(x, y-1, i+1))
            
            used[x][y] = False
            
            return value


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False