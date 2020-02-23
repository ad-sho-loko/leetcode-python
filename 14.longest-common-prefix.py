class List:
    def __init__(self):
        pass


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        shortest = min(strs, key=len)
        for i in range(minLen):
            target = strs[0][i]
            for s in strs:
                if s[i] != target:
                    return []
        return ans

