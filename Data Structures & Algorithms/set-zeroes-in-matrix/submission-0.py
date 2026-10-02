class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # given an m x n matrix of integers
        # if an element if 0, set its entire row and column to 0s
        # update the matrix in place

        # basically, the main challenge is
        # we have to keep track of the rows and columsn affected
        # because we have to update it in place

        # have some sort of data structure that will store
        # the rows and columns affected, and then
        # update it at the end
        ROWS, COLS = len(matrix), len(matrix[0])
        
        vert = set()
        hori = set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    vert.add(r)
                    hori.add(c)

        for r in range(ROWS):
            for c in range(COLS):
                if r in vert or c in hori:
                    matrix[r][c] = 0

