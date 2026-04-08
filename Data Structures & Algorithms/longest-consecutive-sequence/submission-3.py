class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l = 0
        for i in s:
                if i-1 in s:
                    continue
                il = 1
                val = i
                while val+1 in s:
                        val+=1
                        il += 1
                l = max(il, l)
        return l