class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # s = []
        # res = [0]*len(temperatures)
        # for j, i in enumerate(temperatures):
        #         while s and temperatures[s[-1]]<i:
        #                 c = s.pop()
        #                 res[c] = j-c
        #                 print(res)
        #         s.append(j)
        # return res
        s = []
        curr = 0
        res = [0]*len(temperatures)
        for i, j in enumerate(temperatures):
                while s and j > temperatures[s[-1]]:
                        idx = s.pop()
                        res[idx] = i - idx
                s.append(i)
        return res