
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


# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        (1, "A"),
        (28, "AB"),
        (701, "ZY"),
        (52, "AZ"),
        (26, "Z"),
        (27, "AA"),
        (702, "ZZ"),
        (703, "AAA")
    ]
    
    for column_number, expected in test_cases:
        result = sol.convertToTitle(column_number)
        print(f"Column {column_number:3} → '{result}' (Expected: '{expected}') → {'✓' if result == expected else '✗'}")
    
    # Additional explanation
    print("\n" + "="*50)
    print("Explanation of key conversions:")
    print("1 → A (1st letter)")
    print("26 → Z (26th letter)") 
    print("27 → AA (after Z comes AA, like 9→10 in decimal)")
    print("28 → AB (next after AA)")
    print("52 → AZ (26*2 = 52)")
    print("701 → ZY (26*26 + 25 = 701)")
    print("702 → ZZ (26*26 + 26 = 702)")