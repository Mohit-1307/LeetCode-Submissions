class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        m = s.count('0')

        if m == 0:
            return 0

        # Special case: every operation flips all indices
        if k == n:
            return 1 if m == n else -1

        base = (m + k - 1) // k
        ans = float('inf')

        if k % 2 == 0:
            # tk is always even
            if m % 2:
                return -1

            for parity in (0, 1):  # even t / odd t
                need = m if parity == 0 else n - m

                L = max(
                    base,
                    (need + (n - k) - 1) // (n - k)
                )

                t = L if L % 2 == parity else L + 1
                ans = min(ans, t)

        else:
            # t parity must equal m parity
            parity = m % 2
            need = m if parity == 0 else n - m

            L = max(
                base,
                (need + (n - k) - 1) // (n - k)
            )

            ans = L if L % 2 == parity else L + 1

        return ans