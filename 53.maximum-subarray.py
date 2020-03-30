class List:
    def __init__(self):
        pass

# 良い問題
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for i in nums]
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            v = nums[i]
            if dp[i-1] >= 0:
                v += dp[i-1]
            dp[i] = v

        return max(dp)
