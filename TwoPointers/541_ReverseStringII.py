class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        char = list(s)
        for i in range(0, len(char), 2 * k):
            l = i
            r = min(i + k - 1, len(char) - 1)
            
            while l < r:
                char[l], char[r] = char[r], char[l]
                l += 1
                r -= 1
        return ''.join(char)

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ("abcdefg", 2),    # → "bacdfeg"
        ("abcd", 2),       # → "bacd"
        ("abc", 2),        # → "bac"
        ("a", 2),          # → "a"
        ("abcdef", 3),     # → "cbadef"
    ]
    
    for s, k in test_cases:
        print(f"Input:  s='{s}', k={k}")
        result = sol.reverseStr(s, k)
        print(f"Output: '{result}'\n")