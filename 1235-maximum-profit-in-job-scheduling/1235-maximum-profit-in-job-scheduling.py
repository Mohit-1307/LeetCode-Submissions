class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        starts = [job[0] for job in jobs]
        n = len(jobs)

        @lru_cache(None)
        def dp(i):
            if i == n:
                return 0

            # Skip current job
            skip = dp(i + 1)

            # Take current job
            next_idx = bisect_left(starts, jobs[i][1])
            take = jobs[i][2] + dp(next_idx)

            return max(skip, take)

        return dp(0)