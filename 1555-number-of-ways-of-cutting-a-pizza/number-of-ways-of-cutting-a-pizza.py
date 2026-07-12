class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7

        m, n = len(pizza), len(pizza[0])

        apples = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                apples[r][c] = (
                    apples[r + 1][c]
                    + apples[r][c + 1]
                    - apples[r + 1][c + 1]
                    + (pizza[r][c] == 'A')
                )

        @lru_cache(None)
        def dp(r: int, c: int, cuts: int) -> int:
            if apples[r][c] == 0:
                return 0

            if cuts == 0:
                return 1

            ans = 0

            # horizontal cuts
            for nr in range(r + 1, m):
                if apples[r][c] - apples[nr][c] > 0:
                    ans = (ans + dp(nr, c, cuts - 1)) % MOD

            # vertical cuts
            for nc in range(c + 1, n):
                if apples[r][c] - apples[r][nc] > 0:
                    ans = (ans + dp(r, nc, cuts - 1)) % MOD

            return ans

        return dp(0, 0, k - 1)