class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        c = Counter(s)
        count = 0
        curr = set()
        res = []
        for i in s:
            if c[i] > 1:
                curr.add(i)
                count += 1
                c[i] -= 1
            else:
                flag = True
                count += 1
                for j in curr:
                    if j == i:
                        c[i] -= 1
                    if j != i and c[j] > 0:
                        flag = False
                if flag:
                    curr = set()
                    res.append(count)
                    count = 0
        return res