class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum_S, sum_T = 0, 0
        for i in s:
            sum_S += ord(i)
        for i in t:
            sum_T += ord(i)
        return chr(sum_T - sum_S)

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheDifference("abcd", "abcde"))  # Expected output: "e"
    print(sol.findTheDifference("", "y"))           # Expected output: "y"
    print(sol.findTheDifference("a", "aa"))         # Expected output: "a"