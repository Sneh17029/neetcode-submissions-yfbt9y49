class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = set(days)
        dp = [0]*366
        for day in range(1, 366):
            if day not in days:
                dp[day] = dp[day-1]
            else:
                dp[day] = min(dp[day-1] + costs[0], dp[max(0, day-7)]   + costs[1], dp[max(0, day-30)] + costs[2])
        return dp[365]