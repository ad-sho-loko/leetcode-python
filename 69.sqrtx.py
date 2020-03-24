class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 0

        low = 0.0
        high = x / 2
        mid = 0.0

        for i in range(len(100)):
            mid = (low + high) // 2
            t = mid*mid
            if t == x:
                return mid

            if t > x:
                high = mid
            else:
                low = mid

        return int(mid)
