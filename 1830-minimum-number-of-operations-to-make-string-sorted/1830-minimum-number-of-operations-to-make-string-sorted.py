class Solution:
    def makeStringSorted(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        # factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        # inverse factorials
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        # frequency of each character
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        ans = 0

        for i, ch in enumerate(s):
            current = ord(ch) - ord('a')
            remaining = n - i - 1

            # Try putting every smaller character at position i
            for c in range(current):
                if count[c] == 0:
                    continue

                # Use one occurrence of c
                count[c] -= 1

                ways = fact[remaining]

                # Divide by factorial of each remaining frequency
                for k in range(26):
                    ways = ways * inv_fact[count[k]] % MOD

                ans = (ans + ways) % MOD

                # Restore c
                count[c] += 1

            # Fix the current character and move forward
            count[current] -= 1

        return ans