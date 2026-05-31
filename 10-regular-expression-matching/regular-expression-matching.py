class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):

            if (i, j) in memo:
                return memo[(i, j)]

            # Pattern exhausted
            if j == len(p):
                return i == len(s)

            # Current character match
            first_match = (
                i < len(s)
                and (s[i] == p[j] or p[j] == '.')
            )

            # Check if next char is '*'
            if j + 1 < len(p) and p[j + 1] == '*':

                ans = (
                    dp(i, j + 2)                 # Skip x*
                    or
                    (first_match and dp(i + 1, j))  # Use x*
                )

            else:
                ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)