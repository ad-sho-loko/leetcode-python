class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digits = [0 for i in range(300)]

        start = 0
        for i in num2[::-1]:
            dg = start

            for j in num1[::-1]:
                ii = int(i)
                jj = int(j)
                t = ii * jj
                carry = t // 10
                value = t % 10
                if digits[dg] + value >= 10:
                    digits[dg+1] += 1
                    value -= 10
                digits[dg] += value

                if digits[dg+1] >= 10 or digits[dg+1] + carry >= 10:
                    digits[dg+2] += 1
                    digits[dg+1] -= 10

                digits[dg+1] += carry
                dg += 1

            start += 1

        return  "".join(map(str, reversed(digits))).lstrip("0")




