class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        res = []
        for i in strs:
                c = Counter(i)
                key = tuple(sorted(c.items())) 
                print(key)
                m[key].append(i)
        for i, v in m.items():
                res.append(v)
        return res


        # res = []
        # mainMap = defaultdict(list)
        # for i in strs:
        #         m = [0]*26
        #         for j in i:
        #                 m[ord(j) - ord('a')] += 1
        #         mainMap[tuple(m)].append(i)
        # for i, v in mainMap.items():
        #         res.append(v)
        # return res
