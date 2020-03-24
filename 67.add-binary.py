class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0: return b
        if len(b) == 0: return a

        if a[-1] == "0" and b[-1] == "0":
            return self.addBinary(a[0:-1], b[0:-1]) + "0"
        elif a[-1] == "1" and b[-1] == "1":
            # 両方とも１の場合は、次の桁に１を加算してあげればよい。
            # 現在の桁は"0"を末尾に挿入するだけで良い。
            # 仮にaddBinaryが３引数取るなら、addBinary(a[0:-1], b[0:-1], "1") + "0"
            return self.addBinary(self.addBinary(a[0:-1], "1"), b[0:-1]) + "0"
        else:
            return self.addBinary(a[0:-1], b[0:-1]) + "1"
