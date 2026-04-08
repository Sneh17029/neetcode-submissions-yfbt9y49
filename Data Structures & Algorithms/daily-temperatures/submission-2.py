class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0]*len(temperatures)
        for j, i in enumerate(temperatures):
                if not s or i<=temperatures[s[-1]]:
                        s.append(j)
                else:
                        while s and temperatures[s[-1]]<i:
                                c = s.pop()
                                res[c] = j-c
                                print(res)
                        s.append(j)
        return res