class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        s = list(s)
        n = len(s)

        class Node:
            __slots__ = ("l", "r", "len", "lchar", "rchar", "lmx", "rmx", "mx")

            def __init__(self):
                self.l = self.r = 0
                self.len = 0
                self.lchar = ""
                self.rchar = ""
                self.lmx = self.rmx = self.mx = 0

        tree = [Node() for _ in range(4 * n)]

        def pull(idx):
            left = tree[idx * 2]
            right = tree[idx * 2 + 1]
            cur = tree[idx]

            cur.len = left.len + right.len
            cur.lchar = left.lchar
            cur.rchar = right.rchar

            # prefix
            cur.lmx = left.lmx
            if left.lmx == left.len and left.rchar == right.lchar:
                cur.lmx = left.len + right.lmx

            # suffix
            cur.rmx = right.rmx
            if right.rmx == right.len and left.rchar == right.lchar:
                cur.rmx = right.len + left.rmx

            # answer
            cur.mx = max(left.mx, right.mx)
            if left.rchar == right.lchar:
                cur.mx = max(cur.mx, left.rmx + right.lmx)

        def build(idx, l, r):
            tree[idx].l = l
            tree[idx].r = r
            tree[idx].len = r - l + 1

            if l == r:
                c = s[l]
                tree[idx].lchar = c
                tree[idx].rchar = c
                tree[idx].lmx = 1
                tree[idx].rmx = 1
                tree[idx].mx = 1
                return

            mid = (l + r) // 2
            build(idx * 2, l, mid)
            build(idx * 2 + 1, mid + 1, r)
            pull(idx)

        def update(idx, pos, ch):
            node = tree[idx]

            if node.l == node.r:
                node.lchar = ch
                node.rchar = ch
                node.lmx = node.rmx = node.mx = 1
                return

            if pos <= tree[idx * 2].r:
                update(idx * 2, pos, ch)
            else:
                update(idx * 2 + 1, pos, ch)

            pull(idx)

        build(1, 0, n - 1)

        ans = []

        for ch, pos in zip(queryCharacters, queryIndices):
            if s[pos] != ch:
                s[pos] = ch
                update(1, pos, ch)
            ans.append(tree[1].mx)

        return ans