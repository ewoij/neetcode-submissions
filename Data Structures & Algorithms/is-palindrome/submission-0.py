import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = string.ascii_letters + string.digits
        s = ''.join([c for c in s if c in alphabet])
        s = s.lower()
        return s == s[::-1]