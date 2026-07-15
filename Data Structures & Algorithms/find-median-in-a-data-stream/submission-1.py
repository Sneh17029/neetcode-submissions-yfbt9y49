class MedianFinder:

    def __init__(self):
        self.arr = []
        self.l = 0

    def addNum(self, num: int) -> None:
        l = 0
        r = len(self.arr) - 1
        while l<=r:
            m = (l+r)//2
            if num<=self.arr[m]:
                r = m-1
            else:
                l = m+1
        self.arr.insert(l, num)
        self.l += 1

    def findMedian(self) -> float:
        print(self.arr)
        r = self.l % 2
        q = self.l // 2
        if r == 0:
            return (self.arr[q-1] + self.arr[q])/2
        return self.arr[q]
