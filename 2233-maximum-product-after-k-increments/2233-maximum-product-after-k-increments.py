class Solution:
    def maximumProduct(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7

        heapq.heapify(nums)

        for _ in range(k):
            smallest = heapq.heappop(nums)
            heapq.heappush(nums, smallest + 1)

        ans = 1

        for num in nums:
            ans = (ans * num) % MOD

        return ans