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
