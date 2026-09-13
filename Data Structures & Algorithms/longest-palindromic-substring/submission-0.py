class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def valid(l, r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        for i in range(len(s)):
            p = valid(i, i)
            if len(p)>len(res):
                res = p
            p = valid(i, i+1)
            if len(p)>len(res):
                res = p
        return res