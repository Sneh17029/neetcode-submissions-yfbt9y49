class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i,v in edges:
            graph[i].append(v)
            graph[v].append(i)
        visited = set()
        count = 0
        def dfs(val):
            visited.add(val)
            for i in graph[val]:
                if i not in visited:
                    dfs(i)
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count