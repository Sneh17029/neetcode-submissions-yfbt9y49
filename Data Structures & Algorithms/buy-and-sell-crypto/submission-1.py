class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_curr = prices[0]
        profit = 0
        for i in range(1, n):
            if(min_curr > prices[i]):
                min_curr = prices[i]
            else:
                profit = max(prices[i] - min_curr, profit)
        return profit