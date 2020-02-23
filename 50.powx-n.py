class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n == 1:
            return x

        # 負の数の場合は一度だけを割る。
        if n < 0:
            return 1 / self.myPow(x, -n)

        # 指数が奇数の場合は偶数に丸める
        if n % 2 == 1:
            return x * self.myPow(x * x, n // 2)

        return self.myPow(x * x, n // 2)

