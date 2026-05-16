class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(word, i = 0, curr = self.root):
            # if i == len(word) - 1: # BUG
            if i == len(word):
                if curr.endOfWord:
                    return True 
                return False

            c = word[i]
            if c == '.':
                for k in curr.children:
                    if not dfs(word, i + 1, curr.children[k]):
                        return False 
            elif c not in curr.children:
                return False
            elif not dfs(word, i + 1, curr.children[c]):
                return False

            return True

        return dfs(word)

class TrieNode:

    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False
