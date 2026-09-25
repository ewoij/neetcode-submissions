class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [v for i in range(len(nums)+1) for v in self.toto(nums, 0, i)]

    def toto(self, nums, start, n):
        length = len(nums) - start
        if n == 0:
            return [[]]

        if length < n:
            return []

        res = []
        for i in range(start, len(nums)):
            r = self.toto(nums, i+1, n-1)
            res += [[nums[i]] + v for v in r]
        
        return res
