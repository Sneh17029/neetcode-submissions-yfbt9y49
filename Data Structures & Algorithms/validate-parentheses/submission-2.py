class Solution:
    def isValid(self, s: str) -> bool:
        m = {"}":"{", "]":"[", ")":"("}
        st = []
        for i in s:
                if i not in m:
                        st.append(i)
                else:
                        if len(st) == 0:
                                return False
                        v = st.pop()
                        if v != m[i]:
                                return False
        return True if len(st) == 0 else False