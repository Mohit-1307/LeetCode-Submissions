class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        mn = min(nums1)

        # If minimum is odd, every even number has a
        # smaller odd number to subtract.
        # If minimum is even, all numbers must be even.
        return mn % 2 == 1 or all(x % 2 == 0 for x in nums1)