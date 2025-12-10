from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2

            if nums[m] == target:
                return m
            
            # Left half is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            # Right half is sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
                    
        return -1

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0),   # → 4
        ([4, 5, 6, 7, 0, 1, 2], 3),   # → -1
        ([1], 0),                      # → -1
        ([1], 1),                      # → 0
        ([1, 3], 3),                   # → 1
    ]
    
    for nums, target in test_cases:
        print(f"Array: {nums}, Target: {target}")
        result = sol.search(nums, target)
        print(f"Index: {result}\n")