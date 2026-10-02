class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0':
                return False

            grid[r][c] = '0'

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

            return True

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c):
                    res += 1

        return res
