class List:
    def __init__(self):
        pass

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0:
                return

            if i >= len(grid) or j >= len(grid[0]):
                return

            if grid[i][j] == "0":
                return

            grid[i][j] = "0"
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    ans += 1
                    dfs(r, c)

        return ans

