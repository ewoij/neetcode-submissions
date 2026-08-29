class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            m.setdefault(tuple(sorted(s)), []).append(s)
        return list(m.values())