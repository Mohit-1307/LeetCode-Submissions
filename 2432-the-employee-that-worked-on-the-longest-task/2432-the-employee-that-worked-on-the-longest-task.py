class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        prev = 0
        maxTime = 0
        ans = 0

        for emp, leave in logs:
            duration = leave - prev

            if duration > maxTime or (duration == maxTime and emp < ans):
                maxTime = duration
                ans = emp

            prev = leave

        return ans