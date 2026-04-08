class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def check(m1, s):
                m2 = {}
                for i in s:
                        m2[i] = m2.get(i, 0) + 1
                print("M2", s)
                return m1 == m2
        ms1 = {}
        for i in s1:
                ms1[i] = ms1.get(i, 0) + 1
        ms2 = {}
        for j in range(len(s2)):
                if s2[j] in ms1:
                        res = check(ms1, s2[j:j + len(s1)])
                        if res:
                                return True
        return False