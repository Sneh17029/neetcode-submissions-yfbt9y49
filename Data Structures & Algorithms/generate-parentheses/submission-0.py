class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sub = ""
        res = []
        def back(val, sub, s, e):
            sub += val
            if len(sub) == n*2:
                res.append(sub)
                return
            if s<n:
                back("(", sub, s+1, e)
            if e<n and e<s:
                back(")", sub, s, e+1)
        back("", "", 0, 0)
        return res