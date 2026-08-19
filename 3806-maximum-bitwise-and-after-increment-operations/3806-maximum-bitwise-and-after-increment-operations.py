from typing import List


class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        max_val = max(nums) + k
        bits = max_val.bit_length()

        ans = 0
        cost = [0] * len(nums)

        for bit in range(bits - 1, -1, -1):
            target = ans | (1 << bit)

            for i, x in enumerate(nums):
                # Highest bit where target requires 1
                # but x currently has 0.
                diff = target & ~x

                j = diff.bit_length()

                # Keep only the lower j bits.
                mask = (1 << j) - 1

                # Minimum increments needed for x to satisfy target.
                cost[i] = (target & mask) - (x & mask)

            cost.sort()

            # We only need the m cheapest elements.
            if sum(cost[:m]) <= k:
                ans = target

        return ans