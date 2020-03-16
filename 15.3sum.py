class List:
    def __init__(self):
        pass

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)

        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if i > 0 and nums[i] == nums[i-1]:
                    continue

                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    ans.append([nums[i] , nums[l] , nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    while l < r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif total < 0:
                    l+=1
                else:
                    r-=1

        return ans