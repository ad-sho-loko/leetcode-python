class Solution:
    # n段目の答えはn-1段目とn-2段目の答えの加算になること
    # 0,1,2段目は答えが確定していること
    # 上記を利用できるかがポイント
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
