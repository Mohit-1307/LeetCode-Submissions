class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Find rook
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    r, c = i, j
                    break

        ans = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            while 0 <= nr < 8 and 0 <= nc < 8:
                if board[nr][nc] == 'B':
                    break

                if board[nr][nc] == 'p':
                    ans += 1
                    break

                nr += dr
                nc += dc

        return ans