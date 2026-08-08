class Solution:
    def captureForts(self, forts: List[int]) -> int:
        prev = -1
        ans = 0

        for i, x in enumerate(forts):
            if x != 0:
                if prev != -1 and forts[prev] != x:
                    ans = max(ans, i - prev - 1)
                prev = i

        return ans