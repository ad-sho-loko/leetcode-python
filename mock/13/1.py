class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        for n in range(10000):
            if pow(4, n) == num:
                return True

        return False
