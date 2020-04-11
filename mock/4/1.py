class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        isOne = False

        while i < len(bits):
            isOne = bits[i] == 0
            if isOne:
                i += 1
            else:
                i += 2

        return isOne
