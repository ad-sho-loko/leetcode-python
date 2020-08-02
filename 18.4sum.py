class List:
    def __init__(self):
        pass

class Solution:
    answer = []

    def two_sum(self, nums: List[int], target: int, f, s):
        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] + nums[r] == target:
                return self.answer.append((f, s, nums[l], nums[r]))

            while l+1 < len(nums) and nums[l] == nums[l+1]:
                l+=1

            while r-1 >= 0 and nums[r] == nums[r-1]:
                r-=1

            l+=1
            r-=1

    def solve(self, nums, target, f, s, N):
        if N == 2:
            return self.two_sum(nums, target, f, s)

        if N == 3:
            for i, n in enumerate(nums):
                self.solve(nums[i:], target - n, f, n, N - 1)

        if N == 4:
            for i, n in enumerate(nums):
                self.solve(nums[i:], target - n, n, s, N - 1)


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.answer = []
        sorted(nums)
        self.solve(nums, target, -1, -1, 4)
        return self.answer
