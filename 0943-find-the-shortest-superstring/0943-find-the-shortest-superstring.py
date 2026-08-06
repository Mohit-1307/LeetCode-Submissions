class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)

        # overlap[i][j] = longest suffix of words[i]
        # matching prefix of words[j]
        overlap = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                m = min(len(words[i]), len(words[j]))
                for k in range(m, -1, -1):
                    if words[i].endswith(words[j][:k]):
                        overlap[i][j] = k
                        break

        N = 1 << n

        dp = [[-1] * n for _ in range(N)]
        parent = [[-1] * n for _ in range(N)]

        for i in range(n):
            dp[1 << i][i] = 0

        for mask in range(N):
            for last in range(n):
                if dp[mask][last] == -1:
                    continue

                for nxt in range(n):
                    if mask & (1 << nxt):
                        continue

                    newmask = mask | (1 << nxt)
                    val = dp[mask][last] + overlap[last][nxt]

                    if val > dp[newmask][nxt]:
                        dp[newmask][nxt] = val
                        parent[newmask][nxt] = last

        full = N - 1

        last = max(range(n), key=lambda i: dp[full][i])

        order = []

        mask = full
        while last != -1:
            order.append(last)
            p = parent[mask][last]
            mask ^= 1 << last
            last = p

        order.reverse()

        ans = words[order[0]]

        for i in range(1, len(order)):
            a = order[i - 1]
            b = order[i]
            ans += words[b][overlap[a][b]:]

        return ans