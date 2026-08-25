class Solution:
    def findDiagonalOrder(self, mat):
        m = len(mat)
        n = len(mat[0])

        ans = []

        for d in range(m + n - 1):
            diagonal = []

            # Find starting row of this diagonal
            r = max(0, d - n + 1)
            c = d - r

            while r < m and c >= 0:
                diagonal.append(mat[r][c])
                r += 1
                c -= 1

            # Reverse every other diagonal
            if d % 2 == 0:
                diagonal.reverse()

            ans.extend(diagonal)

        return ans