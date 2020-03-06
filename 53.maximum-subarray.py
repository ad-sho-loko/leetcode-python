class List:
    def __init__(self):
        pass

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp = [-99999999 for i in nums]
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if nums[i] >= 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = max(0, nums[i] + dp[i-1])

        return dp[len(nums)-1]

