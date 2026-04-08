class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l<r:
            m = l + (r-l)//2
            s = sum((p + m - 1) // m for p in piles)
            if s <= h:
                r = m
            else:
                l = m + 1
        return l