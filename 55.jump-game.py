class List:
    def __init__(self):
        pass

# DP解にならないのはn個先にしか飛べないのではなく、
# n個先までであれば好きに移動できるため、
# 最大の飛べるところまでを記録し続けていけば良い
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i, n in enumerate(nums):
            if i > reachable:
                return False

            reachable = max(reachable, i+n)

        return True
