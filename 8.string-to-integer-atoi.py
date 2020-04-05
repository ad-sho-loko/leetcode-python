class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()
        if len(str) == 0:
            return 0

        isNeg = False
        if str[0] == "+":
            str = str[1:]
        elif str[0] == "-":
            str = str[1:]
            isNeg = True

        if len(str) == 0 or not str[0].isdigit():
            return 0

        ans = 0
        for ch in str:
            if not ch.isdigit():
                break

            ans = ans * 10 + int(ch)

            if ans >= 2 ** 31 and isNeg:
                return -(ans ** 31)

            if ans >= 2 ** 31 - 1 and not isNeg:
                return ans ** 31 - 1


        if isNeg:
            return -ans

        return ans
