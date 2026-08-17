class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        # prefix[i] = sum of stoneValue[0:i]
        prefix = list(accumulate(stoneValue, initial=0))

        @lru_cache(None)
        def dfs(l: int, r: int) -> int:
            if l >= r:
                return 0

            ans = 0

            left_sum = 0
            right_sum = prefix[r + 1] - prefix[l]

            for k in range(l, r):
                left_sum += stoneValue[k]
                right_sum -= stoneValue[k]

                if left_sum < right_sum:

                    # Alice keeps the left part.
                    #
                    # If ans >= 2 * left_sum, then:
                    #
                    # left_sum + dfs(l,k) <= 2*left_sum <= ans
                    #
                    # so this split cannot improve the answer.
                    if ans >= 2 * left_sum:
                        continue

                    ans = max(
                        ans,
                        left_sum + dfs(l, k)
                    )

                elif left_sum > right_sum:

                    # Alice keeps the right part.
                    #
                    # As k moves right, right_sum only decreases.
                    # If ans >= 2 * right_sum, no later split
                    # can improve the answer.
                    if ans >= 2 * right_sum:
                        break

                    ans = max(
                        ans,
                        right_sum + dfs(k + 1, r)
                    )

                else:
                    # Equal sums -> Alice chooses either side.
                    ans = max(
                        ans,
                        left_sum + dfs(l, k),
                        right_sum + dfs(k + 1, r)
                    )

            return ans

        return dfs(0, n - 1)