class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # given a 2d grid of characters board
        # string word
        # return true if the word is present in the grid, otherwise return false
        # horizontal and vertical
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        

        def dfs(row: int, col: int, path: int) -> bool:
            if (row, col) in visited: return False

            if len(path) > len(word): return False

            path.append(board[row][col])
            visited.add((row, col))

            if len(path) == len(word) and word == "".join(path):
                return True

            for r, c in DIRECTIONS:
                nr, nc = row + r, col + c
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                    continue

                if dfs(nr, nc, path): return True

            path.pop()
            visited.remove((row, col))

            return False
            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, []):
                    return True

        return False

            

            