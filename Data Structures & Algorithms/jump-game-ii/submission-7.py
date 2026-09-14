class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(nums) - 1:
                return 0
            if nums[i] == 0:
                return 10000000
            end = min(len(nums) - 1, i + nums[i])
            res = 10000000
            for j in range(i + 1, end + 1):
                res = min(res, dfs(j) + 1)
            memo[i] = res
            return res
        return dfs(0)