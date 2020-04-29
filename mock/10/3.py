class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        plus = {}
        minus = {}

        sort_point = sorted(points, key = lambda x: x[0])

        for p in sort_point[0]:
            plus[p[1]] = 1
            minus[p[1]] = 1

        prev = sort_point[0][0]
        for p in sort_point[1:]:
            if prev + 1 ==p[0]:

            else:
                plus = {p[1] : 1}
                plus = {p[1] : 1}
