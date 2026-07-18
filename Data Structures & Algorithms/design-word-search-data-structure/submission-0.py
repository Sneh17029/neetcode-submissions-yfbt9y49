class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c in node.children.keys():
                node = node.children[c]
                continue
            node.children[c] = Trie()
            node = node.children[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        def dfs(i, node):
            if i == len(word):
                return node.isEnd
            c = word[i]
            if c != "." and c not in node.children.keys():
                return False
            if c != ".":
                node = node.children[c]
                return dfs(i+1, node)
                
            for w in node.children.values():
                if dfs(i+1, w):
                    return True
            return False

        return dfs(0, node)