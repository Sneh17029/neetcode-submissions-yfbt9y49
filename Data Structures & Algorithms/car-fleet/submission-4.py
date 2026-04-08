class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        m = {}
        for i in range(len(position)):
                m[position[i]] = speed[i]
        s = sorted(m.items(), key = lambda x : x[0], reverse = True)
        st = []
        for i, v in s:
                time = (target - i)/v
                if not st or st[-1] < time:
                        st.append(time)
        return len(st)