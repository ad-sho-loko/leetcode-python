class List:
    def __init__(self):
        pass


# 再帰関数は今回のように最終的にリストにするタイプに弱かったりする
# そのときは終了条件(n==0)において副作用をもたせることで解決させる
# フィボナッチ数列などは最終的に「集約」するので戻り値が一つで済むので簡単
# 今回は戻り値が複数あるパターンなのでグローバルにリストをもたせてそこに格納する。

# 不変条件
# 1. 左括弧の数は右括弧の数は最終的には等しい
# 2. 左括弧の数を右括弧の数が追い抜くことはない(left >= right)
# 3. 左括弧の数はNより多くはならない (left <= N)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def generate(S, left, right):
            if len(S) == n * 2:
                answer.append(S)
                return

            if left < n:
                generate(S+"(", left+1, right)
            if right < left:
                generate(S+")", left, right+1)

        generate("", 0, 0)
        return answer
