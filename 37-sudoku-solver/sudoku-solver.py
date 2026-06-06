class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empty = []

        # Initialize sets
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    num = board[r][c]
                    box = (r // 3) * 3 + (c // 3)

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

        def backtrack(idx: int) -> bool:
            if idx == len(empty):
                return True

            r, c = empty[idx]
            box = (r // 3) * 3 + (c // 3)

            for digit in "123456789":
                if (
                    digit not in rows[r]
                    and digit not in cols[c]
                    and digit not in boxes[box]
                ):
                    board[r][c] = digit

                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box].add(digit)

                    if backtrack(idx + 1):
                        return True

                    board[r][c] = "."

                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box].remove(digit)

            return False

        backtrack(0)