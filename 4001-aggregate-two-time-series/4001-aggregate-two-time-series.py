class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        n, m = len(series1), len(series2)

        # Merge timestamps
        timestamps = []
        a = b = 0

        while a < n and b < m:
            if series1[a][0] < series2[b][0]:
                timestamps.append(series1[a][0])
                a += 1
            elif series1[a][0] > series2[b][0]:
                timestamps.append(series2[b][0])
                b += 1
            else:
                timestamps.append(series1[a][0])
                a += 1
                b += 1

        while a < n:
            timestamps.append(series1[a][0])
            a += 1

        while b < m:
            timestamps.append(series2[b][0])
            b += 1

        ans = []
        i = j = 0

        for t in timestamps:
            while i < n and series1[i][0] < t:
                i += 1
            while j < m and series2[j][0] < t:
                j += 1

            v1 = series1[i][1] if i < n else 0
            v2 = series2[j][1] if j < m else 0

            ans.append([t, v1 + v2])

        return ans