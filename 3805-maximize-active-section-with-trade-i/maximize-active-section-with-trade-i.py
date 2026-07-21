class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')

        t = '1' + s + '1'

        # Run-length encoding: [(char, length), ...]
        runs = [(ch, sum(1 for _ in grp)) for ch, grp in groupby(t)]

        max_gain = 0

        # Interior 1-runs only
        for i in range(1, len(runs) - 1):
            if runs[i][0] == '1':
                left_zero = runs[i - 1][1]
                right_zero = runs[i + 1][1]
                max_gain = max(max_gain, left_zero + right_zero)

        return ones + max_gain