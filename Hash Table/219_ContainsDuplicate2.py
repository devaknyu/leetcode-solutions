
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))   # Expected output: True
    print(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))   # Expected output: True
    print(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # Expected output: False