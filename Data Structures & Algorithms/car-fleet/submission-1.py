class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        my_dict = dict(zip(position, speed))
        sor = dict(sorted(my_dict.items(), reverse = True))
        l = []
        for k, v in sor.items():
            l.append((target-k)/v)
        count = 1
        print(sor)
        print(l)
        for i in range(1, len(l)):
            if l[i] > l[i-1]:
                count += 1
            else:
                l[i] = l[i-1]
        return count