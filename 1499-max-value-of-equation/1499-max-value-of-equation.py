from collections import deque

class Solution:
    def findMaxValueOfEquation(self, points, k):
        dq = deque()  # stores [x, y - x]
        ans = float("-inf")

        for x, y in points:

            # Remove points outside the allowed x-distance
            while dq and x - dq[0][0] > k:
                dq.popleft()

            # Best previous point is at the front
            if dq:
                ans = max(ans, dq[0][1] + y + x)

            # Current point becomes a candidate for future points.
            value = y - x

            # Remove worse candidates from the back
            while dq and dq[-1][1] <= value:
                dq.pop()

            dq.append((x, value))

        return ans