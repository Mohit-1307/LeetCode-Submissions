class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        m = len(nums[0])

        order = list(range(n))

        # ranks[t] = ordering for trim=t
        ranks = [None] * (m + 1)

        for pos in range(m - 1, -1, -1):

            buckets = [[] for _ in range(10)]

            for idx in order:
                digit = ord(nums[idx][pos]) - ord('0')
                buckets[digit].append(idx)

            order = []

            for b in buckets:
                order.extend(b)

            trim = m - pos
            ranks[trim] = order[:]

        ans = []

        for k, trim in queries:
            ans.append(ranks[trim][k - 1])

        return ans