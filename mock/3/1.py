class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        if len(heights) == 0 or len(heights) == 1:
            return 0

        cnt = 0
        for i in range(1, len(heights)):
            j = i - 1
            h = heights[i]

            changed = False
            while j >= 0:
                if heights[j] > h:
                    heights[j+1] = heights[j]
                    changed = True
                    j -= 1
                else:
                    break

            if changed:
                cnt += 1

        return cnt