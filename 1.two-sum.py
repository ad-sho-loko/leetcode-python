class List:
    def __init__(self):
        pass


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = map()
        for i in len(nums):
            if abs(target - nums[i]) in numbers.keys():
                return [numbers[i], i]
            numbers[nums[i]] = i
