class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Prefix sums after mapping target->+1, others->-1
        prefix = [0]
        s = 0
        for x in nums:
            s += 1 if x == target else -1
            prefix.append(s)

        # Coordinate compression
        vals = sorted(set(prefix))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        # Fenwick Tree
        bit = [0] * (len(vals) + 2)

        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        ans = 0
        for p in prefix:
            idx = rank[p]
            # Count previous prefix sums strictly smaller
            ans += query(idx - 1)
            update(idx)

        return ans