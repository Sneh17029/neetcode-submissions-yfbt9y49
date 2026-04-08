class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
                return False
        m = [0]*26
        for i in s:
                m[ord(i) - ord('a')] += 1
        for i in t:
                m[ord(i) - ord('a')] -= 1
                if  m[ord(i) - ord('a')] < 0:
                        return False
        return True