class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(pos, mask):
            # All positions are filled
            if pos > n:
                return 1

            count = 0

            for num in range(1, n + 1):
                bit = 1 << (num - 1)

                # num is already used
                if mask & bit:
                    continue

                # Check beautiful arrangement condition
                if num % pos == 0 or pos % num == 0:
                    count += backtrack(pos + 1, mask | bit)

            return count

        return backtrack(1, 0)