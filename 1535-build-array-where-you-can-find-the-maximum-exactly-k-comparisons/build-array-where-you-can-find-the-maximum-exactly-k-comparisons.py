class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        dp = [[0] * (k + 1) for _ in range(m + 1)]

        for mx in range(1, m + 1):
            dp[mx][1] = 1

        for _ in range(1, n):
            ndp = [[0] * (k + 1) for _ in range(m + 1)]

            for cost in range(1, k + 1):
                prefix = [0] * (m + 1)
                for mx in range(1, m + 1):
                    prefix[mx] = (prefix[mx - 1] + dp[mx][cost]) % MOD

                for mx in range(1, m + 1):
                    # choose value <= current maximum
                    ndp[mx][cost] = (ndp[mx][cost] + dp[mx][cost] * mx) % MOD

                    # choose current element as a new maximum
                    if cost < k:
                        ndp[mx][cost + 1] = (
                            ndp[mx][cost + 1] + prefix[mx - 1]
                        ) % MOD

            dp = ndp

        ans = 0
        for mx in range(1, m + 1):
            ans = (ans + dp[mx][k]) % MOD

        return ans