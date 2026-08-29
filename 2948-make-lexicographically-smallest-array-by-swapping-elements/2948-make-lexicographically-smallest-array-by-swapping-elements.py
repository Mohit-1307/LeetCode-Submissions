class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)

        # (value, original_index)
        arr = sorted((value, i) for i, value in enumerate(nums))

        ans = [0] * n

        left = 0

        while left < n:
            right = left

            # Find one connected group
            while (
                right + 1 < n
                and arr[right + 1][0] - arr[right][0] <= limit
            ):
                right += 1

            # Values in this group
            values = [arr[i][0] for i in range(left, right + 1)]

            # Original indices in this group
            indices = sorted(arr[i][1] for i in range(left, right + 1))

            # Smallest values -> smallest indices
            for idx, value in zip(indices, values):
                ans[idx] = value

            left = right + 1

        return ans