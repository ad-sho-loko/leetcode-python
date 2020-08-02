class Solution:
    # これはOK
    def dfs(self, nums, now, answer):
        answer.append(now)

        for i, n in enumerate(nums):
            # 初登場時は無視せず、それ以降は無視するようにする
            if i > 0 and nums[i-1] == nums[i]:
                continue
            self.dfs(nums[i+1:], now + [n], answer)

    # これはダメ。選ぶ/選ばないの二項でやろうとすると無理になってしまう
    # この場合だと重複を削除した場合の結果と同じになる（一度Setにしたパターン）
    def dfs_notgood(self, nums, now, answer):
        if len(nums) == 0:
            answer.append(now)
            return

        if len(nums) == 1 or nums[0] != nums[1]:
            self.dfs(nums[1:], now + [nums[0]], answer)

        self.dfs(nums[1:], now, answer)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # ソートすることで重複する要素が隣り同士になるのがポイント
        nums.sort()
        answer = []
        self.dfs(nums, [], answer)
        return answer

