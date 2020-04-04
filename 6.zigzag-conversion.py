class Solution:
    def convert(self, s: str, numRows: int) -> str:
        buf = [[] for _ in range(numRows)]
        bi = 0
        step = 1

        for ch in s:
            buf[bi].append(ch)
            bi += step

            if bi < 0:
                bi = 1
                step = 1

            if bi == numRows:
                bi = numRows - 1
                step = -1

        ans = ""
        for b in buf:
            ans += "".join(b)

        return ans
