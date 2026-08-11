class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]

        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            prefix_sum += nums[i]
            i += 1

        seen = set(nums)

        while prefix_sum in seen:
            prefix_sum += 1

        return prefix_sum