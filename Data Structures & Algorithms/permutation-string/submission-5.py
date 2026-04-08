class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
                return False
        def check(m1, s):
                m2 = {}
                for i in s:
                        m2[i] = m2.get(i, 0) + 1
                print("M2", s)
                return m1 == m2
        ms1 = [0]*26
        for i in s1:
                ms1[ord(i)-ord('a')] += 1
        ms2 = [0]*26
        for i in range(len(s1)):
                ms2[ord(s2[i])-ord('a')] += 1
        l = 0
        if ms1 == ms2:
                return True
        for j in range(len(s1), len(s2)):
                ms2[ord(s2[l])-ord('a')] -= 1
                ms2[ord(s2[j])-ord('a')] += 1
                l += 1
                if ms2 == ms1:
                        return True
                # if s2[j] in ms1:
                #         res = check(ms1, s2[j:j + len(s1)])
                #         if res:
                #                 return True
        return False