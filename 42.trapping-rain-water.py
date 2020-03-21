class List:
    def __init__(self, x):
        pass


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left = -1
        for i, h in enumerate(height):
            if h > 0:
                left = i
                break

        if left == -1:
            return 0


