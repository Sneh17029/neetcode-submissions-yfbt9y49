class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_curr = prices[0]
        m = 0
        for i in range(1, len(prices)):
                if prices[i] < min_curr:
                        min_curr = prices[i]
                else:
                        m = max(m, prices[i] - min_curr)
        return m