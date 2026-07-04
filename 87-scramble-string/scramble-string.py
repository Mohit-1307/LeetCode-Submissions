class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def dfs(a, b):

            if a == b:
                return True

            if Counter(a) != Counter(b):
                return False

            n = len(a)

            for k in range(1, n):

                # No swap
                if dfs(a[:k], b[:k]) and dfs(a[k:], b[k:]):
                    return True

                # Swap
                if dfs(a[:k], b[n-k:]) and dfs(a[k:], b[:n-k]):
                    return True

            return False

        return dfs(s1, s2)