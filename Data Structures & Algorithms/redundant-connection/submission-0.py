class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges)+1))
        rank = [1]*(len(edges)+1)
        def find(a):
            if a != parent[a]:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        def union(a, b):
            r1 = find(a)
            r2 = find(b)
            if r1 == r2:
                return False
            if rank[r1] < rank[r2]:
                r1, r2 = r2, r1
            parent[r2] = parent[r1]
            rank[r1] += rank[r2]
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]