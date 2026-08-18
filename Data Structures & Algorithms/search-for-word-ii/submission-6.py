class Node:
    def __init__(self):
        self.children = {}
        self.word = ""

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        if not word: return

        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()

            curr = curr.children[ch]

        curr.word = word



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # given a 2D grid of characters
        # return all words that are present in the grid

        # horizontally or vertically
        # cell can only be used once

        # brute force:
        # for every word, traverse the graph. if you find the first letter, then DFS
        # for k words, it would be O (k * n^2)
        
        # instead, we can construct a trie in O(k) time, and then we traverse the grid and the trie at the same time
        # O(k * n) time
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        res = []
        visited = set()

        trie = Trie()
        for w in words:
            trie.insert(w)

        # we have the trie constructed now

        def dfs(r, c, curr):
            visited.add((r, c))

            if curr.word:
                res.append(curr.word)
                curr.word = ""

            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc

                if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or board[nr][nc] not in curr.children or (nr, nc) in visited:
                    continue

                newCh = board[nr][nc]
                dfs(nr, nc, curr.children[newCh])

            visited.remove((r, c))

            return

        for r in range(ROWS):
            for c in range(COLS):
                ch = board[r][c]
                if ch in trie.root.children:
                    dfs(r, c, trie.root.children[ch])


        return res

            
            
        
