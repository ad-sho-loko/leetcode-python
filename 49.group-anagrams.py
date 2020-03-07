class List:
    def __init__(self):
        pass

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            sort_str = "".join(sorted(s))
            if sort_str not in anagrams.keys():
                anagrams[sort_str] = []
            anagrams[sort_str].append(s)

        ans = []
        for v in anagrams.values():
            ans.append(v)

        return ans
