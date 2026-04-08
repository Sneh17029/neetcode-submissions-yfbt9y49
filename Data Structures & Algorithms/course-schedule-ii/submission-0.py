class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashMap = defaultdict(list)
        for i, j in prerequisites:
            hashMap[i].append(j)
        l = [0]*numCourses
        res = []
        def dfs(val):
            if l[val] == 1:
                return False
            if l[val] == 2:
                return True
            l[val] = 1
            for i in hashMap[val]:
                if not dfs(i):
                    return False
            res.append(val)
            l[val] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        for i in range(numCourses):
            if i not in res:
                res.append(i)
        return res
            