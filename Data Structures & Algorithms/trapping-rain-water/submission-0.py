class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = max_past(height)
        max_right = max_past(height[::-1])[::-1]

        res = 0

        for i in range(len(height)):
            res += min(max_left[i], max_right[i]) - height[i]

        return res

def max_past(arr):
    res = list(arr)
    for i in range(1, len(arr)):
        res[i] = max(res[i], res[i-1])
    return res