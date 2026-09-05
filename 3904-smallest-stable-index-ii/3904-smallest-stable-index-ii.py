class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Build suffix minimum in-place in a separate array
        suf = nums[:]

        for i in range(n - 2, -1, -1):
            suf[i] = min(suf[i], suf[i + 1])

        mx = 0

        for i, x in enumerate(nums):
            mx = max(mx, x)

            if mx - suf[i] <= k:
                return i

        return -1