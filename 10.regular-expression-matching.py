class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.inner(s, p, 0, 0)

    def inner(self, s: str, p: str, si: int, pi: int):
        while si < len(s) and pi < len(p):
            if pi + 1 < len(p):
                if p[pi + 1] == "*":
                    if self.star(s, p, si, pi):
                        return True

            if p[pi] != "." and s[si] != p[pi]:
                return False

            si += 1
            pi += 1

        while pi + 1 < len(p):
            pi += 2

        return si == len(s) and pi == len(p)

    def star(self, s: str, p: str, si: int, pi: int):
        while si < len(s) and (p[pi] == "." or s[si] == p[pi]):
            if self.inner(s, p, si, pi + 2):
                return True
            si += 1

        return self.inner(s, p, si, pi + 2)
