class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        col0 = True

        # Mark rows and columns
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = False

            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Fill interior cells
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # First row
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        # First column
        if not col0:
            for i in range(m):
                matrix[i][0] = 0