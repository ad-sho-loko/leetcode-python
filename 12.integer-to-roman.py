class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        thousand = num // 1000
        hundred = (num - thousand * 1000) // 100                  # num % 1000で
        ten = (num - thousand * 1000 - hundred * 100) // 10       # (num % 100) / 10でOk
        one = (num - thousand * 1000 - hundred * 100 - ten * 10)

        for i in range(thousand):
            ans += "M"

        ans += hundreds[hundred]
        ans += tens[ten]
        ans += ones[one]

        return ans
