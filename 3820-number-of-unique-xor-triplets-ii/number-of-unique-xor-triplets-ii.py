class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAXX = 2048

        # dp[k][x] = can obtain xor x using exactly k distinct elements
        dp = [[False] * MAXX for _ in range(4)]
        dp[0][0] = True

        for v in nums:
            for k in range(2, -1, -1):
                cur = dp[k]
                nxt = dp[k + 1]
                for x in range(MAXX):
                    if cur[x]:
                        nxt[x ^ v] = True

        ans = [False] * MAXX

        # Case 1: repeated indices -> original values
        for v in nums:
            ans[v] = True

        # Case 2: three distinct indices
        for x in range(MAXX):
            if dp[3][x]:
                ans[x] = True

        return sum(ans)