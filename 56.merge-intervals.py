# まず始点でソートをすることで非常にシンプルな構成になる。
# 一つ前の終点が現在の始点より大きければオーバラップ確定なので、終点同士を比較する
# そうでなければ以前の範囲から必ず離れていることが確定される。
# ソートを行うことでシンプルな解法を導き出せるかがポイント

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        for iv in sorted(intervals, key=lambda i: i[0]):
            if out and out[-1][1] >= iv[0]:
                out[-1][1] = max(iv[1], out[-1][1])
            else:
                out.append(iv)

        return out

