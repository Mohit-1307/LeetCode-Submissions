class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        # Initialize with first possible sum
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                current_sum = nums[i] + nums[left] + nums[right]

                # Update closest sum
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum

                # Exact match
                if current_sum == target:
                    return current_sum

                # Move pointers
                elif current_sum < target:
                    left += 1

                else:
                    right -= 1

        return closest