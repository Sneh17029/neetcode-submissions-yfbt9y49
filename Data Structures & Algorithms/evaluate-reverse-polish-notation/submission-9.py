class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i, v in enumerate(tokens):
                if v in "+-*/":
                        a = s.pop()
                        b = s.pop()
                        if v == '+':
                                s.append(b + a)
                        elif v == '-':
                                s.append(b - a)
                        elif v == '*':
                                s.append(b * a)
                        elif v == '/':
                                s.append(int(b / a))
                else:
                        s.append(int(v))
        return s.pop()