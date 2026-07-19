class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            su = 0
            for i in str(n):
                su += int(i)*int(i)
                print(su)
                if su in s:
                    return False
            n = su
            s.add(n)
            if su == 1:
                return True
        return True