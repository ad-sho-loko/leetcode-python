class Solution:
    def myAtoi(self, str: str) -> int:
        digit_str = str.lstrip()
        isNeg = False
        if len(digit_str) == 0:
            return 0

        if digit_str[0] == "+":
            digit_str = digit_str[1:]
        elif digit_str[0] == "-":
            digit_str = digit_str[1:]
            isNeg = True

        ans = 0
        for i in range(len(digit_str)):
            if not digit_str[i].isdigit():
                break

            ans = ans * 10 + int(digit_str[i])

            # check overflow/underflow
            if ans >= 2 ** 31:
                if isNeg:
                    return -2 ** 31
                else:
                    return 2 ** 31 - 1

        if isNeg:
            ans = -ans

        return ans
