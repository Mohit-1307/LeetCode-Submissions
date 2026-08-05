class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def toMinutes(t):
            h, m = map(int, t.split(":"))
            return h * 60 + m

        diff = toMinutes(correct) - toMinutes(current)

        ans = 0
        for x in [60, 15, 5, 1]:
            ans += diff // x
            diff %= x

        return ans