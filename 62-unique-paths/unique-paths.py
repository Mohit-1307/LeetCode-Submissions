class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = m + n - 2
        R = min(m - 1, n - 1)

        ans = 1

        for i in range(1, R + 1):
            ans = ans * (N - R + i) // i

        return ans