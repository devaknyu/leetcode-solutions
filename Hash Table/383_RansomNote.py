
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = {}
        for c in magazine:
            if c in available:
                available[c] += 1
            else:
                available[c] = 1
        
        for c in ransomNote:
            if c not in available:
                return False
            elif available[c] == 1:
                del available[c]
            else:
                available[c] -= 1
        return True
