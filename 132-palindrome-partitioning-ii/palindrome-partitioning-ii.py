class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # pal[i][j] = whether s[i:j+1] is palindrome
        pal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        dp = [0] * n

        for i in range(n):
            if pal[0][i]:
                dp[i] = 0
                continue

            dp[i] = i  # worst case: cut every character

            for j in range(1, i + 1):
                if pal[j][i]:
                    dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[-1]