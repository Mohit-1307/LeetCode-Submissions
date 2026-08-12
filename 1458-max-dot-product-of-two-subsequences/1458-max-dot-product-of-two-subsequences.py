class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        NEG = float('-inf')

        dp = [[NEG] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                prod = nums1[i] * nums2[j]

                dp[i][j] = max(
                    prod,
                    prod + max(0, dp[i + 1][j + 1]),
                    dp[i + 1][j],
                    dp[i][j + 1]
                )

        return dp[0][0]