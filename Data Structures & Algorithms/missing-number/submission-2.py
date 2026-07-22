class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = set(nums)
        for i in range(n):
            if i not in s:
                return i
        return n