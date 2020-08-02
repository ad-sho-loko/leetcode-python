class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return nums

        l = len(nums) - 2
        while l >= 1:
            if nums[l] < nums[l + 1]:
                break
            l -= 1

        r = l
        while r < len(nums) - 1:
            if nums[l] > nums[r + 1]:
                break
            r += 1

        nums[l], nums[r] = nums[r], nums[l]
        self.rev(nums, l + 1, len(nums) - 1)

    def rev(self, nums, start, end):
        l = start
        r = end

        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1



