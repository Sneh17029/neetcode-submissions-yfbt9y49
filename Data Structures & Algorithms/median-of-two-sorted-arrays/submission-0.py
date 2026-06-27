class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        if len(num1) > len(num2):
            nums1, nums2 = num2, num1
        else:
            nums1, nums2 = num1, num2
        n = len(nums1) + len(nums2)
        e = n//2
        l = 0
        r = len(nums1)
        while l<=r:
            m = l + (r-l)//2
            l1 = nums1[m-1] if m > 0 else float("-inf")
            r1 = nums1[m] if m < len(nums1) else float("inf")
            l2 = nums2[e-m-1] if e-m>0 else float("-inf")
            r2 = nums2[e-m] if e-m<len(nums2) else float("inf")
            if l1 <= r2 and l2 <= r1:
                break
            if l1 > r2:
                r = m-1
            else:
                l = m+1
        if n % 2:
            return min(r1, r2)
        else:
            return (max(l1, l2) + min(r1, r2)) / 2
