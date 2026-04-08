class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        m = {}
        l = 0
        while j<len(s):
                if s[j] in m and i<=m[s[j]]:
                        i = m[s[j]] + 1
                m[s[j]] = j
                j+=1
                l = max(l, j-i)
                print(m, i, j)
        return l