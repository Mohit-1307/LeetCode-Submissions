class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)

        # Remove redundant coins.
        # If a coin is a multiple of another coin,
        # it produces no new amounts.
        coins.sort()
        useful = []

        for c in coins:
            if not any(c % d == 0 for d in useful):
                useful.append(c)

        coins = useful
        n = len(coins)

        # Precompute LCM for every subset.
        lcms = []

        for mask in range(1, 1 << n):
            lcm = 1
            bits = 0

            for i in range(n):
                if mask & (1 << i):
                    bits += 1
                    lcm = lcm // gcd(lcm, coins[i]) * coins[i]

            lcms.append((lcm, bits))

        def count(x):
            """Number of distinct valid amounts <= x."""
            total = 0

            for lcm, bits in lcms:
                if lcm > x:
                    continue

                if bits & 1:
                    total += x // lcm
                else:
                    total -= x // lcm

            return total

        # The answer cannot exceed k * minimum_coin.
        lo = 1
        hi = k * min(coins)

        while lo < hi:
            mid = (lo + hi) // 2

            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo