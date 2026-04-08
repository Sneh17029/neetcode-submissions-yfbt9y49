class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in pair.values():
                stack.append(i)
            elif i in pair:
                if not stack or stack.pop() != pair[i]:
                    return False
        return not stack