from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        # Assign a bit to every litter cell.
        litter = {}
        sr = sc = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        k = len(litter)

        # No litter to collect.
        if k == 0:
            return 0

        full_mask = (1 << k) - 1

        # best[r][c][mask] = maximum energy with which
        # we've reached (r, c) having collected `mask`.
        #
        # energy <= 50, so bytearray is sufficient.
        best = [
            [bytearray(1 << k) for _ in range(n)]
            for _ in range(m)
        ]

        q = deque([(sr, sc, 0, energy)])
        best[sr][sc][0] = energy

        directions = (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        )

        moves = 0

        while q:
            for _ in range(len(q)):
                r, c, mask, e = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    # Need energy to make the move.
                    if e == 0:
                        continue

                    ne = e - 1
                    nmask = mask

                    # Collect litter.
                    if classroom[nr][nc] == 'L':
                        nmask |= 1 << litter[(nr, nc)]

                    # If we collected everything, we're done.
                    # This is important even when ne == 0.
                    if nmask == full_mask:
                        return moves + 1

                    # Reset energy immediately upon entering R.
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    # If no energy remains and we're not on R,
                    # this state cannot make another move.
                    if ne == 0:
                        continue

                    # Dominance:
                    # same position + same collected litter,
                    # but having more energy is always better.
                    if ne <= best[nr][nc][nmask]:
                        continue

                    best[nr][nc][nmask] = ne
                    q.append((nr, nc, nmask, ne))

            moves += 1

        return -1