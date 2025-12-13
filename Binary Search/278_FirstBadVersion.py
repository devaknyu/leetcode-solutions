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