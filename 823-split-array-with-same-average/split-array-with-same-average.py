class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        # Necessary condition
        possible = False
        for k in range(1, n):
            if total * k % n == 0:
                possible = True
                break
        if not possible:
            return False

        m = n // 2
        left = nums[:m]
        right = nums[m:]

        left_sums = defaultdict(set)
        right_sums = defaultdict(set)

        # All subset sums of left half
        for mask in range(1 << len(left)):
            s = 0
            cnt = 0
            for i in range(len(left)):
                if mask & (1 << i):
                    s += left[i]
                    cnt += 1
            left_sums[cnt].add(s)

        # All subset sums of right half
        for mask in range(1 << len(right)):
            s = 0
            cnt = 0
            for i in range(len(right)):
                if mask & (1 << i):
                    s += right[i]
                    cnt += 1
            right_sums[cnt].add(s)

        for k in range(1, n):
            if total * k % n:
                continue

            target = total * k // n

            for lsize in range(max(0, k - len(right)),
                               min(k, len(left)) + 1):

                rsize = k - lsize

                for lsum in left_sums[lsize]:
                    if target - lsum in right_sums[rsize]:
                        # exclude choosing all elements
                        if k < n:
                            return True

        return False