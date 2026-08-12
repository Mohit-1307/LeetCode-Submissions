class Solution:
    def minimumChairs(self, s: str) -> int:
        current = 0
        ans = 0

        for event in s:
            if event == 'E':
                current += 1
                ans = max(ans, current)
            else:
                current -= 1

        return ans