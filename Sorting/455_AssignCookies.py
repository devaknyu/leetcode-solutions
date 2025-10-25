class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0

        while i < len(g):
            while j < len(s) and g[i] > s[j]:
                j += 1
            if j < len(s):
                i += 1
                j += 1
            else:
                break
        return i

# Example usage
    if __name__ == "__main__":
        sol = Solution()
        print(sol.findContentChildren([1, 2, 3], [1, 1]))   # Expected output: 1
        print(sol.findContentChildren([1, 2], [1, 2, 3]))   # Expected output: 2
        print(sol.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))  # Expected output: 2