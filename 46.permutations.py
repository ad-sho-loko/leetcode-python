class List:
    def __init__(self):
        pass

# 78.subsetも参照

# Recursive
class Solution:
    ans = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, array):
            if len(nums) == 0:
                self.ans.append(array)
                return


        self.backtrack(nums, [])
        return self.ans
