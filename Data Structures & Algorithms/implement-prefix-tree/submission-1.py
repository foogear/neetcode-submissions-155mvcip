class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(word, curr = self.root):
            if not word:
                if curr.endOfWord:
                    return True
                return False

            c = word[0]
            if c not in curr.children:
                return False
            if not dfs(word[1:], curr.children[c]):
                return False
            
            return True 
        
        return dfs(word)

    def startsWith(self, prefix: str) -> bool:
        def dfs(prefix, curr = self.root):
            if not prefix:
                return True

            c = prefix[0]
            if c not in curr.children:
                return False
            if not dfs(prefix[1:], curr.children[c]):
                return False

            return True
        
        return dfs(prefix)
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
