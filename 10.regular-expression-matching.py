class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True

        for j in range(1, len(p) + 1):
            pi = j - 1
            dp[0][j] = p[pi] == "*" and dp[0][j-2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                si = i - 1
                pi = j - 1

                if p[pi] == "*":
                    dp[i][j] = dp[i][j-2] or ((s[si] == p[pi-1] or p[pi-1] == ".") and dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j-1] and (s[si] == p[pi] or p[pi] == ".")

        return dp[len(s)][len(p)]
