class Solution:
    def ladderLength(self, begin: str, end: str, wordList: List[str]) -> int:
        nset = set(wordList)
        visited = {begin}
        q = deque([(begin, 1)])
        if end not in nset:
            return 0
        while q:
            curr, price = q.popleft()
            if curr == end:
                return price
            for c in range(len(curr)):
                for a in "abcdefghijklmnopqrstuvwxyz":
                    n = curr[:c] + a + curr[c+1:]
                    if n in nset and n not in visited:
                        visited.add(n)
                        q.append((n, price+1))
        return 0
