class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0

        for c in s.[::-1]:
            if c == " ":
                break
            count += 1

        return count
