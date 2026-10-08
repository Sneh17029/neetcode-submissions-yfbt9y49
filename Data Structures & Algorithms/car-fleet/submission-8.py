class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # # cars = sorted(zip(position, speed), reverse=True)
        # m = {}
        # for i in range(len(position)):
        #         m[position[i]] = speed[i]
        # s = sorted(m.items(), key = lambda x : x[0], reverse = True)
        # st = []
        # for i, v in s:
        #         time = (target - i)/v
        #         if not st or st[-1] < time:
        #                 st.append(time)
        # return len(st)
        m = {}
        for i in range(len(position)):
                m[position[i]] = speed[i]
        m = sorted(m.items(), key = lambda x:x[0], reverse=True)
        t = 0
        curr = 0
        for i, v in m:
                time = (target - i)/v
                if t:
                        if t >= time:
                                continue
                        else:
                                t = time
                                curr += 1
                else:
                        t = time
                        curr += 1
        return curr