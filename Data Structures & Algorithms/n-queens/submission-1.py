class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # place n queens on an n x n chessboard so that no two queens can attack each other
        # given n, return all distinct solutions

        # return in any order
        cols = set()
        posDiag = set()
        negDiag = set()

        board = [["."] * n for _ in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                pos = r + c
                neg = r - c

                if pos in posDiag or neg in negDiag or c in cols:
                    continue

                # valid new board
                posDiag.add(r + c)
                negDiag.add(r - c)
                cols.add(c)

                board[r][c] = "Q"

                backtrack(r + 1)

                board[r][c] = "."
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                cols.remove(c)

        backtrack(0)
        return res