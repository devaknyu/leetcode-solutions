"""
LeetCode 278: First Bad Version
https://leetcode.com/problems/first-bad-version/

Approach:
- Find the first bad version in a sequence of versions using binary search
- API function isBadVersion(version) returns True if version is bad
- Versions after first bad are also bad (due to inheritance)

Technique: Binary Search with Boundary Condition
1. Use binary search to find boundary between good and bad versions
2. Check if current version is bad and previous is good (boundary found)
3. If current is bad, search left for earlier bad version
4. If current is good, search right for bad version

Time Complexity: O(log n)
Space Complexity: O(1)
"""

# NOTE:
# On LeetCode, isBadVersion is provided by the platform.
# This stub exists ONLY to avoid editor / linter errors in local environments.
def isBadVersion(version: int) -> bool:
    raise NotImplementedError("This function is provided by LeetCode")

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n  # Version numbers start from 1

        while l <= r:
            m = (r + l) // 2
            
            # Check if this is the first bad version
            if isBadVersion(m) and (m == 1 or not isBadVersion(m-1)):
                return m
            
            # If current version is bad, search left (including m)
            elif isBadVersion(m):
                r = m - 1
            
            # If current version is good, search right
            else:
                l = m + 1
                
        return -1  # Should never reach here if there's at least one bad version

# Example usage
if __name__ == "__main__":
    # Mock isBadVersion function for testing
    first_bad = 4
    def isBadVersion(version: int) -> bool:
        return version >= first_bad
    
    sol = Solution()
    
    # Test cases
    test_cases = [
        (5, 4),   # n=5, first bad=4
        (1, 1),   # n=1, first bad=1
        (10, 2),  # n=10, first bad=2
    ]
    
    for n, expected in test_cases:
        # Update the global first_bad for mock function
        first_bad = expected
        result = sol.firstBadVersion(n)
        status = "✓" if result == expected else "✗"
        print(f"n={n}, first bad version={result} (Expected: {expected}) {status}")