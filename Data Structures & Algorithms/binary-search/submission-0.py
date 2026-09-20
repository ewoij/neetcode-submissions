class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            l, r = (l, m) if target <= nums[m] else (m + 1, r)
        
        return r if r < len(nums) and nums[r] == target else -1