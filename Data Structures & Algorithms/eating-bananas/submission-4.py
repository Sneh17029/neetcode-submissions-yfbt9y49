class Solution:
    def search(self, m, piles):
        s = 0
        for i in range(len(piles)):
            s += (piles[i]+m-1)//m
        return s
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return -1
        if h == len(piles):
            return max(piles)
        l, r = 1, max(piles)
        while l<r:
            m = l + (r-l)//2
            s = self.search(m, piles)
            if s <= h:
                r = m
            else:
                l = m + 1
        return l