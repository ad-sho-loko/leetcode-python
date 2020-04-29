class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        m = {}
        ans = 0
        for t in time:
            if t % 60 == 0:
                ans += m[0]

            if 60 - t % 60 in m:
                ans += m[60 - t % 60]

            if t % 60 not in m:
                m[t % 60] = 1
            else:
                m[t % 60] += 1

        return ans

