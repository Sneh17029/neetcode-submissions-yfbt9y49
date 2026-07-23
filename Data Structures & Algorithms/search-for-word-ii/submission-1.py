class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res, visit = set(), set()
        row, col = len(board), len(board[0])
        root = TrieNode()
        for w in words:
            root.addWord(w)
        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == row or c == col or (r, c) in visit or board[r][c] not in node.children:
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)
            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root, "")
        return list(res)