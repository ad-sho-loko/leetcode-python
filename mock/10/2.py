class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [-1] * 201
        def f(n):
            if n == 1:
                return 1

            if memo[n] != -1:
                return memo[n]

            memo[n] = n * f(n-1)
            return memo[n]

        return f(m+n) // (f(m) * f(n))
