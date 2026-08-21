class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # given a 2D matrix
        # 0: empty, 1: fresh, 2:rotten
        # if a fresh fruit is adjacent, then it is rotten
        # return the minimum number of minutes until 0 fresh fruits remain

        # the core problem is:
        # we can model the bananas rotting by doing a standard traversal
        # either with bfs or dfs
        # the harder probelm is returning the minimum number of minutes
        # in my mind, bfs comes to the top of my mind, because we can 
        # traverse and simulate it minute by minute

        # a harder problem is determining if all the bananas are rotten
        # but we can do this pretty easily by just storing the fresh bananas and 
        # checking if theyre rotten

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while q and fresh > 0:
            print(q)
            minutes += 1
            for _ in range(len(q)):
                # mark the new bananas
                # and push them onto the q
                r, c = q.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                        continue

                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))


        return minutes if fresh == 0 else -1



