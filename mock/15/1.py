class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        dup = set()
        i = 0

        while i < len(nums) - 2:
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    h = str(nums[i]) + str(nums[left]) + str(nums[right])
                    if h not in dup:
                        ans.append([nums[i], nums[left], nums[right]])
                        dup.add(h)
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    break

            i += 1

        return list(ans)

