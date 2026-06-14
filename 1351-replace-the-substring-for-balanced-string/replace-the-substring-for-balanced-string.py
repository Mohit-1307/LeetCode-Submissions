class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4

        cnt = Counter(s)

        if all(cnt[c] == target for c in "QWER"):
            return 0

        ans = n
        left = 0

        for right in range(n):
            cnt[s[right]] -= 1

            while left <= right and all(cnt[c] <= target for c in "QWER"):
                ans = min(ans, right - left + 1)

                cnt[s[left]] += 1
                left += 1

        return ans
        