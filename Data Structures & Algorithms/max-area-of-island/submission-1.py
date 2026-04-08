class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        marea = 0
        r, c = len(grid), len(grid[0])
        def dfs(ir, ic):
            nonlocal marea
            if ir<0 or ir>=r or ic<0 or ic>=c or grid[ir][ic] == 0:
                return 0
            grid[ir][ic] = 0
            return (1 + dfs(ir+1, ic)
            + dfs(ir, ic+1)
            + dfs(ir-1, ic)
            + dfs(ir, ic-1))
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    marea = max(marea, dfs(i, j))
        return marea
