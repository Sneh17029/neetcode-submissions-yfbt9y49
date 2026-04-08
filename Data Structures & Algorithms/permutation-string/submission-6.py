class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
                return False
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
        return False