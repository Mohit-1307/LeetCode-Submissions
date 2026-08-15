class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0

        for x in nums:
            xor ^= x

        if xor != 0:
            return len(nums)

        # Total XOR is 0.
        # If any element is non-zero, remove it.
        for x in nums:
            if x != 0:
                return len(nums) - 1

        # All elements are zero.
        return 0