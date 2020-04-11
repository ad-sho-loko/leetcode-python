class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0] * n] * n



    # ダメなやつ
    def minScoreTriangulation_ダメ(self, A: List[int]) -> int:
        n = len(A)
        mins = 2 ** 31

        for i in range(n):
            s = 0
            for cnt in range(n - 2):
                j = (i + cnt + 1) % n
                k = (i + cnt + 2) % n
                s += A[i] * A[j] * A[k]
            mins = min(mins, s)

        return mins
