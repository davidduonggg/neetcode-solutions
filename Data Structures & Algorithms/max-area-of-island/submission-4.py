class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # given a matrix
        # water = 0, land = 1
        # island is 1s connected horizontally/vertically

        # area is the number of cells within the island
        # return the maxiumum area of an island in grid

        # the main problem is how can we traverse the grid and
        # group the cells together so they represent an island
        ROWS, COLS = len(grid), len(grid[0])   
        maxArea = 0

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0

            # cell is land and valid
            grid[r][c] = 0 # mark as water
            area = 1

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                area += dfs(nr, nc)

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(dfs(r, c), maxArea)


        return maxArea