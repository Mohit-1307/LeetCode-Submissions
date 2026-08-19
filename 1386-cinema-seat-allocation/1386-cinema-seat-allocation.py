class Solution:
    def maxNumberOfFamilies(
        self,
        n: int,
        reservedSeats: List[List[int]]
    ) -> int:

        rows = {}

        # Store reservations using a bitmask for each affected row.
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                rows[row] = rows.get(row, 0) | (1 << seat)

        # Rows with no relevant reservations can always fit 2 groups.
        ans = 2 * (n - len(rows))

        LEFT = 60    # seats 2,3,4,5
        MIDDLE = 240  # seats 4,5,6,7
        RIGHT = 960   # seats 6,7,8,9

        for mask in rows.values():

            left_free = (mask & LEFT) == 0
            right_free = (mask & RIGHT) == 0

            if left_free and right_free:
                # (2-5) + (6-9)
                ans += 2

            elif left_free or right_free:
                # One of the two outer groups is possible.
                ans += 1

            elif (mask & MIDDLE) == 0:
                # Only the middle group is possible.
                ans += 1

        return ans