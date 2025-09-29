class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length, i = 0, len(s) - 1

        # Skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        # Count characters of the last word
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length
    
    # Example tests
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLastWord("Hello World"))  # Expected 5
    print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # Expected 4
    print(sol.lengthOfLastWord("luffy is still joyboy"))  # Expected 6