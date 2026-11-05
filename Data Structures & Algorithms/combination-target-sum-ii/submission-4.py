class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sub = []
        def backTrack(i, remaining):
            if remaining == 0:
                res.append(sub[:])
                return
            for j in range(i, len(candidates)):
                if (j > i and candidates[j] == candidates[j-1]):
                    continue
                if candidates[j] > remaining:
                    break
                sub.append(candidates[j])
                backTrack(j + 1, remaining - candidates[j])
                sub.pop()
        backTrack(0, target)
        return res