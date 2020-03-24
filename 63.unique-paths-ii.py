class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])

        dp = [[0 for j in range(c)] for i in range(r)]

        for i in range(r):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for j in range(c):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        for i in range(1, r):
            for j in range(1, c):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[r-1][c-1]