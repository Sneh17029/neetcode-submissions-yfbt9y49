class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        first, second = 0, 0
        for i in range(len(nums)-1):
            first, second = second, max(second, first+nums[i])
        first, third = 0, 0
        for i in range(1, len(nums)):
            first, third = third, max(third, first+nums[i])
        return max(third, second)