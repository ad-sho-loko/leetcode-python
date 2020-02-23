class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next = 0

        for n in nums:
            nums[next] = n
            if n == val:
                next += 1

        return next
