class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        memo = {}
        mx = 0

        for i, ch in enumerate(s):
            if ch in memo:
                start = max(memo[ch] + 1, start)

            mx = max(mx, i - start + 1)
            memo[ch] = i

        return mx

