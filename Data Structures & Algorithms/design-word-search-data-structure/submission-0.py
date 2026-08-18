class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:
    # it seems like this is just a standard trie
    # key invariant:
    # . == wildcard, can be matched with any letter

    def __init__(self):
        self.root = Node()


    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()

            curr = curr.children[ch]

        curr.isWord = True
        

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(i, curr):
            if i == len(word):
                return curr.isWord

            if word[i] == '.':
                for child in curr.children:
                    if dfs(i + 1, curr.children[child]): return True

                return False

            if word[i] not in curr.children:
                return False

            return dfs(i + 1, curr.children[word[i]])
            
        return dfs(0, self.root)