class List:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    ans = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        for i in range(len(candidates)):
            self.dfs(candidates, [], i, target)

        return self.ans

    def dfs(self, candidates: List[int], selected: List[int], i:int, target:int):
        if target < 0:
            return

        if target == 0:
            self.ans.append(selected)
            return

        if i >= len(candidates):
            return

        self.dfs(candidates[1:], selected + [candidates[i]], i, target - candidates[i])
        self.dfs(candidates[1:], selected + [candidates[i]], i+1, target)
