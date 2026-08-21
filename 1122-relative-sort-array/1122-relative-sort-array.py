from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        freq = Counter(arr1)

        result = []

        # Elements that appear in arr2
        for x in arr2:
            result.extend([x] * freq[x])
            freq[x] = 0

        # Remaining elements in ascending order
        remaining = []

        for x, count in freq.items():
            remaining.extend([x] * count)

        remaining.sort()

        return result + remaining