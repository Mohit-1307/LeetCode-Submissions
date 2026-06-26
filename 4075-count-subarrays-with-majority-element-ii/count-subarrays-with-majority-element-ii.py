class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Fenwick Tree
        size = 2 * n + 5
        bit = [0] * size

        def update(i, delta):
            while i < size:
                bit[i] += delta
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        offset = n + 2
        pref = 0
        ans = 0

        # Initial prefix sum = 0
        update(offset, 1)

        for x in nums:
            if x == target:
                pref += 1
            else:
                pref -= 1

            idx = pref + offset

            # Count previous prefix sums < current prefix sum
            ans += query(idx - 1)

            update(idx, 1)

        return ans