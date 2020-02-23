class List:
    def __init__(self):
        pass

class Solution:
    table = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        ans = []

        def inner(s:str, digits:str, ans:List[str]):
            if digits == "":
                ans.append(s)
                return

            for c in self.table[digits[0]]:
                inner(s + c, digits[1:])

        inner("", digits, ans)
        return ans
