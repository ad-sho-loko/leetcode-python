class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        m = {}
        si = 0
        ei = 0
        mx = -1

        while ei < len(s):
            if s[ei] in m:
                si = max(m[s[ei]], si)

            m[s[ei]] = ei
            ei += 1
            mx = max(mx, ei - si)

        return mx

