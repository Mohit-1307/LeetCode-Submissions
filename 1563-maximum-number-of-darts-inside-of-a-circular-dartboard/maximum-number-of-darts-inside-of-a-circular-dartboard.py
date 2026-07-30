class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        n = len(darts)
        if n == 1:
            return 1

        ans = 1
        rr = r * r
        eps = 1e-7

        def count(cx, cy):
            cnt = 0
            for x, y in darts:
                if (x - cx) ** 2 + (y - cy) ** 2 <= rr + eps:
                    cnt += 1
            return cnt

        for i in range(n):
            x1, y1 = darts[i]
            for j in range(i + 1, n):
                x2, y2 = darts[j]

                dx = x2 - x1
                dy = y2 - y1
                d = math.hypot(dx, dy)

                if d > 2 * r + eps:
                    continue

                mx = (x1 + x2) / 2
                my = (y1 + y2) / 2

                if d == 0:
                    continue

                h = math.sqrt(rr - (d / 2) ** 2)

                ux = -dy / d
                uy = dx / d

                cx1 = mx + h * ux
                cy1 = my + h * uy

                cx2 = mx - h * ux
                cy2 = my - h * uy

                ans = max(ans, count(cx1, cy1))
                ans = max(ans, count(cx2, cy2))

        return ans