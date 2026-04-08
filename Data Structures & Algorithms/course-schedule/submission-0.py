class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashMap = defaultdict(list)
        for dest, src in prerequisites:
            hashMap[src].append(dest)
        l = [False] * numCourses

        def dfs(val):
            if l[val] == 2:
                return True
            if l[val] == 1:
                return False
            l[val] = 1
            for i in hashMap[val]:
                if not dfs(i):
                    return False
            l[val] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True