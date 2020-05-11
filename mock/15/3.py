class Solution:
    m = {
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxxz",
    }

    ans = []

    def rec(self, digits, comb):
        if not digits and len(comb) > 0:
            self.ans.append(comb)
            return

        for ch in self.m[digits[0]]:
            self.rec(digits[1:], comb + ch)


    def letterCombinations(self, digits: str) -> List[str]:
        self.rec(digits, "")
        return self.ans
