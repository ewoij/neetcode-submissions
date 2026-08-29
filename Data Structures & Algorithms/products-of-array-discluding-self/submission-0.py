class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if not nums: return []

        prod_l = [nums[0]] * len(nums)
        prod_r = [nums[-1]] * len(nums)

        for i in range(1, len(nums)):
            prod_l[i] = prod_l[i-1] * nums[i]

        for i in range(len(nums)-1-1, -1, -1):
            prod_r[i] = prod_r[i+1] * nums[i]

        res = []
        for i in range(len(nums)):
            l = 1 if i == 0 else prod_l[i-1]
            r = 1 if i == len(nums)-1 else prod_r[i+1]
            res.append(l * r)

        return res
