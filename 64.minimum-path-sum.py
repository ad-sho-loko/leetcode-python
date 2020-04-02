class List:
    def __init__(self):
        pass

# ☆
class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in grid[0]] for _ in grid]
        nrow = len(grid)
        ncol = len(grid[0])

        dp[0][0] = grid[0][0]
        for i in range(1, nrow):
            dp[i][0] = grid[i][0] + dp[i-1][0]

        for j in range(1, ncol):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        for i in range(1, nrow):
            for j in range(1, ncol):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[nrow-1][ncol-1]

    # 以下、幅優先探索はおそすぎる。
    # この問題は数学の組み合わせのやつと似ていることにきづけるか
    def minPathSumDfs(self, grid: List[List[int]]) -> int:
        q = queue.Queue()
        q.put((0, 0, 0))

        i = 0
        j = 0
        ans = 999

        while not q.empty():
            i, j, cost = q.get()
            cost += grid[i][j]

            if i + 1 < len(grid):
                q.put((i+1, j, cost))

            if j + 1 < len(grid[0]):
                q.put((i, j+1, cost))

            if i + 1 == len(grid) and j + 1 == len(grid[0]):
                ans = min(ans, cost)

        return ans
