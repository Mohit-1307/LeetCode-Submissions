class Solution:
    def numberOfWays(self, s: str) -> int:
        left0 = left1 = 0
        right0 = s.count('0')
        right1 = len(s) - right0

        ans = 0

        for ch in s:
            if ch == '0':
                right0 -= 1

                # pattern 101
                ans += left1 * right1

                left0 += 1
            else:
                right1 -= 1

                # pattern 010
                ans += left0 * right0

                left1 += 1

        return ans