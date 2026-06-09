class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag = set()       # row - col
        anti_diag = set()  # row + col

        count = 0

        def backtrack(row):
            nonlocal count

            if row == n:
                count += 1
                return

            for col in range(n):
                if (col in cols or
                    row - col in diag or
                    row + col in anti_diag):
                    continue

                cols.add(col)
                diag.add(row - col)
                anti_diag.add(row + col)

                backtrack(row + 1)

                cols.remove(col)
                diag.remove(row - col)
                anti_diag.remove(row + col)

        backtrack(0)
        return count