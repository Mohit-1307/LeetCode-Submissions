class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        n = len(s)

        for i in range(n):
            if s[i] == '?':
                for ch in "abc":
                    left = s[i - 1] if i > 0 else ''
                    right = s[i + 1] if i < n - 1 else ''

                    if ch != left and ch != right:
                        s[i] = ch
                        break

        return ''.join(s)