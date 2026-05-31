class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        low, high = 0, m

        while low <= high:

            cut1 = (low + high) // 2
            cut2 = (m + n + 1) // 2 - cut1

            # Left values
            left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]

            # Right values
            right1 = float('inf') if cut1 == m else nums1[cut1]
            right2 = float('inf') if cut2 == n else nums2[cut2]

            # Correct partition
            if left1 <= right2 and left2 <= right1:

                # Odd total length
                if (m + n) % 2 == 1:
                    return max(left1, left2)

                # Even total length
                return (max(left1, left2) + min(right1, right2)) / 2

            # Move left
            elif left1 > right2:
                high = cut1 - 1

            # Move right
            else:
                low = cut1 + 1