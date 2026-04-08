class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        used = [False]*len(nums)
        def back():
            if len(sub) == len(nums):
                res.append(sub[:])
                return
            for j in range(len(nums)):
                if used[j] == True:
                    continue
                sub.append(nums[j])
                used[j] = True
                back()
                sub.pop()
                used[j] = False
        back()
        return res