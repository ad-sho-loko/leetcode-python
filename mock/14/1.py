import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        majority = math.ceil(len(nums) / 2)

        for n in nums:
            if n not in m:
                m[n] = 1
            else:
                m[n] += 1

            if m[n] == majority:
                return n

        return -1
