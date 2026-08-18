class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return

        if self.size[a] < self.size[b]:
            a, b = b, a

        self.parent[b] = a
        self.size[a] += self.size[b]


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = max(nums)

        # Smallest Prime Factor
        spf = list(range(max_num + 1))

        for i in range(2, int(max_num ** 0.5) + 1):
            if spf[i] == i:  # i is prime
                for j in range(i * i, max_num + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        dsu = DSU(n)

        # prime -> index of first number containing this prime
        owner = {}

        for i, x in enumerate(nums):
            while x > 1:
                p = spf[x]

                if p in owner:
                    dsu.union(i, owner[p])
                else:
                    owner[p] = i

                # Remove all occurrences of p
                while x % p == 0:
                    x //= p

        return max(dsu.size)