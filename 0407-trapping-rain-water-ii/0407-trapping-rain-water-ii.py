import heapq

class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])

        if m < 3 or n < 3:
            return 0

        heap = []
        visited = [[False] * n for _ in range(m)]

        # Put all boundary cells into the min-heap
        for r in range(m):
            for c in (0, n - 1):
                heapq.heappush(heap, (heightMap[r][c], r, c))
                visited[r][c] = True

        for c in range(1, n - 1):
            for r in (0, m - 1):
                heapq.heappush(heap, (heightMap[r][c], r, c))
                visited[r][c] = True

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        water = 0

        while heap:
            height, r, c = heapq.heappop(heap)

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Outside grid or already processed
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if visited[nr][nc]:
                    continue

                visited[nr][nc] = True

                neighbor_height = heightMap[nr][nc]

                # Water trapped at this cell
                if neighbor_height < height:
                    water += height - neighbor_height

                # Effective boundary height
                new_height = max(height, neighbor_height)

                heapq.heappush(heap, (new_height, nr, nc))

        return water