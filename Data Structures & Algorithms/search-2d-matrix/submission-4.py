class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l<r:
            mid = l + (r-l)//2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                l = mid
                break
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        print("here")
        a, b = 0, len(matrix[0]) - 1
        while a<= b:
            m = a + (b-a)//2
            if matrix[l][m] == target:
                return True
            if matrix[l][m]< target:
                a = m+1
            else:
                b = m - 1
        return False