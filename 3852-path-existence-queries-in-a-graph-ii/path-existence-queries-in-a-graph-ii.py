from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        order = sorted(range(n), key=lambda x: nums[x])
        vals = [nums[i] for i in order]

        pos = [0] * n
        for p, node in enumerate(order):
            pos[node] = p

        # connected components in sorted order
        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if vals[i] - vals[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        # farthest reachable in one step
        nxt = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and vals[j + 1] - vals[i] <= maxDiff:
                j += 1
            nxt[i] = j

        LOG = (n + 1).bit_length()

        up = [nxt]
        for _ in range(LOG - 1):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            l = pos[u]
            r = pos[v]

            if l > r:
                l, r = r, l

            if comp[l] != comp[r]:
                ans.append(-1)
                continue

            cur = l
            dist = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < r:
                    cur = up[k][cur]
                    dist += 1 << k

            ans.append(dist + 1)

        return ans