class Solution:
    def lengthOfLongestSubstring(seenlf, s: str) -> int:
        left = 0
        seen = {}
        c = 0
        for right in range(len(s)):
            if s[right] in seen:
                left = max(left, seen[s[right]] + 1)
            c = max(c, right-left + 1)
            seen[s[right]] = right
        return c