from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        # If all digits were 9 → [9,9,9] → [1,0,0,0]
        return [1] + digits
    
    # Example run for local testing
if __name__ == "__main__":
    print(Solution().plusOne([1, 2, 3]))  # Output: [1, 2, 4]
    print(Solution().plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]