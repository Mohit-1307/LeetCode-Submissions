class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        # Step 1: detect node with two parents
        parent = [0] * (n + 1)
        cand1 = None
        cand2 = None

        for u, v in edges:
            if parent[v] == 0:
                parent[v] = u
            else:
                cand1 = [parent[v], v]
                cand2 = [u, v]
                break

        # Union Find
        uf = list(range(n + 1))

        def find(x):
            while uf[x] != x:
                uf[x] = uf[uf[x]]
                x = uf[x]
            return x

        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa == pb:
                return False
            uf[pb] = pa
            return True

        # Case: node with two parents
        if cand2:
            uf = list(range(n + 1))
            for u, v in edges:
                if [u, v] == cand2:
                    continue
                if not union(u, v):
                    return cand1
            return cand2

        # Case: only cycle
        uf = list(range(n + 1))
        for u, v in edges:
            if not union(u, v):
                return [u, v]