class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        res = nums[0]
        for i in nums[1:]:
            temp = currMax
            currMax = max(i, currMax*i, currMin*i)
            currMin = min(i, temp*i, currMin*i)
            res = max(currMax, res)
        return res