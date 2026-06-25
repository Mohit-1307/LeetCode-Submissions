class Solution:
    def maxDiff(self, num: int) -> int:
        s = list(str(num))

        # Maximum number
        mx = s[:]
        for ch in mx:
            if ch != '9':
                old = ch
                mx = ['9' if c == old else c for c in mx]
                break
        max_num = int("".join(mx))

        # Minimum number
        mn = s[:]

        if mn[0] != '1':
            old = mn[0]
            mn = ['1' if c == old else c for c in mn]
        else:
            old = None
            for c in mn[1:]:
                if c != '0' and c != '1':
                    old = c
                    break
            if old:
                mn = ['0' if c == old else c for c in mn]

        min_num = int("".join(mn))

        return max_num - min_num