class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # frequency of each value
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = how many numbers are divisible by d
        cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for m in range(d, mx + 1, d):
                cnt[d] += freq[m]

        # exact[d] = number of pairs with gcd exactly d
        exact = [0] * (mx + 1)

        for d in range(mx, 0, -1):
            c = cnt[d]
            pairs = c * (c - 1) // 2  # pairs with gcd multiple of d

            for m in range(2 * d, mx + 1, d):
                pairs -= exact[m]

            exact[d] = pairs

        # prefix counts of sorted gcdPairs
        pref = [0]
        running = 0
        values = []

        for d in range(1, mx + 1):
            if exact[d]:
                running += exact[d]
                values.append(d)
                pref.append(running)

        # answer queries
        ans = []
        for k in queries:
            idx = bisect_right(pref, k)
            ans.append(values[idx - 1])

        return ans