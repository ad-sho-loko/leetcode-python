class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        dp = [[False for i in range(length)] for i in range(length)]
        res = ""
        i = length - 1
        while i >= 0:
            j = i
            while j < length:
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i - 1][j + 1])

                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j+1]

                j+=1
            i-=1

        return res
