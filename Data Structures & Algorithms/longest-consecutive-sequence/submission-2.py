class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)

        res = 0

        for v in nums:
            is_start = v - 1 not in nums

            if is_start:
                end = v
                while end in nums:
                    end += 1

                res = max(res, end - v)

        return res