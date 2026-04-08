class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i, v in enumerate(tokens):
                if v.lstrip('-').isdigit():
                        s.append(int(v))
                else:
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
        return s.pop()