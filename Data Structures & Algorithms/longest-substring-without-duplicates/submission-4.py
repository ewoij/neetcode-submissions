class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)

        chars = set([s[0]])
        l, r = 0, 0
        res = 0

        while r < len(s) - 1:
            if s[r+1] not in chars:
                r += 1
                chars.add(s[r])
            else:
                chars.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            
        return res