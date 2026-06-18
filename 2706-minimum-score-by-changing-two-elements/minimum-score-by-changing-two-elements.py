class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        return min(
            nums[n - 3] - nums[0],      # remove 2 largest
            nums[n - 1] - nums[2],      # remove 2 smallest
            nums[n - 2] - nums[1]       # remove 1 smallest, 1 largest
        )