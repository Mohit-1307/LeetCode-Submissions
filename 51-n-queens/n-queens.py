class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        cols = set()
        diag = set()       # row - col
        anti_diag = set()  # row + col

        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):

                if (col in cols or
                    row - col in diag or
                    row + col in anti_diag):
                    continue

                cols.add(col)
                diag.add(row - col)
                anti_diag.add(row + col)
                board[row][col] = "Q"

                backtrack(row + 1)

                board[row][col] = "."
                cols.remove(col)
                diag.remove(row - col)
                anti_diag.remove(row + col)

        backtrack(0)
        return res