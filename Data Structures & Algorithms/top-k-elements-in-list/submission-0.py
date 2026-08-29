class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        
        count = sorted(((c, v) for v, c in count.items()), reverse=True)

        count = [v for (_, v) in count]

        count = count[:k]

        return count