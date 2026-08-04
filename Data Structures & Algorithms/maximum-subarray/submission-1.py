class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = float('-inf')
        prev_sum = float('-inf')
        for i in range(len(nums)):
                curr_sum = max(nums[i], curr_sum + nums[i])
                prev_sum = max(prev_sum, curr_sum)
        return prev_sum