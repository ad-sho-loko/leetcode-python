class List:
    def __init__(self):
        pass


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        low = -1
        high = len(nums)
        mid = 0
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                break

            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1

        if low >= high:
            return [-1, -1]

        left = mid
        right = mid
        while left > 1:
            if nums[left-1] != target:
                break
            left-=1
        while right < len(nums) - 1:
            if nums[right+1] != target:
                break
            right+=1


        return [left, right]

