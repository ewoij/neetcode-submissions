class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        
        res = []

        for _ in range(k):
            k = max(count, key=lambda v: count[v])
            res.append(k)
            count.pop(k)

        return res