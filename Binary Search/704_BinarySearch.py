from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
                
        return -1
# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9),   # → 4
        ([-1, 0, 3, 5, 9, 12], 2),   # → -1
        ([5], 5),                     # → 0
        ([1, 3, 5, 7, 9], 1),        # → 0
    ]
    
    for nums, target in test_cases:
        print(f"nums={nums}, target={target}")
        result = sol.search(nums, target)
        print(f"Index: {result}\n")