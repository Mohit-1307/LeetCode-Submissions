class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        n = len(digits)

        # powers of 10
        pow10 = [1] * (n + 1)
        for i in range(n):
            pow10[i + 1] = (pow10[i] * 10) % MOD

        # prefix concatenation hash
        H = [0] * (n + 1)
        for i, d in enumerate(digits):
            H[i + 1] = (H[i] * 10 + d) % MOD

        # prefix digit sums
        pref_sum = [0] * (n + 1)
        for i, d in enumerate(digits):
            pref_sum[i + 1] = pref_sum[i] + d

        ans = []

        for l, r in queries:
            a = bisect_left(pos, l)
            b = bisect_right(pos, r) - 1

            if a > b:
                ans.append(0)
                continue

            length = b - a + 1

            x_mod = (
                H[b + 1]
                - H[a] * pow10[length]
            ) % MOD

            digit_sum = pref_sum[b + 1] - pref_sum[a]

            ans.append((x_mod * digit_sum) % MOD)

        return ans