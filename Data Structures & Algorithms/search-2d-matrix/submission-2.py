class Solution:
    def indexMat(self, l, r, matrix, target):
        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0] <= target:
                if mid<len(matrix)-1 and target < matrix[mid+1][0]:
                    return mid
                elif mid == len(matrix) - 1:
                    return mid
                else:
                    l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
        return -1
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        m = self.indexMat(l, r, matrix, target)
        l = 0
        r = len(matrix[0]) - 1
        x = matrix[m]
        while l<=r:
            mid = l + (r-l)//2
            if (target == x[mid]):
                return True
            if target < x[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False
        