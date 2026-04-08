class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        res = []
        for i in nums:
                m[i] = m.get(i, 0) + 1
        sorted_dic = {k:v for k,v in sorted(m.items(), key = lambda item: item[1], reverse = True)}
        print(sorted_dic)
        for i in sorted_dic.keys():
                res.append(i)
                if len(res) == k:
                        return res
        return res
