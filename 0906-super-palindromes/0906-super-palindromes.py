class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L = int(left)
        R = int(right)

        def is_palindrome(x: int) -> bool:
            s = str(x)
            return s == s[::-1]

        ans = 0

        # A root p must satisfy p^2 <= 10^18,
        # so p < 10^9. Therefore p has at most 9 digits.
        #
        # We construct palindromic roots using their first half.
        for i in range(1, 100000):
            s = str(i)

            # Odd-length palindrome:
            # 123 -> 12321
            p = int(s + s[-2::-1])
            square = p * p

            if square > R:
                # For odd roots, p increases with i,
                # so all later odd roots are also too large.
                break

            if square >= L and is_palindrome(square):
                ans += 1

            # Even-length palindrome:
            # 123 -> 123321
            p = int(s + s[::-1])
            square = p * p

            if L <= square <= R and is_palindrome(square):
                ans += 1

        return ans