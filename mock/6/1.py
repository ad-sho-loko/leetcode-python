class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) <= 2:
            return nums.count(target) > 0

        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            if nums[left] <= nums[right]:
                return self.bsearch(nums, target)

            if nums[left] > nums[mid]:
                if self.bsearch(nums[mid:right+1], target):
                    return True

                right = mid - 1
                continue

            if nums[left] <= target <= nums[mid]:
                return self.bsearch(nums[left:mid], target)

            if target < nums[left]:
                right = mid - 1
            else:
                left = mid + 1

        mid = (left + right) // 2
        if nums[mid] == target:
            return True

        return False

    def bsearch(self, nums: List[int], target: int) -> bool:
        left = -1
        right = len(nums)

        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            if nums[mid] < target:
                left = mid
            else:
                right = mid

        return False

