class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        total = 0
        last = [0] * 26

        for ch in s:
            i = ord(ch) - ord('a')

            # New subsequences created by appending ch
            # to every existing subsequence, plus ch itself.
            new = (total + 1) % MOD

            # Remove the subsequences that were already created
            # when the previous occurrence of ch was processed.
            total = (total + new - last[i]) % MOD

            last[i] = new

        return total