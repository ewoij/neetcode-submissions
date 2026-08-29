class Solution:

    def encode(self, strs: list[str]) -> str:
        strs = [f'{len(s)}:{s}' for s in strs]
        return ''.join(strs)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            for j in range(i+1, len(s)):
                if s[j] == ':':
                    break
            length = int(s[i:j])
            i = j+1+length
            res.append(s[j+1:i])
        return res