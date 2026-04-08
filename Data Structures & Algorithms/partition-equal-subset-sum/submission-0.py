class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        su = sum(nums)
        if su%2 != 0:
            return False
        su = su//2
        res = []
        indF = []
        def back(i, total, path, ind):
            nonlocal indF
            if total == su:
                res = path[:]
                indF = ind[:]
                return True
            if total>su or i>=len(nums):
                return False
            path.append(nums[i])
            ind.append(i)
            if back(i+1, total+nums[i], path, ind):
                return True
            path.pop()
            ind.pop()
            if back(i+1, total, path, ind):
                return True
            return False
        res = back(0,0,[], [])
        return res