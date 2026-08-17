class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        if not word: return

        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            
            curr = curr.children[ch]

        curr.isWord = True
            

    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                return False

            curr = curr.children[ch]

        return curr.isWord

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            if ch not in curr.children:
                return False

            curr = curr.children[ch]

        return True
        