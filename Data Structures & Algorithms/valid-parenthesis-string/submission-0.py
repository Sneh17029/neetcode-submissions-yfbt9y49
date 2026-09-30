class Solution:
    def checkValidString(self, s: str) -> bool:
        os = []
        ss = []
        for i, c in enumerate(s):
            if c == "(":
                os.append(i)
            elif c == "*":
                ss.append(i)
            else:
                if len(os) > 0:
                    os.pop()
                elif len(ss) > 0:
                    ss.pop()
                else:
                    return False
        while os and ss:
            if os[-1] > ss[-1]:
                return False
            os.pop()
            ss.pop()
        return False if os else True