from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        s1_c = Counter(s1)
        s2_c = Counter(s2[:len(s1) - 1])

        for r in range(len(s1)-1, len(s2)):
            s2_c[s2[r]] += 1
            l = r - len(s1)
            if l >= 0:
                s2_c[s2[l]] -= 1
            if s1_c == s2_c:
                return True
        
        return False