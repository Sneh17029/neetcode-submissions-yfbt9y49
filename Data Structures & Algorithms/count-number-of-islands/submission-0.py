class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        r,c = len(grid), len(grid[0])
        def dfs(ir, ic):
            if ir<0 or ic<0 or ir>=r or ic>=c or grid[ir][ic] == '0':
                return
            grid[ir][ic] = '0'
            dfs(ir+1, ic)
            dfs(ir, ic+1)
            dfs(ir-1, ic)
            dfs(ir, ic-1)
            return
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
