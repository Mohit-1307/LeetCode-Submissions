class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        # Convert stones into prefix sums in-place.
        for i in range(1, n):
            stones[i] += stones[i - 1]

        ans = stones[-1]

        for i in range(n - 2, 0, -1):
            ans = max(ans, stones[i] - ans)

        return ans