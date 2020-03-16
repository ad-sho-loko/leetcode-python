class List:
    def __init__(self):
        pass

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = 0
        diff_min = 99999
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                diff = abs(target-total)

                if diff_min > diff:
                    diff_min = diff
                    ans = total

                if total > target:
                    r -= 1
                else:
                    l += 1

        return ans

