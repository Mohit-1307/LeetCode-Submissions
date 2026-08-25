class Solution:
    def cherryPickup(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        # dp[c1][c2] = maximum cherries collected
        # when robots are at columns c1 and c2
        dp = [[-1] * cols for _ in range(cols)]

        dp[0][cols - 1] = grid[0][0] + grid[0][cols - 1]

        for r in range(1, rows):
            new_dp = [[-1] * cols for _ in range(cols)]

            for c1 in range(cols):
                for c2 in range(cols):
                    if dp[c1][c2] == -1:
                        continue

                    # Each robot can move -1, 0, +1
                    for d1 in (-1, 0, 1):
                        nc1 = c1 + d1

                        if nc1 < 0 or nc1 >= cols:
                            continue

                        for d2 in (-1, 0, 1):
                            nc2 = c2 + d2

                            if nc2 < 0 or nc2 >= cols:
                                continue

                            cherries = grid[r][nc1]

                            # If both robots are on different cells,
                            # collect both cells.
                            if nc1 != nc2:
                                cherries += grid[r][nc2]

                            new_dp[nc1][nc2] = max(
                                new_dp[nc1][nc2],
                                dp[c1][c2] + cherries
                            )

            dp = new_dp

        return max(map(max, dp))