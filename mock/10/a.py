# AtCoder流, 繰り返し二乗法
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.mypow(x, -n)

        ans = 1
        while n != 0:
            if n & 1:
                ans *= x

            x *= x
            n >>= 1

        return ans