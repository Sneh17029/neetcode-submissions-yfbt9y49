class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_dist = [float('inf')]*n
        min_dist[0] = 0
        visited = [False]*n
        total_cost = 0

        for i in range(n):
            curr = -1
            for j in range(n):
                if not visited[j] and (curr == -1 or min_dist[j] < min_dist[curr]):
                    curr = j
            visited[curr] = True
            total_cost += min_dist[curr]

            curr_x, curr_y = points[curr]

            for k in range(n):
                if not visited[k]:
                    nxt_x, nxt_y = points[k]
                    curr_dist = abs(nxt_x - curr_x) + abs(nxt_y - curr_y)
                    if curr_dist < min_dist[k]:
                        min_dist[k] = curr_dist
        return total_cost