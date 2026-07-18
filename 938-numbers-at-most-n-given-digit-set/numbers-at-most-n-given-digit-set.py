class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        m = len(digits)
        L = len(s)

        ans = 0

        # Count numbers with fewer digits
        for length in range(1, L):
            ans += m ** length

        # Count numbers with the same length
        for i, ch in enumerate(s):
            smaller = 0

            for d in digits:
                if d < ch:
                    smaller += 1
                else:
                    break

            ans += smaller * (m ** (L - i - 1))

            if ch not in digits:
                return ans

        return ans + 1