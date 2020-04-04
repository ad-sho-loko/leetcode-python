class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        neg = x < 0
        n = x

        if neg:
            n = -n

        while n != 0:
            ans = ans * 10 + n % 10

            # check underflow
            if neg and ans >= 2147483648:
                return -2147483648

            # check overflow
            if ans >= 2147483647:
                return 2147483647

            n //= 10

        if neg:
            return -ans

        return ans
