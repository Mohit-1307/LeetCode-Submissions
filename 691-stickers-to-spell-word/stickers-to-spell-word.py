class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        m = len(target)
        N = 1 << m

        sticker_count = [Counter(s) for s in stickers]

        INF = float('inf')
        dp = [INF] * N
        dp[0] = 0

        for mask in range(N):
            if dp[mask] == INF:
                continue

            for cnt in sticker_count:
                new_mask = mask
                remain = cnt.copy()

                for i, ch in enumerate(target):
                    if (new_mask >> i) & 1:
                        continue
                    if remain[ch] > 0:
                        remain[ch] -= 1
                        new_mask |= 1 << i

                dp[new_mask] = min(dp[new_mask], dp[mask] + 1)

        ans = dp[N - 1]
        return -1 if ans == INF else ans