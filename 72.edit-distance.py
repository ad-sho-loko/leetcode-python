class Solution:
    # https://nw.tsuda.ac.jp/lec/EditDistance/
    # 最小コストだけであれば、上記サイトのコスト表だけで十分。
    # どのような走査をしたかが必要であれば、上記サイトの操作表が必要になる。
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        costs = [[0] * m + 1 for _ in range(n+1)]

        for i in range(n + 1):
            costs[i][0] = i

        for i in range(m + 1):
            costs[0][i] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                c = costs[i - 1][j - 1] + 1
                if word1[i - 1] == word2[j - 1]:
                    c = costs[i - 1][j - 1]
                costs[i][j] = min(costs[i - 1][j] + 1, costs[i][j - 1] + 1, c)

        return costs[n][m]
