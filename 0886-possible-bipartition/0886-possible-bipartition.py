class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        graph = [[] for _ in range(n + 1)]

        # Build graph
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        # color[i] = 0  -> uncolored
        # color[i] = 1  -> group 1
        # color[i] = -1 -> group 2
        color = [0] * (n + 1)

        for person in range(1, n + 1):
            if color[person] != 0:
                continue

            # Start a new connected component
            color[person] = 1
            queue = deque([person])

            while queue:
                u = queue.popleft()

                for v in graph[u]:

                    # Same group -> impossible
                    if color[v] == color[u]:
                        return False

                    # Assign opposite group
                    if color[v] == 0:
                        color[v] = -color[u]
                        queue.append(v)

        return True