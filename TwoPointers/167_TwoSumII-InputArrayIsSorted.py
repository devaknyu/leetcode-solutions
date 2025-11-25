from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            current_sum = numbers[l] + numbers[r]
            if current_sum == target:
                return [l + 1, r + 1]  # 1-based indices
            elif current_sum > target:
                r -= 1
            else:  # current_sum < target
                l += 1
        return []


# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9),   # → [1, 2]
        ([2, 3, 4], 6),        # → [1, 3]
        ([-1, 0], -1),         # → [1, 2]
        ([1, 2, 3, 4], 7),     # → [3, 4]
    ]
    
    for numbers, target in test_cases:
        print(f"numbers={numbers}, target={target}")
        result = sol.twoSum(numbers, target)
        print(f"Output: {result}\n")