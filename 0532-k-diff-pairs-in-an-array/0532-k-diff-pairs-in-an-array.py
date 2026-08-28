class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        if k < 0:
            return 0

        if k == 0:
            freq = set()
            ans = set()

            for x in nums:
                if x in freq:
                    ans.add(x)
                else:
                    freq.add(x)

            return len(ans)

        seen = set()
        ans = set()

        for x in nums:
            if x - k in seen:
                ans.add((x - k, x))

            if x + k in seen:
                ans.add((x, x + k))

            seen.add(x)

        return len(ans)