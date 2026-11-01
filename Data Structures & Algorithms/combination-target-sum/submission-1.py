class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def backTrack(i):
            if sum(sub) == target:
                res.append(sub[:])
                return
            if sum(sub) > target:
                return
            for j in range(i, len(nums)):
                sub.append(nums[j])
                backTrack(j)
                sub.pop()
        backTrack(0)
        return res