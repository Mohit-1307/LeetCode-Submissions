from bisect import bisect_right
from functools import lru_cache
from typing import List


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # Store: [left, right, weight, original_index]
        arr = [
            [l, r, w, i]
            for i, (l, r, w) in enumerate(intervals)
        ]

        # Sort by left endpoint
        arr.sort(key=lambda x: x[0])

        starts = [x[0] for x in arr]

        # next[i] = first interval j such that starts[j] > arr[i].right
        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        # dp(i, k) returns:
        # (maximum score, lexicographically smallest tuple of indices)
        @lru_cache(None)
        def dp(i: int, k: int):
            if i == n or k == 0:
                return (0, ())

            # Option 1: skip current interval
            skip_score, skip_indices = dp(i + 1, k)

            # Option 2: take current interval
            take_score, take_indices = dp(nxt[i], k - 1)

            take_score += arr[i][2]
            take_indices = tuple(sorted(
                take_indices + (arr[i][3],)
            ))

            # Choose maximum score.
            # If scores tie, choose lexicographically smaller indices.
            if take_score > skip_score:
                return take_score, take_indices
            elif take_score < skip_score:
                return skip_score, skip_indices
            else:
                return (
                    skip_score,
                    min(skip_indices, take_indices)
                )

        return list(dp(0, 4)[1])