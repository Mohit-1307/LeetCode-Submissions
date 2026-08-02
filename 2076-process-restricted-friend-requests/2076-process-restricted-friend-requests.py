class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1

        ans = []

        for u, v in requests:
            ru, rv = find(u), find(v)

            if ru == rv:
                ans.append(True)
                continue

            ok = True
            for x, y in restrictions:
                rx, ry = find(x), find(y)

                if (ru == rx and rv == ry) or (ru == ry and rv == rx):
                    ok = False
                    break

            ans.append(ok)

            if ok:
                union(ru, rv)

        return ans