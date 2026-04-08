class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        sub = []
        def back(i):
            res.append(sub[:])
            for j in range(i, len(nums)):
                if j>i and nums[j-1] == nums[j]:
                    continue
                sub.append(nums[j])
                back(j+1)
                sub.pop()
        back(0)
        return res