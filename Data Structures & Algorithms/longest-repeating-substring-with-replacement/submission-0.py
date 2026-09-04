class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        l = 0
        res = 0

        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1

            if (r - l + 1) - max(chars.values()) <= k:
                res = max(res, r - l + 1)
            else:
                chars[s[l]] = chars[s[l]] - 1
                l += 1

        return res
