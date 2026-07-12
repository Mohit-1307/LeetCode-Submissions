class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        cnt = [0] * batchSize

        for g in groups:
            cnt[g % batchSize] += 1

        happy = cnt[0]

        # remove remainder-0 groups
        counts = cnt[1:]

        BASE = 31

        def encode(arr):
            state = 0
            for x in arr:
                state = state * BASE + x
            return state

        @lru_cache(None)
        def dfs(state, mod):
            arr = [0] * (batchSize - 1)

            x = state
            for i in range(batchSize - 2, -1, -1):
                arr[i] = x % BASE
                x //= BASE

            best = 0

            for r in range(1, batchSize):
                idx = r - 1

                if arr[idx] == 0:
                    continue

                arr[idx] -= 1
                nxt = encode(arr)

                gain = 1 if mod == 0 else 0

                best = max(
                    best,
                    gain + dfs(nxt, (mod + r) % batchSize)
                )

                arr[idx] += 1

            return best

        return happy + dfs(encode(counts), 0)