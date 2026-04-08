class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = {}
        freq = 0
        l = 0
        ans = 0
        for r in range(len(s)):
                m[s[r]] = m.get(s[r], 0) + 1
                freq = max(freq, m[s[r]])
                while (r-l+1) - freq > k:
                        m[s[l]] -= 1
                        l += 1
                ans = max(ans, r-l+1)
        return ans