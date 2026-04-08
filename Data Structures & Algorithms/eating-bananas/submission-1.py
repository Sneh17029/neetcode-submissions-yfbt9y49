class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid = left + (right - left)//2
            s = 0
            for i in piles:
                s += math.ceil(i/mid)
            if s > h:
                left = mid + 1
            else:
                right = mid - 1
        return left