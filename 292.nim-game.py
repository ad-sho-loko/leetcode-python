class Solution:
    # Nimには必勝法がある.
    # https://mathtrain.jp/nim
    # 各山の石の数を2進数で表したとき，各桁の和が全て偶数である状態
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
