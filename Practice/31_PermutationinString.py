class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1count = [0] * 26
        s2count = [0] * 26
        
        # Initialize frequency arrays for first window
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1
        
        # Count initial matches
        matches = 0
        for i in range(26):
            matches += 1 if s1count[i] == s2count[i] else 0
        
        # Slide window through s2
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # Add new character on right
            index = ord(s2[r]) - ord('a')
            s2count[index] += 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1
            
            # Remove old character on left
            index = ord(s2[l]) - ord('a')
            s2count[index] -= 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] - 1 == s2count[index]:
                matches -= 1
            l += 1
        
        return matches == 26