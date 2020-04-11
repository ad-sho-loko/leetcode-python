class List:
    def __init__(self):
        pass

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sort_nums = sorted(nums)
        length = len(nums)
        ans = []

        for i in range(length-3):
            for j in range(i+1, length-2):
                left = j + 1
                right = length - 1
                while left < right:
                    total = sort_nums[i] + sort_nums[j] + sort_nums[left] + sort_nums[right]

                    if total == target:
                        ans.append([sort_nums[i], sort_nums[j], sort_nums[left], sort_nums[right]])

                        left += 1
                        right -= 1

                        while left < right and sort_nums[left] == sort_nums[left-1] :
                            left += 1
                        while left < right and sort_nums[right] == sort_nums[right+1] :
                            right -= 1

                    elif total > target:
                        right -= 1
                    else:
                        left += 1

        return ans
