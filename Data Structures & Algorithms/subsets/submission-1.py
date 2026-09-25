class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)+1):
            if (r := self.toto(nums, 0, i)) and r is not None:
                res.extend(r)
        return res

    def toto(self, nums, start, n):
        length = len(nums) - start
        if n == 0:
            return [[]]

        if length < n:
            return None

        res = []
        for i in range(start, len(nums)):
            r = self.toto(nums, i+1, n-1)
            if r is not None:
                res += [[nums[i]] + v for v in r]
        
        return res
