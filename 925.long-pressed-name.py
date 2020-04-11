class Solution:
    def isLongPressedName2(self, name: str, typed: str) -> bool:
        ni = 0
        ti = 0

        prev = "_"

        while ni < len(name):
            pass


    # 別解: ランレングス圧縮のような解法。アルゴリズム的には非常にシンプル。
    def isLongPressedName2(self, name: str, typed: str) -> bool:
        n = self.build(name)
        t = self.build(typed)

        if len(n) != len(t):
            return False

        i = 0
        while i < len(n) - 1:
            if n[i] != t[i]:
                return False

            if int(n[i + 1]) <= int(t[i + 1]):
                return False

            i += 2

        return True

    def build(self, s: str):
        result = []

        i = 0
        while i < len(s):
            ch = s[i]
            count = 1

            while i < len(s) - 1 and s[i] == s[i + 1]:
                count += 1
                i += 1

            result.append(ch + str(count))
            i += 1

        return "".join(result)

