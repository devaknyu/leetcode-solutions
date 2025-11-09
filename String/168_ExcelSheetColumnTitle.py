
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            # Adjust for 1-indexing and get current character
            offset = (columnNumber - 1) % 26
            res += chr(ord('A') + offset)
            # Move to next more significant digit
            columnNumber = (columnNumber - 1) // 26
        return res[::-1]  # Reverse to get correct order