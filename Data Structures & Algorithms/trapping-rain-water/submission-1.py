class Solution:
    def trap(self, height: List[int]) -> int:
        s = 0
        n = len(height)
        pre = [0]*n
        suff = [0]*n
        for i in range(1, n):
                pre[i] = max(pre[i-1], height[i-1])
        for i in range(n-2, -1, -1):
                suff[i] = max(suff[i+1], height[i+1])
        for i in range(n):
                v = min(pre[i], suff[i]) - height[i]
                if v > 0:
                        s += v
        return s