
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count = {}
        result = []

        for num in nums1:
            count[num] = count.get(num, 0) + 1

        for num in nums2:
            if num in count and count[num] > 0:
                result.append(num)
                count[num] -= 1
        
        return result
    
    # Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.intersect([1, 2, 2, 1], [2, 2]))          # Expected output: [2, 2]
    print(sol.intersect([4, 9, 5], [9, 4, 9, 8, 4]))    # Expected output: [9, 4]