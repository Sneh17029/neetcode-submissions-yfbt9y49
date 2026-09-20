class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        itinerary = []
        for dep, arr in sorted(tickets, reverse = True):
            graph[dep].append(arr)
        def dfs(port):
            while graph[port]:
                nxt = graph[port].pop()
                dfs(nxt)
            itinerary.append(port)
        dfs("JFK")
        return itinerary[::-1]
