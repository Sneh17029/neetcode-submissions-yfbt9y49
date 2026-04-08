class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)
        dp[len(nums) - 1] = True
        for i in range(len(nums) - 2, -1, -1):
                j = i+1
                while j<i+nums[i]+1 and j<len(nums):
                        if dp[j] == True:
                                dp[i] = True
                                break
                        j += 1
        return dp[0]