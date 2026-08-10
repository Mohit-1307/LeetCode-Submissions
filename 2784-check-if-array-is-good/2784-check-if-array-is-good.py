class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mx = max(nums)

        if len(nums) != mx + 1:
            return False

        freq = Counter(nums)

        if freq[mx] != 2:
            return False

        for i in range(1, mx):
            if freq[i] != 1:
                return False

        return True