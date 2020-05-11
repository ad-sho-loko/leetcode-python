class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = -1
        high = len(nums)

        while high - low > 1:
            mid = (low + high) // 2
            if nums[mid] == target:
                left = mid
                while left - 1 >= 0 and nums[left-1] == nums[left]:
                    left -= 1

                right = mid
                while right + 1 < len(nums) and nums[right+1] == nums[right]:
                    right += 1

                return [left, right]

            elif nums[mid] > target:
                high = mid
            else:
                low = mid

        return [-1, -1]
