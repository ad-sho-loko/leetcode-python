class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if nums < 2:
            return nums

        r = len(nums) - 1
        while r >= 1:
            if nums[r-1] < nums[r]:
                break
            r-=1

        if r == 0:
            nums.reverse()
            return


