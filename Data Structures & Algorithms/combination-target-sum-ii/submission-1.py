class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sub = []
        def backTrack(i):
            if sum(sub) == target:
                res.append(sub[:])
                return
            if sum(sub) > target:
                return
            for j in range(i, len(candidates)):
                if j>i and candidates[j-1] == candidates[j]:
                    continue
                sub.append(candidates[j])
                backTrack(j+1)
                sub.pop()
        backTrack(0)
        return [r for r in res]