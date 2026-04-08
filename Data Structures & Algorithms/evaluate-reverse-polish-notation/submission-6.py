class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in range(len(tokens)):
            print(s)
            if tokens[i] not in ["+", "-", "*", "/"]:
                s.append(tokens[i])
            else:
                v1 = s.pop(-2) + tokens[i] + s.pop(-1)
                s.append(str(int(eval("".join(v1)))))
        return int(eval(s.pop(-1)))