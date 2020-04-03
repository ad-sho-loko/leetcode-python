class Solution:

    # 初期の解答.
    # 美しくないのはループ条件があらゆる箇所に伝播するということ
    # i+2対策として番兵をおいた点はよいとはおもう
    def simplifyPath(self, path: str) -> str:
        stack = []
        path += "//"
        i = 0

        while i < len(path):
            while i < len(path) and path[i] == "/":
                i += 1

            if i == len(path):
                break

            if path[i] == "." and path[i+1] == "/":
                i += 1
                continue

            if path[i] == "." and path[i+1] == ".":
                if len(stack) != 0:
                        stack.pop()
                i += 2
                continue

            s = ""
            while i < len(path) and path[i] != "/":
                s += path[i]
                i += 1

            if i == len(path):
                break

            stack.append(s)

        if len(stack) == 0:
            return "/"

        return "/" + "/".join(stack)
