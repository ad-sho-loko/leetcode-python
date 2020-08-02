class List:
    def __init__(self):
        pass

# めっちゃ賢いパターン.途中経過のリストを利用することで倍々やる.
# 例: [1,2,3]
# [] ->
# [[],[1]] ->
# [[],[1], [2], [1,2]] -> ...
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for n in nums:
            subset += [sub + [n] for sub in subset]
        return subset


# 思いつくやつ。これのほうがマシかも。
class Solution:
    def dfs(self, nums, now, answer):
        if len(nums) == 0:
            answer.add(now)
            return

        self.dfs(nums[1:], now, answer)        # 入れない
        self.dfs(nums[1:], now + [nums[0]], answer) # 入れる

    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        self.dfs(nums, [], answer)
        return answer


# マトモなrecursive-pattern。
# ↑よりもシンプルなdfsメソッド内がシンプルになる
class Solution:
    def dfs(self, nums, now, answer):

        answer.append(now)
        for i, n in enumerate(nums):
            self.dfs(nums[i+1:], now + [n], answer)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        self.dfs(nums, [], answer)
        return answer


# recursive-pattern. フィールド値を持たないといけないのがタルい。コピーも必要。クソコード。
class Solution:
    ans = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def inner(num, array):
            if len(num) == 0:
                self.ans.append(array)
                return

            inner(num[1:], array.copy())
            array.append(num[0])
            inner(num[1:], array.copy())

        inner(nums, [])
        return self.ans
