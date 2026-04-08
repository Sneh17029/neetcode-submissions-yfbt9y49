class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        w = 0
        while l<r:
                lv = heights[l]
                rv = heights[r]
                w = max(w, min(lv, rv)*(r-l))
                if lv<rv:
                        l+=1
                else:
                        r-=1
        return w