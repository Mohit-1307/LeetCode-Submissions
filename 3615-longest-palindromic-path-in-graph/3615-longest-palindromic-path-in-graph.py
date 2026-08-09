class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = set()
        q = deque()

        ans = 1

        # Length 1 palindromes
        for i in range(n):
            mask = 1 << i
            vis.add((mask, i, i))
            q.append((mask, i, i))

        # Length 2 palindromes
        for u, v in edges:
            if label[u] == label[v]:
                mask = (1 << u) | (1 << v)
                if (mask, u, v) not in vis:
                    vis.add((mask, u, v))
                    vis.add((mask, v, u))
                    q.append((mask, u, v))
                    q.append((mask, v, u))
                    ans = 2

        while q:
            mask, u, v = q.popleft()

            ans = max(ans, mask.bit_count())

            for nu in adj[u]:
                if mask >> nu & 1:
                    continue

                for nv in adj[v]:
                    if mask >> nv & 1:
                        continue
                    if nu == nv:
                        continue

                    if label[nu] != label[nv]:
                        continue

                    newMask = mask | (1 << nu) | (1 << nv)

                    state = (newMask, nu, nv)
                    if state not in vis:
                        vis.add(state)
                        q.append(state)

        return ans