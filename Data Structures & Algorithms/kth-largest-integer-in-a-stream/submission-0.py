class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        self.k = k
        self.arr.sort()

    def add(self, val: int) -> int:
        self.insert_sorted(self.arr, val)
        return self.arr[len(self.arr) - self.k]
        
    def insert_sorted(self, arr, x):
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid

        arr.insert(left, x)
        return arr
