class Solution:
    def toLowerCase(self, str: str) -> str:
        buf = []

        for ch in str:
            ascii = ord(ch)
            if 65 <= ascii <= 90:
                buf.append(chr(ascii + 32))
            else:
                buf.append(ch)

        return "".join(buf)
