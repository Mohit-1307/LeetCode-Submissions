class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7

        runs = []
        cnt = 1

        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                cnt += 1
            else:
                runs.append(cnt)
                cnt = 1

        runs.append(cnt)

        m = len(runs)

        total = 1
        for r in runs:
            total = (total * r) % MOD

        if m >= k:
            return total

        dp = [0] * k
        dp[0] = 1

        for r in runs:
            ndp = [0] * k

            pref = [0] * k
            pref[0] = dp[0]

            for i in range(1, k):
                pref[i] = (pref[i - 1] + dp[i]) % MOD

            for s in range(1, k):
                L = max(0, s - r)
                R = s - 1

                ndp[s] = pref[R]
                if L > 0:
                    ndp[s] = (ndp[s] - pref[L - 1]) % MOD

            dp = ndp

        invalid = sum(dp[:k]) % MOD

        return (total - invalid) % MOD