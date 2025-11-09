"""
LeetCode 168: Excel Sheet Column Title
https://leetcode.com/problems/excel-sheet-column-title/

Approach:
- We need to convert a positive integer to an Excel column title (like 1→"A", 28→"AB").
- This is essentially converting a number from base 10 to base 26, but with a twist:
  - Excel columns are 1-indexed (A=1, B=2, ..., Z=26), not 0-indexed.
  - This means we need to adjust by subtracting 1 before each conversion step.

Technique: Base Conversion with Adjustment
1. While the columnNumber is greater than 0:
   - Subtract 1 from columnNumber to convert from 1-indexed to 0-indexed
   - Calculate the current character using modulo 26
   - Append the corresponding uppercase letter to the result
   - Update columnNumber using integer division by 26
2. Reverse the result string at the end since we built it from least significant to most significant digit.

Why subtract 1?
- In normal base conversion, digits range from 0 to (base-1)
- But Excel columns range from 1 to 26
- Subtracting 1 maps: 1→0 (A), 2→1 (B), ..., 26→25 (Z)

Example:
Input: 28
Process:
  Iteration 1: (28-1)=27 → 27%26=1 → 'B', (27//26)=1
  Iteration 2: (1-1)=0 → 0%26=0 → 'A', (0//26)=0
  Reverse "BA" → "AB"
Output: "AB"

Input: 701
Process:
  Iteration 1: (701-1)=700 → 700%26=24 → 'Y', (700//26)=26
  Iteration 2: (26-1)=25 → 25%26=25 → 'Z', (25//26)=0
  Reverse "ZY" → "YZ"
Output: "ZY"

Time Complexity: O(log₂₆(n)) — number of digits in base 26 representation
Space Complexity: O(log₂₆(n)) — for storing the result string
"""
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