class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # given a 2d grid where 1 represents land and 0 represents water
        # count and return the number of islands

        # the problem is basically asking
        # how can we group all of the 1s together, and how to not duplicate islands
        # what we can do is do a dfs, and then mark the visited cells as 0
        # that way, it would be O(n), we'd visit every cell once by traversing the graph,
        # and we wouldn't duplicate work
        # O(k) recursion call stack, where k is the size of the island
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0


        def dfs(r, c):
            if grid[r][c] == '0':
                return

            grid[r][c] = '0'

            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc

                if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == '0':
                    continue

                dfs(nr, nc)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(row, col)


        return islands

                