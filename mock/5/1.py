class Solution:
    answer = []

    # あまり美しくはないけど、こうする他ない。
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