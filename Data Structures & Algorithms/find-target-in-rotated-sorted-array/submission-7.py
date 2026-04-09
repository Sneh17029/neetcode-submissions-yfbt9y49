class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l<=r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            if nums[m] < nums[r]:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target > nums[r] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return l if l < len(nums) and nums[l] == target else -1