class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        digits = []

        while target:
            digits.append(target % x)
            target //= x

        n = len(digits)

        @cache
        def dfs(pos: int, carry: int) -> int:
            if pos == n:
                if carry:
                    return pos
                return 0

            d = digits[pos] + carry

            cost = 2 if pos == 0 else pos

            # use digit directly
            use = d * cost + dfs(pos + 1, 0)

            # round upward (borrow from next digit)
            carry_up = (x - d) * cost + dfs(pos + 1, 1)

            return min(use, carry_up)

        return dfs(0, 0) - 1