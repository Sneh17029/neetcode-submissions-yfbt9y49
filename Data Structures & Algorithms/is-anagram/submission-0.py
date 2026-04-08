class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        m1 = {}
        m2 = {}
        for i, v in enumerate(s):
            m1[v] = m1.get(v, 0) + 1
        for i, v in enumerate(t):
            m2[v] = m2.get(v, 0) + 1
        return m1 == m2