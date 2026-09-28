class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {char : i for i, char in enumerate(s)}
        end = 0
        start = 0
        res = []
        for k, v in enumerate(s):
            end = max(end, last_idx[v])
            if end == k:
                res.append(end - start + 1)
                start = end + 1
        return res