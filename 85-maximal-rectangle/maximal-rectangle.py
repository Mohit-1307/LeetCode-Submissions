class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        ans = 0

        for r in range(rows):

            # Build histogram
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0

            # Largest Rectangle in Histogram
            stack = []
            for i in range(cols + 1):

                curr_height = 0 if i == cols else heights[i]

                while stack and heights[stack[-1]] > curr_height:
                    h = heights[stack.pop()]

                    left = stack[-1] if stack else -1
                    width = i - left - 1

                    ans = max(ans, h * width)

                stack.append(i)

        return ans