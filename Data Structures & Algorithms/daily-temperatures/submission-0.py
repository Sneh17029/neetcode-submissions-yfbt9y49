class Solution:
    def dailyTemperatures(self, temperature: List[int]) -> List[int]:
        n = len(temperature)
        s = []
        s.append(temperature[0])
        result = [0]*n
        for i in range(1, n):
            print(s)
            print(result)
            print("/////////////")
            if s[-1] >= temperature[i]:
                s.append(temperature[i])
            else:
                x = 1
                while s and s[-1] < temperature[i]:
                    if result[i-x] == 0:
                        s.pop()
                        result[i-x] = x
                    x += 1
                s.append(temperature[i])
        return result