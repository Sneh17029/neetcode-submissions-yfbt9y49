class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lis = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            j = nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if j > 0:
                break
            while left<right:
                l = nums[left]
                r = nums[right]
                if j+l+r == 0:
                    lis.append([j,l,r])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif j+l+r<0:
                    left+=1
                else:
                    right-=1
        return lis