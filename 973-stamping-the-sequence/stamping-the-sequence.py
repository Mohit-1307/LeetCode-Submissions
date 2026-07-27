from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        target = list(target)
        res = []
        visited = [False] * (n - m + 1)
        stars = 0

        while stars < n:
            changed = False

            for i in range(n - m + 1):
                if not visited[i] and self.canReplace(target, i, stamp):
                    stars += self.doReplace(target, i, m)
                    visited[i] = True
                    changed = True
                    res.append(i)

                    if stars == n:
                        break

            if not changed:
                return []

        return res[::-1]

    def canReplace(self, target, pos, stamp):
        changed = False

        for i in range(len(stamp)):
            if target[pos + i] == '*':
                continue
            if target[pos + i] != stamp[i]:
                return False
            changed = True

        return changed

    def doReplace(self, target, pos, m):
        count = 0

        for i in range(m):
            if target[pos + i] != '*':
                target[pos + i] = '*'
                count += 1

        return count