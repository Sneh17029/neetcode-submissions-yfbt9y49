class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for i in nums:
            m[i] = m.get(i, 0) + 1
        l = sorted(m, key = m.get, reverse=True)
        return l[:k]