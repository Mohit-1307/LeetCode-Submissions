class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # Number of elements in the array
        n = len(nums)

        # Find positions of minimum and maximum values
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # left = leftmost target
        # right = rightmost target
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # Three possible strategies:
        #
        # 1. Remove both from the front
        #    Need to reach index 'right'
        front = right + 1

        # 2. Remove both from the back
        #    Need to reach index 'left'
        back = n - left

        # 3. Remove left target from front
        #    and right target from back
        both_sides = left + 1 + n - right

        # Choose the cheapest strategy
        return min(front, back, both_sides)