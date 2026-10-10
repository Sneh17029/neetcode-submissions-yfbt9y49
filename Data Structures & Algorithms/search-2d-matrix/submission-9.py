class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # l, r = 0, len(matrix) - 1
        # while l<r:
        #     mid = l + (r-l)//2
        #     if matrix[mid][0] == target:
        #         return True
        #     if matrix[mid][0] <= target <= matrix[mid][-1]:
        #         l = mid
        #         break
        #     elif matrix[mid][0] < target:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # a, b = 0, len(matrix[0]) - 1
        # while a<= b:
        #     m = a + (b-a)//2
        #     if matrix[l][m] == target:
        #         return True
        #     if matrix[l][m]< target:
        #         a = m+1
        #     else:
        #         b = m - 1
        # return False
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = l + (r-l)//2
            if matrix[m][0] <= target <= matrix[m][-1]:
                l = m
                break
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        a, b = 0, len(matrix[0]) - 1
        if l >= len(matrix) or not (matrix[l][0] <= target <= matrix[l][-1]):
            return False

        while a <= b:
            m = a + (b-a)//2
            if matrix[l][m] == target:
                return True
            elif matrix[l][m] < target:
                a = m + 1
            else:
                b = m - 1
        return False