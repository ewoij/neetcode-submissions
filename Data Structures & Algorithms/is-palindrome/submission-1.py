import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = string.ascii_letters + string.digits
        s = ''.join([c.lower() for c in s if c in alphabet])

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False

            l, r = l + 1, r - 1

        return True