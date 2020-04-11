class Solution:
    answer = []

    # 1,あまり美しくはないけど...
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(tmp: List[int]):
            if len(tmp) == len(nums):
                t = tmp.copy()
                self.answer.append(t)
            else:
                for n in nums:
                    if tmp.count(n) != 0:
                        continue

                    tmp.append(n)
                    backtrack(tmp)
                    tmp.remove(n)

        self.answer = []
        backtrack([])
        return self.answer

# pythonならでは. しかも↑よりは早い。
class Solution2:
    def __init__(self):
        self.answer = []

    # DFS
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums: List[int], path:List[int]):
            if not nums:
                self.answer.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]])

        dfs(nums, [])
        return self.answer

