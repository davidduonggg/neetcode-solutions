class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        DISTANCES = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        R, C = len(grid), len(grid[0])

        gates = []  # list[(r, c)]

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    gates.append((r, c))

        # -1 is an obstacle
        # 0 is gate
        # inf means empty room

        q = deque(gates)
        dist = 0

        while q:  # while there's elements
            for _ in range(len(q)):  # level by level
                r, c = q.popleft()
    
                if grid[r][c] == -1:
                    continue

                if dist <= grid[r][c]:
                    grid[r][c] = dist

                    # explore neighbors?
                    for row, col in DISTANCES:
                        nr, nc = r + row, c + col
                        if nr < 0 or nr >= R or nc < 0 or nc >= C:
                            continue
                        q.append((nr, nc))

            dist += 1
