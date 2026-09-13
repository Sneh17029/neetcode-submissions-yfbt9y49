class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def valid(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count
        for i in range(len(s)):
            res += valid(i, i)
            res += valid(i, i+1)
        return res