class Solution:
    def addOperators(self, num: str, target: int):
        n = len(num)
        ans = []

        def dfs(pos, expr, curr_val, prev):
            if pos == n:
                if curr_val == target:
                    ans.append(expr)
                return

            for i in range(pos, n):

                # No leading zeros
                if i > pos and num[pos] == '0':
                    break

                s = num[pos:i + 1]
                curr = int(s)

                # First number
                if pos == 0:
                    dfs(i + 1, s, curr, curr)

                else:
                    # +
                    dfs(
                        i + 1,
                        expr + "+" + s,
                        curr_val + curr,
                        curr
                    )

                    # -
                    dfs(
                        i + 1,
                        expr + "-" + s,
                        curr_val - curr,
                        -curr
                    )

                    # *
                    dfs(
                        i + 1,
                        expr + "*" + s,
                        curr_val - prev + prev * curr,
                        prev * curr
                    )

        dfs(0, "", 0, 0)
        return ans