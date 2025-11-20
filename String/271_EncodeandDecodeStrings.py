from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res


# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ["hello", "world"],
        ["", ""],
        ["a", "b", "c"],
        ["#", "##", "###"],
        [],
    ]
    
    for strs in test_cases:
        encoded = sol.encode(strs)
        decoded = sol.decode(encoded)
        print(f"Input:  {strs}")
        print(f"Encoded: '{encoded}'")
        print(f"Decoded: {decoded}")
        print(f"Match: {strs == decoded}\n")
