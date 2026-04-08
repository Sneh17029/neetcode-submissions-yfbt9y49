class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for i in range(1, len(nums)):
            pre.append(pre[i-1]* nums[i-1])
        post = [1]
        for i in range(len(nums)-2, -1, -1):
            post.insert(0, post[0]* nums[i+1])
        l = []
        for i in range(len(nums)):
            l.append(pre[i]*post[i])
        return l