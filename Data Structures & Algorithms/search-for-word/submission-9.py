class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # given a 2d grid of characters board
        # string word
        # return true if the word is present in the grid, otherwise return false
        # horizontal and vertical
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        

        def dfs(row: int, col: int, i: int) -> bool:
            if (row, col) in visited: return False
            if board[row][col] != word[i]: return False

            visited.add((row, col))

            if board[row][col] == word[i] and i == len(word) - 1:
                return True

            for r, c in DIRECTIONS:
                nr, nc = row + r, col + c
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                    continue

                if dfs(nr, nc, i + 1): return True

            visited.remove((row, col))

            return False
            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False

            

            