class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # water can flow to an adj cell with height equal or lower
        # water can flow into ocean from cells adjacent to ocean

        # find all cells where water can flow to both pacific and atlantic

        # brute force : (N^2)

        # check all cells to see if they can reach atlantic
        # then, check all cells to see if they can reach pacific
        # return the union of those two sets
        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = set()
        atlantic = set()
        pacific = set()

        def dfs(r, c, ocean):
            if (r, c) in visited:
                return

            ocean.add((r, c))
            visited.add((r, c))

            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc

                if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or heights[nr][nc] < heights[r][c]:
                    continue

                dfs(nr, nc, ocean)

        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic)

        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic)

        visited.clear()

        for r in range(ROWS):
            dfs(r, 0, pacific)

        for c in range(COLS):
            dfs(0, c, pacific)

        return list(atlantic.intersection(pacific))
            

            