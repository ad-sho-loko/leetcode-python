class Solution:
    # return s.count('A') <= 1 and s.count('LLL') == 0
    def checkRecord(self, s: str) -> bool:
        a = 0
        l = 0
        for ch in s:
            if ch == "A":
                a += 1
                if a > 1:
                    return False

            if ch == "L":
                l += 1
                if l > 2:
                    return False
            else:
                l = 0

        return True