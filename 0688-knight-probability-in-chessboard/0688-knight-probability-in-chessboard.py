class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [
            (2, 1), (2, -1),
            (-2, 1), (-2, -1),
            (1, 2), (1, -2),
            (-1, 2), (-1, -2)
        ]

        @lru_cache(None)
        def dfs(r, c, steps):
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0.0

            if steps == 0:
                return 1.0

            prob = 0.0

            for dr, dc in moves:
                prob += dfs(r + dr, c + dc, steps - 1)

            return prob / 8

        return dfs(row, column, k)