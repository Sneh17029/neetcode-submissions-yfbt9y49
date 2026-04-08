class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        f1 = [0]*26
        f2 = [0]*26
        n = len(s1)
        for i in s1:
            f1[ord(i) - ord('a')] += 1
        left = 0
        for right in range(len(s2)):
            f2[ord(s2[right]) - ord('a')] += 1
            if right-left+1>n:
                f2[ord(s2[left]) - ord('a')] -= 1
                left += 1
            if f1==f2:
                return True
        return False